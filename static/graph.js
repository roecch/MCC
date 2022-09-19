let games = ['AR', 'BB', 'BM', 'GR', 'HITW', 'PT', 'SOT', 'SG']
let team_data;
window.onload = () => {
    make_team_avgs_json({...sessionStorage}).then(res => make_graph(games, res))
};

function update_xaxis() {
    if (if_games_order_udpated()) {
        make_graph(games, team_data)
    }
}


function if_games_order_udpated() {
    let list = [...document.getElementById('game-choices').querySelectorAll('.draggable')];
    console.log(list)
    list = list.map(x => x.id.toUpperCase())
    list = list.slice(0,8);
    console.log(list)
    console.log(games)
    console.log(list.every((val, index) => val === games[index]))
    if (!list.every((val, index) => val === games[index])) {
        games = list
        console.log(games)
        return true;
    }
    return false;
}


function make_team_avgs_json(t) {
    return new Promise(res => {
        // convert object array
        let teams_map = Object.entries(t)

        $.ajax({
            type: "GET",
            url: "/get_data",
            data: {teams: JSON.stringify(teams_map)},
            success: function (data) {
                team_data = data
                res(data)
            },
            error: function () {
                alert('something bad happened');
            }
        })
    })
}


function make_graph(eight_games, data) {
    data = data.filter((d) => {
        return d.game !== "AVG" && eight_games.includes(d.game);
    });

    let margin = {top: 20, right: 20, bottom: 20, left: 50},
        width = 860 - margin.left - margin.right,
        height = 500 - margin.top - margin.bottom;

    // append the svg object to the body of the page
    // appends a 'group' element to 'svg'
    // moves the 'group' element to the top left margin
    const svg = d3.select("#vis-svg").append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .attr("transform",
            "translate(" + margin.left + "," + margin.top + ")");


    let xShift = 72;

    // Add X axis
    var x = d3.scaleBand()
        .domain(eight_games)
        .range([0, width]);
    var xAxis = svg.append("g")
        .attr("class", "x axis")
        .attr("transform", "translate(" + xShift + "," + height + ")")
        .call(d3.axisBottom(x));

    let xAxisGrid = d3.axisBottom(x)
        .tickSize(-height, 0)
        .tickFormat('')
    svg.append('g')
        .attr('class', 'x axis-grid')
        .attr('transform', 'translate(' + xShift + ',' + height + ')')
        .call(xAxisGrid);

    // Add Y axis
    var y = d3.scaleLinear()
        .domain([0, 20000])
        .range([height, 0]);
    var yAxis = svg.append("g")
        .attr("class", "y axis")
        .attr("transform", "translate(" + xShift + ",0)")
        .call(d3.axisLeft(y));


    var sumstat = d3.group(data, d => d.color)
    console.log(sumstat)
    console.log(sumstat.keys())


    // list of group names
    var color = d3.scaleOrdinal()
        // .domain(sumstat.keys())
        .domain(["red", "orange", "yellow", "lime", "green", "cyan", "aqua", "blue", "purple", "pink"])
        .range(['#FF0000', '#FFA500', '#FFFF00', '#00FF55', '#32CD32', '#00FFFF', '#008B8B', '#0000FF', '#AA00FF', '#FF69B4'])


    // Draw the line
    let lines = svg.selectAll(".line")
        .data(sumstat)
        .enter()
        .append("path")
        .attr('id', function (d) {
            return d[0]
        })
        .attr("fill", "none")
        .attr("stroke", function (d) {
            return color(d[0])
        })
        .attr("stroke-width", 1.5)
        .attr("transform", "translate(" + (xShift + (x.bandwidth() / 2)) + ",0)")
        .attr("d", function (d) {
            console.log(d)
            let p = 0
            let multiplitier = 1
            let inc_multi = false
            return d3.line()
                .x(function (d) {
                    if (inc_multi) {
                        multiplitier += 0.5
                        inc_multi = false
                    } else {
                        inc_multi = true
                    }
                    return x(d.game);
                })
                .y(function (d) {
                    p += (d.pts * multiplitier);
                    console.log(p)
                    return y(p);
                })
                (d[1])
        })
        .on("mouseover", function () {
            let cur = this
            d3.select(this).style("stroke-width", 5);
            d3.selectAll(lines).each(function () {
                if (this !== cur) {
                    // d3.select(this).style("stroke", '#999999')
                    d3.select(this).transition().duration('50').attr('opacity', '.25');
                }
            });
        })
        .on("mouseleave", function () {
            d3.select(this).style("stroke-width", 1.5);
            d3.selectAll(lines).each(function () {
                // d3.select(this).style("stroke", color[this.id])
                d3.select(this).transition().duration('50').attr('opacity', '1');
            })
        });

    let tooltip = d3.select("#vis-svg")
        .append("div")
        .attr('class', 'tooltip')
        .style("position", "absolute")
        .style("z-index", "10")
        .style("visibility", "hidden")

    //hover for line chart
    function hoverLine(event, d) {
        d3.select(this)
        let coords = d3.pointer(event, svg)
        let invertX = x.invertX(coords[0] - margin.left - 19)
        let invertY = height - (y.invert(coords[1] - 60) * -1)
        //Update Tooltip Position & value
        tooltip
            .style('top', coords[1] + 'px')
            .style('left', coords[0] + 'px')
            // .text(d[0] + "\n" + invertX + "\n" + invertY)
            .style("visibility", "visible")

    }
}

