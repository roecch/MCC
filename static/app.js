'use strict'

const players_menu = document.getElementById('vertical-menu');
const playerMap = getPlayerImgMap();

window.onload = () => {
  set_menu()
  set_drag_drop()
  updating_player_card()
};

//document.addEventListener('DOMContentLoaded', (event) => {
//    set_menu();
//    set_drag_drop();
//    updating_player_card();
//});

function set_menu() {
  for (let [index, value] of playerMap.entries()) {
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
    item.addEventListener('click', function handleClick() {
      // item.setAttribute('style', 'background-color: yellow;');
    });

    item.addEventListener('dragstart', function dragstart_handler(ev) {
      // item.setAttribute('style', 'background-color: yellow;');
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
}

const pn = document.getElementById('pn');

function updating_player_card() {
  const players_vm = document.getElementsByClassName("img-txt-div");
  for (let item of players_vm) {
    item.addEventListener('mouseover', function () {
      pn.innerHTML = item.firstElementChild.id
      $.ajax({
        type: "GET",
        url: "/retrieve",
        data: {name: item.firstElementChild.id},
        success: function (data) {
          console.log(data)
        },
        error: function () {
          alert('something bad happened');
        }
      });
    })
  }
}

function get_players_under_each_team() {
  let all_team_holders = document.getElementById('droppable-holder').children;
  all_team_holders = Array.from(all_team_holders).filter(function (str) {
    return str.id.startsWith('droppable-') && str.id.endsWith('-holder')
  });
  console.log(all_team_holders)
  let players_under_each_team = [];
  for (let key in all_team_holders) {
    let teamArray = [...all_team_holders[key].children]
    const team_color = teamArray[0].className.split('-')[1]

    teamArray = teamArray.map((player_holder) => {
      let player_div_data = player_holder.innerHTML
      player_div_data = player_div_data.substring(
          player_div_data.indexOf('id=\"') + 4)
      console.log(player_div_data.substring(0, player_div_data.indexOf('\"')))
      return player_div_data.substring(0, player_div_data.indexOf('\"'))
    })
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
  console.log(hash_of_changes_players)
  return hash_of_changes_players
}

const team_points_holders = document.getElementsByClassName('team-points')

function display_team_coin_avg() {
}