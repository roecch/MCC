'use strict'

const switcher = document.querySelector('.btn');

switcher.addEventListener('click', function() {
  document.body.classList.toggle('dark-theme')

  var className = document.body.className;
  if(className == "light-theme") {
    this.textContent = "Dark";
  }
  else {
    this.textContent = "Light";
  }
  console.log('current class name: ' + className);
});


const players1to9 = document.getElementById('1-9');
const playersAtoD = document.getElementById('A-D');
const playersEtoI = document.getElementById('E-I');
const playersJtoK = document.getElementById('J-K');
const playersLtoP = document.getElementById('L-P');
const playersQtoS = document.getElementById('Q-S');
const playersTtoZ = document.getElementById('T-Z');
const playerMap = getPlayerImgMap();

window.onload = (event) => {
  console.log(playerMap);
  console.log(playerMap.keys());
  console.log(playerMap.entries());

  for (let [index,value] of playerMap.entries()) {
    let img = document.createElement("img");
    img.src = value;
    img.alt = index + " Icon";
    img.draggable = false;
    img.setAttribute("id", "player" + index)
    img.setAttribute("class", "player")
    let imgDiv = document.createElement("p");
    imgDiv.appendChild(img)
    if (['1','2','3','4','5','6','7','8','9'].includes(index.substring(0,1)))
      players1to9.appendChild(imgDiv);
    else if (['A','B','C','D'].includes(index.substring(0,1)))
      playersAtoD.appendChild(imgDiv);
    else if (['E','F','G','H','I'].includes(index.substring(0,1)))
      playersEtoI.appendChild(imgDiv);
    else if (['J','K'].includes(index.substring(0,1)))
      playersJtoK.appendChild(imgDiv);
    else if (['L','M','N','O','P'].includes(index.substring(0,1)))
      playersLtoP.appendChild(imgDiv);
    else if (['Q','R','S'].includes(index.substring(0,1)))
      playersQtoS.appendChild(imgDiv);
    else if (['T','U','V','W','X','Y','Z'].includes(index.substring(0,1)))
      playersTtoZ.appendChild(imgDiv);
  }};


const players = document.querySelectorAll('player')
console.log(players)

for (let play of players) {
  dragElement(play)
  console.log(play)
}

function dragElement(elmnt) {
  var pos1 = 0, pos2 = 0, pos3 = 0, pos4 = 0;
  if (document.getElementById(elmnt.id + "header")) {
    // if present, the header is where you move the DIV from:
    document.getElementById(elmnt.id + "header").onmousedown = dragMouseDown;
  } else {
    // otherwise, move the DIV from anywhere inside the DIV:
    elmnt.onmousedown = dragMouseDown;
  }

  function dragMouseDown(e) {
    e = e || window.event;
    e.preventDefault();
    // get the mouse cursor position at startup:
    pos3 = e.clientX;
    pos4 = e.clientY;
    document.onmouseup = closeDragElement;
    // call a function whenever the cursor moves:
    document.onmousemove = elementDrag;
  }

  function elementDrag(e) {
    e = e || window.event;
    e.preventDefault();
    // calculate the new cursor position:
    pos1 = pos3 - e.clientX;
    pos2 = pos4 - e.clientY;
    pos3 = e.clientX;
    pos4 = e.clientY;
    // set the element's new position:
    elmnt.style.top = (elmnt.offsetTop - pos2) + "px";
    elmnt.style.left = (elmnt.offsetLeft - pos1) + "px";
  }

  function closeDragElement() {
    // stop moving when mouse button is released:
    document.onmouseup = null;
    document.onmousemove = null;
  }
}



