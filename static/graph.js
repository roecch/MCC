let games = ['AR', 'BB', 'BM', 'GR', 'HITW', 'MD', 'PT', 'SOT', 'SB', 'SG', 'TGTTOS', 'RSR']

//let teamsJson = "[
//        + "{'color':'red', 'players':['Purpled','CaptainPuffy','WilburSoot','Ranboo']},"
//        + "{'color':'orange', 'players':['HBomb94','Tubbo','TommyInnit', 'JackManifold']},"
//        + "{'color':'yellow', 'players':['Dream','BadBoyHalo','Skeppy','GeorgeNotFound']},"
//        + "{'color':'lime', 'players':['Krtzyy','Shubble','Smajor','Seapeekay']},"
//        + "{'color':'green', 'players':['5up','TapL','TheOrionSound','GeminiTay']},"
//        + "{'color':'cyan', 'players':['Hannahxxrose','jojosolos','Aimsey','PearlescentMoon']},"
//        + "{'color':'aqua', 'players':['Fruitberries','Smallishbeans','Cubfan','GoodTimesWithScar']},"
//        + "{'color':'blue', 'players':['Sapnap','Sylvee','FoolishGames','GeeNelly']},"
//        + "{'color':'purple', 'players':['Illumina','RyguyRocky','Michealmcchill','Krinios']},"
//        + "{'color':'pink', 'players':['Philza','InTheLittleWood','CaptainSparklez','AntVenom']},"
//       ]";

let testTeamsJson = [
    {"color": "red", 'game': 'AR', 'pts': 10},
    {"color": "red", 'game': 'BB', 'pts': 20},
    {"color": "red", 'game': 'BM', 'pts': 30},
    {"color": "red", 'game': 'GR', 'pts': 40},
    {"color": "red", 'game': 'HITW', 'pts': 50},
    {"color": "red", 'game': 'PT', 'pts': 60},
    {"color": "red", 'game': 'SOT', 'pts': 70},
    {"color": "red", 'game': 'SG', 'pts': 80},
    {"color": "orange", 'game': 'AR', 'pts': 20},
    {"color": "orange", 'game': 'BB', 'pts': 30},
    {"color": "orange", 'game': 'BM', 'pts': 40},
    {"color": "orange", 'game': 'GR', 'pts': 50},
    {"color": "orange", 'game': 'HITW', 'pts': 60},
    {"color": "orange", 'game': 'PT', 'pts': 70},
    {"color": "orange", 'game': 'SOT', 'pts': 80},
    {"color": "orange", 'game': 'SG', 'pts': 10},
    {"color": "yellow", 'game': 'AR', 'pts': 30},
    {"color": "yellow", 'game': 'BB', 'pts': 40},
    {"color": "yellow", 'game': 'BM', 'pts': 50},
    {"color": "yellow", 'game': 'GR', 'pts': 60},
    {"color": "yellow", 'game': 'HITW', 'pts': 70},
    {"color": "yellow", 'game': 'PT', 'pts': 80},
    {"color": "yellow", 'game': 'SOT', 'pts': 10},
    {"color": "yellow", 'game': 'SG', 'pts': 20},
    {"color": "lime", 'game': 'AR', 'pts': 40},
    {"color": "lime", 'game': 'BB', 'pts': 50},
    {"color": "lime", 'game': 'BM', 'pts': 60},
    {"color": "lime", 'game': 'GR', 'pts': 70},
    {"color": "lime", 'game': 'HITW', 'pts': 80},
    {"color": "lime", 'game': 'PT', 'pts': 10},
    {"color": "lime", 'game': 'SOT', 'pts': 20},
    {"color": "lime", 'game': 'SG', 'pts': 30},
    {"color": "green", 'game': 'AR', 'pts': 50},
    {"color": "green", 'game': 'BB', 'pts': 60},
    {"color": "green", 'game': 'BM', 'pts': 70},
    {"color": "green", 'game': 'GR', 'pts': 80},
    {"color": "green", 'game': 'HITW', 'pts': 10},
    {"color": "green", 'game': 'PT', 'pts': 20},
    {"color": "green", 'game': 'SOT', 'pts': 30},
    {"color": "green", 'game': 'SG', 'pts': 40},
    {"color": "cyan", 'game': 'AR', 'pts': 60},
    {"color": "cyan", 'game': 'BB', 'pts': 70},
    {"color": "cyan", 'game': 'BM', 'pts': 80},
    {"color": "cyan", 'game': 'GR', 'pts': 90},
    {"color": "cyan", 'game': 'HITW', 'pts': 10},
    {"color": "cyan", 'game': 'PT', 'pts': 20},
    {"color": "cyan", 'game': 'SOT', 'pts': 30},
    {"color": "cyan", 'game': 'SG', 'pts': 40},
    {"color": "aqua", 'game': 'AR', 'pts': 53},
    {"color": "aqua", 'game': 'BB', 'pts': 78},
    {"color": "aqua", 'game': 'BM', 'pts': 45},
    {"color": "aqua", 'game': 'GR', 'pts': 45},
    {"color": "aqua", 'game': 'HITW', 'pts': 86},
    {"color": "aqua", 'game': 'PT', 'pts': 13},
    {"color": "aqua", 'game': 'SOT', 'pts': 87},
    {"color": "aqua", 'game': 'SG', 'pts': 56},
    {"color": "blue", 'game': 'AR', 'pts': 95},
    {"color": "blue", 'game': 'BB', 'pts': 34},
    {"color": "blue", 'game': 'BM', 'pts': 78},
    {"color": "blue", 'game': 'GR', 'pts': 98},
    {"color": "blue", 'game': 'HITW', 'pts': 12},
    {"color": "blue", 'game': 'PT', 'pts': 64},
    {"color": "blue", 'game': 'SOT', 'pts': 78},
    {"color": "blue", 'game': 'SG', 'pts': 64},
    {"color": "purple", 'game': 'AR', 'pts': 45},
    {"color": "purple", 'game': 'BB', 'pts': 36},
    {"color": "purple", 'game': 'BM', 'pts': 61},
    {"color": "purple", 'game': 'GR', 'pts': 86},
    {"color": "purple", 'game': 'HITW', 'pts': 15},
    {"color": "purple", 'game': 'PT', 'pts': 52},
    {"color": "purple", 'game': 'SOT', 'pts': 53},
    {"color": "purple", 'game': 'SG', 'pts': 69},
    {"color": "pink", 'game': 'AR', 'pts': 35},
    {"color": "pink", 'game': 'BB', 'pts': 57},
    {"color": "pink", 'game': 'BM', 'pts': 42},
    {"color": "pink", 'game': 'GR', 'pts': 95},
    {"color": "pink", 'game': 'HITW', 'pts': 64},
    {"color": "pink", 'game': 'PT', 'pts': 98},
    {"color": "pink", 'game': 'SOT', 'pts': 36},
    {"color": "pink", 'game': 'SG', 'pts': 97}
];

