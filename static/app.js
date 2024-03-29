'use strict'

const players_menu = document.getElementById('vertical-menu');
const player_map = getPlayerImgMap();

window.onload = () => {
    window.setTimeout(function () {
        set_menu()
        set_drag_drop()
        updating_player_card()
    }, 1)
};


function set_menu() {
    console.log(player_map.size)
    for (let [index, value] of player_map.entries()) {
        console.log('done')
        let img = document.createElement("img");
        img.src = value.toString();
        img.alt = index + " Icon";
        img.draggable = true;
        img.setAttribute("class", "player")
        img.setAttribute("height", '40px')
        img.setAttribute("width", '40px')

        let imgDiv = document.createElement("player-div")
        let text = document.createTextNode(index.toString())
        let imgAndTextDiv = document.createElement("div")
        let textDiv = document.createElement("a")

        imgDiv.appendChild(img)
        imgDiv.classList.add("draggable");
        imgDiv.setAttribute('draggable', 'true')

        imgDiv.id = index.toString();

        textDiv.appendChild(text)
        textDiv.classList.add("text-for-img")

        imgAndTextDiv.appendChild(imgDiv)
        imgAndTextDiv.appendChild(textDiv)
        imgAndTextDiv.classList.add("img-txt-div")

        players_menu.appendChild(imgAndTextDiv);
    }
}

function set_drag_drop() {
    const source = document.getElementsByClassName("draggable");
    const target = document.getElementsByClassName("droppable");

    for (let item of source) {
        item.addEventListener('dragstart', function dragstart_handler(ev) {
            ev.dataTransfer.setData("text", ev.target.id);
        });
    }

    for (let item of target) {
        item.addEventListener('dragenter', function dragenter_handler(ev) {
            ev.preventDefault()
        });

        item.addEventListener('dragleave', function dragleave_handler(ev) {
            ev.preventDefault()
        });

        item.addEventListener('dragover', function dragover_handler(ev) {
            ev.preventDefault()
        });

        item.addEventListener('drop', function drop_handler(ev) {
            ev.preventDefault()
            let data = ev.dataTransfer.getData('text')
            data = data.substring(data.lastIndexOf('/') + 1, data.lastIndexOf('.'))
            const newElement = document.getElementById(data)
            const style = getComputedStyle(ev.target)
            newElement.firstElementChild.setAttribute('height', style.height)
            newElement.firstElementChild.setAttribute('width', style.width)

            newElement.setAttribute('height', style.height)
            newElement.setAttribute('width', style.width)

            ev.target.appendChild(newElement)
            newElement.style.border = 'none'

            update_team_coins()

            ev.dataTransfer.clearData()
        });
    }
}

const pn = document.getElementById('pn');

function updating_player_card() {
    const players_vm = document.getElementsByClassName("img-txt-div");
    for (let item of players_vm) {
        item.addEventListener('mouseover', function () {
            // window.setTimeout(function () {
            if (pn.innerHTML !== item.firstElementChild.id && item.firstElementChild.id !== '') {
                let img = document.createElement("img");
                img.id = 'skinImgDiv'
                img.src = "https://mc-heads.net/body/" + get_ign_for_name(item.firstElementChild.id) + "/right";
                let oldImg = document.getElementById('skinImgDiv');
                document.getElementById('skin').replaceChild(img, oldImg)

                pn.innerHTML = item.firstElementChild.id
                $.ajax({
                    type: "GET",
                    url: "/retrieve",
                    data: {name: item.firstElementChild.id},
                    success: function (data) {
                        console.log(data)
                        updating_player_card_helper(data)
                    },
                    error: function () {
                        alert('something bad happened');
                    }
                });
            }
            // }, 500)
        })
    }
}

function updating_player_card_helper(data) {
    let pc_holders = document.getElementsByClassName('pc')
    console.log(pc_holders)
    Array.from(pc_holders).slice(1, -1).forEach(function (item, index) {
        console.log(item.innerHTML)
        item.innerHTML = data[index]
        // if (item.id === 'avg') {
        //     return data[index]
        // }
    });
}

function get_players_under_each_team() {
    let all_team_holders = document.getElementById('all-team-holders').children;
    all_team_holders = Array.from(all_team_holders).filter(function (str) {
        return str.id.startsWith('droppable-') && str.id.endsWith('-holder')
    });
    let players_under_each_team = [];
    for (let key in all_team_holders) {
        let team_array = [...all_team_holders[key].children[0].children]
        const team_color = team_array[0].className.split('-')[1]

        team_array = team_array.map((player_holder) => {
            let player_div_data = player_holder.innerHTML
            player_div_data = player_div_data.substring(
                player_div_data.indexOf('id=\"') + 4)
            return player_div_data.substring(0, player_div_data.indexOf('\"'))
        })
        players_under_each_team[team_color] = team_array
    }
    return players_under_each_team
}

document.getElementById('arrow').addEventListener('click', function () {
    save_teams()
    location.href = "event";
})

function save_teams() {
    let teams = get_players_under_each_team();
    for (let key in teams) {
        window.sessionStorage.setItem(key, teams[key])
    }
    console.log({...sessionStorage})
}

let players_by_team;

function get_latest_changed_players() {
    let last_players_by_team = players_by_team;
    players_by_team = get_players_under_each_team()
    let hash_of_changes_players = [];

    for (let key in players_by_team) {
        let current_team_state = players_by_team[key]
        let prev_team_state;
        try {
            prev_team_state = last_players_by_team[key]
        } catch (e) {
            prev_team_state = ['', '', '', '']
        }
        if (current_team_state !== prev_team_state) {
            let difference = current_team_state.filter(
                x => !prev_team_state.includes(x));
            hash_of_changes_players[key] = difference.map(
                (index) => current_team_state.indexOf(index))
        }
    }
    return hash_of_changes_players
}

function update_team_coins() {
    let hash = get_latest_changed_players();
    let key = Object.keys(hash).filter(key => hash[key].length)[0]

    document.getElementById(key + '-team-points').innerHTML =
        (parseInt(document.getElementById(key + '-team-points').innerHTML)
            + parseInt(document.getElementById('avg').innerHTML)).toString()
}

function change_team_total_calc(choice) {
    let players_under_each_team = get_players_under_each_team()
    for (let players_of_team of players_under_each_team) {

    }
}

function get_ign_for_name(name) {
    console.log(name)

    var ignMap = {'5up' : '5uppps',
        'Eret' : 'The_Eret',
        'GoodTimesWithScar' : 'GoodTimeWithScar',
        'KingBurren' : 'King_Burren',
        'krtzzy' : 'Krtzy',
        'rtgame' : 'Magistrex',
        'shubble' : 'ShubbleYT',
        'spifey' : 'Spifeey',
        'Sylvee' : 'sylvee_',
        'TheOrionSound': 'OrionSound',
        'Tubbo' : 'Tubbo_'}

    if (ignMap[name] === undefined) {
        return name
    }
    else {
        return ignMap[name]
    }
}