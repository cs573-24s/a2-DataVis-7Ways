
var margin = { top: 20, right: 25, bottom: 60, left: 200 },
    width = 800 - margin.left - margin.right,
    height = 600 - margin.top - margin.bottom;

var svg = d3.select("#my_dataviz")
    .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

// Read the data
d3.csv("penglings.csv", function (d) { 

    return {
        flipper_length_mm: +d.flipper_length_mm,
        body_mass_g: +d.body_mass_g,
        bill_length_mm: +d.bill_length_mm,
        species: d.species
    };

}).then(function (data) {

    // Add X axis
    var x = d3.scaleLinear()
        .domain([d3.min(data, function (d) { return d.flipper_length_mm; }), d3.max(data, function (d) { return d.flipper_length_mm; })])
        .range([0, width]);
    svg.append("g")
        .attr("transform", "translate(0," + height + ")")
        .call(d3.axisBottom(x));


    // Add X axis label
    svg.append("text")
        .attr("transform", "translate(" + (width / 2) + " ," + (height + margin.top + 20) + ")")
        .style("text-anchor", "middle")
        .text("Flipper Length (mm)");

    // Add Y axis label
    svg.append("text")
        .attr("transform", "rotate(-90)")
        .attr("y", 0 - margin.left)
        .attr("x", 0 - (height / 8))
        .attr("dy", "1em")
        .style("text-anchor", "middle")
        .text("Body Mass (g)");

    // Add Y axis
    var y = d3.scaleLinear()
        .domain([d3.min(data, function (d) { return d.body_mass_g; }), d3.max(data, function (d) { return d.body_mass_g; })])
        .range([height, 0]);
    svg.append("g")
        .call(d3.axisLeft(y));


    //color scales
    var color = d3.scaleOrdinal()
        .domain(["Adelie", "Chinstrap", "Gentoo"]) 
        .range(["orange", "purple", "green"]); 

    // Add dots
    svg.selectAll("dot")
        .data(data)
        .enter().append("circle")
        .attr("cx", function (d) { return x(d.flipper_length_mm); })
        .attr("cy", function (d) { return y(d.body_mass_g); })
        .attr("r", function (d) {
      
            return Math.sqrt(d.body_mass_g) / 8; 
        })
        .style("fill", function (d) { return color(d.species); })
        .style("opacity", 0.8); 

});