window.onload = () => {
    make_graph(['AR', 'BB', 'BM', 'GR', 'HITW', 'PT', 'SOT', 'SG'],)
};

function make_graph(eight_games) {
    let margin = {top: 20, right: 20, bottom: 30, left: 50},
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


    // Add X axis
    var x = d3.scaleBand()
        .domain(eight_games)
        .range([0, width]);
    var xAxis = svg.append("g")
        .attr("class", "x axis")
        .attr("transform", "translate(30," + height + ")")
        .call(d3.axisBottom(x));

    // Add Y axis
    var y = d3.scaleLinear()
        .domain([0, 1000])
        .range([height, 0]);
    var yAxis = svg.append("g")
        .attr("class", "y axis")
        .attr("transform", "translate(30,0)")
        .call(d3.axisLeft(y));

    var sumstat = d3.group(testTeamsJson, d => d.color)

    // color palette
    var res = testTeamsJson.map(function (d) {
        return d.color
    }) // list of group names
    console.log(res)
    var color = d3.scaleOrdinal()
        .domain(res)
        .range(['#FF0000', '#FFA500', '#FFFF00', '#00FF55', '#32CD32', '#00FFFF', '#008B8B', '#0000FF', '#AA00FF', '#FF69B4'])


    // Draw the line
    let lines = svg.selectAll(".line")
        .data(sumstat)
        .enter()
        .append("path")
        .attr("fill", "none")
        .attr("stroke", function (d) {
            return color(d[0])
        })
        .attr("stroke-width", 1.5)
        .attr("transform", "translate(" + (30 + (x.bandwidth() / 2)) + ",0)")
        .attr("d", function (d) {
            console.log(d);
            let p = 0
            return d3.line()
                .x(function (d) {
                    return x(d.game);
                })
                .y(function (d) {
                    p += d.pts;
                    return y(p);
                })
                (d[1])
        })
        .on("mouseover", hoverLine)
        .on("mousemove", hoverLine)
        .on("mouseout", function (event,d) {
            d3.select(this).attr("stroke", function (d) {
                return color(d[0]);
            })
            tooltip.style("visibility", "hidden");
        });


    //create tooltip
    let tooltip = d3.select("#vis-svg")
        .append("div")
        .attr('class', 'tooltip')
        .style("position", "absolute")
        .style("z-index", "10")
        .style("visibility", "hidden")

    //hover for line chart
    function hoverLine(event,d) {
        d3.select(this)

        // let coords = d3.pointer(event, svg)
        // let invertX = x.invert(coords[0] - margin.left - 19)
        // let invertY = height - (y.invert(coords[1] - 60) * -1)
        // //Update Tooltip Position & value
        // tooltip
        //     .style('top', coords[1] + 'px')
        //     .style('left', coords[0] + 'px')
        //     .text(d[0] + "\n" + invertX + "\n" + invertY)
        //     .style("visibility", "visible")

    }
}