let draggingEle;
let x = 0;
let y = 0;
let placeholder;
let isDraggingStarted = false;


const mouseDownHandler = function (e) {
    draggingEle = e.target;

    // Calculate the mouse position
    const rect = draggingEle.getBoundingClientRect();
    // x = e.pageX - rect.left;
    // y = e.pageY - rect.top;
    x = e.clientX;
    y = e.clientY;

    // Attach the listeners to `document`
    document.addEventListener('mousemove', mouseMoveHandler);
    document.addEventListener('mouseup', mouseUpHandler);
};

const mouseMoveHandler = function (e) {
    const draggingRect = draggingEle.getBoundingClientRect();

    if (!isDraggingStarted) {
        // Update the flag
        isDraggingStarted = true;

        // Let the placeholder take the height of dragging element
        // So the next element won't move up
        placeholder = document.createElement('div');
        placeholder.classList.add('placeholder');
        draggingEle.parentNode.insertBefore(
            placeholder,
            draggingEle.nextSibling
        );

        // Set the placeholder's height
        placeholder.style.height = `${draggingRect.height}px`;
        placeholder.style.border = "thick solid #0000FF";
    }

    // Set position for dragging element
    draggingEle.style.position = 'absolute';
    draggingEle.style.top = `${e.pageY}px`;
    draggingEle.style.left = `${e.pageX - x}px`;

    const prevEle = draggingEle.previousElementSibling;
    const nextEle = placeholder.nextElementSibling;

    // User moves item to the top
    if (prevEle && isAbove(draggingEle, prevEle)) {
        // The current order    -> The new order
        // prevEle              -> placeholder
        // draggingEle          -> draggingEle
        // placeholder          -> prevEle
        swap(placeholder, draggingEle);
        swap(placeholder, prevEle);
        return;
    }

    // User moves the dragging element to the bottom
    if (nextEle && isAbove(nextEle, draggingEle)) {
        // The current order    -> The new order
        // draggingEle          -> nextEle
        // placeholder          -> placeholder
        // nextEle              -> draggingEle
        swap(nextEle, placeholder);
        swap(nextEle, draggingEle);
    }
};

const mouseUpHandler = function () {
    // Remove the placeholder
    placeholder && placeholder.parentNode.removeChild(placeholder);
    // Reset the flag
    isDraggingStarted = false;

    // Remove the position styles
    draggingEle.style.removeProperty('top');
    draggingEle.style.removeProperty('left');
    draggingEle.style.removeProperty('position');

    x = null;
    y = null;
    draggingEle = null;

    // Remove the handlers of `mousemove` and `mouseup`
    document.removeEventListener('mousemove', mouseMoveHandler);
    document.removeEventListener('mouseup', mouseUpHandler);
};

const isAbove = function (nodeA, nodeB) {
    // Get the bounding rectangle of nodes
    const rectA = nodeA.getBoundingClientRect();
    const rectB = nodeB.getBoundingClientRect();

    return rectA.top + rectA.height / 2 < rectB.top + rectB.height / 2;
    // return rectA.top < rectB.top;

};

const swap = function (nodeA, nodeB) {
    const parentA = nodeA.parentNode;
    const siblingA = nodeA.nextSibling === nodeB ? nodeA : nodeA.nextSibling;

    // Move `nodeA` to before the `nodeB`
    nodeB.parentNode.insertBefore(nodeA, nodeB);

    // Move `nodeB` to before the sibling of `nodeA`
    parentA.insertBefore(nodeB, siblingA);
    update_xaxis();
};

// Query the list element
const list = document.getElementById('game-choices');

// Query all items
[].slice.call(list.querySelectorAll('.draggable')).forEach(function (item) {
    item.addEventListener('mousedown', mouseDownHandler);
});
