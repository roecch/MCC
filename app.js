'use strict'

const players_menu = document.getElementById('vertical-menu');
const playerMap = getPlayerImgMap();

window.onload = () => {
    for (let [index, value] of playerMap.entries()) {
        let img = document.createElement("img");
        img.src = value.toString();
        img.alt = index + " Icon";
        img.draggable = true;
        img.setAttribute("class", "player")
        img.setAttribute("height", '50px')
        img.setAttribute("width", '50px')

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

        players_menu.appendChild(imgAndTextDiv);
    }
};

const source = document.getElementsByClassName("draggable");
console.log(source)
const target = document.getElementsByClassName("droppable");
console.log(target)
const event_log = document.getElementById("event-log");

for (let item of source) {
    item.addEventListener('click', function handleClick() {
        // event_log.textContent += "click\n";
        item.setAttribute('style', 'background-color: yellow;');
    });

    item.addEventListener('dragstart', function dragstart_handler(ev) {
        // event_log.textContent += "dragStart\n";
        // Change the source element's background color to signify drag has started
        item.setAttribute('style', 'background-color: yellow;');
        ev.dataTransfer.setData("text", ev.target.id);
    });
}

for (let item of target) {
    item.addEventListener('dragenter',  function dragenter_handler(ev) {
        // event_log.textContent += "dragEnter\n";
        ev.preventDefault()
    });

    item.addEventListener('dragleave', function dragleave_handler(ev) {
        ev.preventDefault()
        // ev.target.style.border = '2px solid #ccc'
    });

    item.addEventListener('dragover', function dragover_handler(ev) {
        ev.preventDefault()
        // ev.target.style.border = '1px solid green'
    });

    item.addEventListener('drop', function drop_handler(ev) {
        // event_log.textContent += "drop\n";
        ev.preventDefault()
        let data = ev.dataTransfer.getData('text')
        console.log(data)
        data = data.substring(data.lastIndexOf('/') + 1, data.indexOf('.'))
        console.log(data)
        const newElement = document.getElementById(data)
        const style = getComputedStyle(ev.target)
        newElement.firstElementChild.setAttribute('height', style.height)
        newElement.firstElementChild.setAttribute('width', style.width)

        newElement.setAttribute('height', style.height)
        newElement.setAttribute('width', style.width)

        console.log(newElement)
        ev.target.appendChild(newElement)
        // ev.target.style.border = 'none'
        newElement.style.border = 'none'
        ev.dataTransfer.clearData()
    });
}

// Set click event listener on button to reload the example
const button = document.getElementById("reload");
button.addEventListener("click", () => {
    display_team_coin_avg()
    // document.location.reload();
});

function get_players_under_each_team() {
    let all_team_holders = document.getElementById('droppable-holder').children;
    all_team_holders = Array.from(all_team_holders).filter(function(str) {
        return str.id.startsWith('droppable-') && str.id.endsWith('-holder')
    });
    console.log(all_team_holders)
    let players_under_each_team = [];
    for (let key in all_team_holders) {
        let teamArray = [...all_team_holders[key].children]
        const team_color = teamArray[0].className.split('-')[1]

        teamArray = teamArray.map((player_holder) => {
            let player_div_data = player_holder.innerHTML
            player_div_data = player_div_data.substring(player_div_data.indexOf('id=\"') + 4)
            console.log(player_div_data.substring(0, player_div_data.indexOf('\"')))
            return player_div_data.substring(0, player_div_data.indexOf('\"'))})
        players_under_each_team[team_color] = teamArray
    }
    return players_under_each_team
}

let players_by_team;
function get_latest_changed_players() {
    let last_players_by_team = players_by_team;
    players_by_team = get_players_under_each_team()
    let hash_of_changes_players = [];

    for (let key in players_by_team) {
        console.log(key)
        let current_team_state = players_by_team[key]
        let prev_team_state;
        try {
            prev_team_state = last_players_by_team[key]
        } catch(e) {
            prev_team_state = ['','','','']
        }
        if (current_team_state !== prev_team_state) {
            let difference = current_team_state.filter(x => !prev_team_state.includes(x));
            hash_of_changes_players[key] = difference.map((index) => current_team_state.indexOf(index))
        }
    }
    console.log(hash_of_changes_players)
    return hash_of_changes_players
}

$(document).ready(function() {
    document.getElementsByTagName("html")[0].style.visibility = "visible";
});

const team_points_holders = document.getElementsByClassName('team-points')

function display_team_coin_avg() {
}