// set the dimensions and margins of the graph
const margin = {top: 70, right: 30, bottom: 70, left: 150},
    width = 850 - margin.left - margin.right,
    height = 600 - margin.top - margin.bottom;

// append the svg object to the body of the page
const svg = d3.select("#scatter")
  .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform",
          `translate(${margin.left}, ${margin.top})`);

// Append a rect element to have the plot background
svg.append("rect")
    .attr("width", width) // Use the width and height without margins
    .attr("height", height)
    .attr("fill", "#f0f0f0");

//Read the data
d3.csv("/penglings.csv").then( function(data) {
// Filter out rows with 'NA' in any column
    const data_ = data.filter(function(row) {
        // Check for 'NA'
         return row.flipper_length_mm !== 'NA' &&
               row.body_mass_g !== 'NA' &&
               row.bill_length_mm !== 'NA' &&
               row.species !== 'NA';
    });


  // Define X axis
  const x = d3.scaleLinear()
    .domain([170, 235])
    .range([ 0, width ]);

  // Define Y axis
  const y = d3.scaleLinear()
    .domain([2500, 6500])
    .range([ height, 0]);
var xAxis = d3.axisBottom(x).ticks(7);
var yAxis = d3.axisLeft(y).ticks(10);
//Add a grid
   var yAxisGrid = d3.axisLeft(y)
    .tickSize(-width) // width is the width of the plot area
    .tickFormat('') // No tick labels
    .ticks(10); //

   var xAxisGrid = d3.axisBottom(x)
    .tickSize(-height) // height is the height of the plot area
    .tickFormat('') // No tick labels
    .ticks(10); //

// For horizontal grid lines
svg.append('g')
    .attr('class', 'y grid')
    .call(yAxisGrid)
    .selectAll("line")
    .style("stroke", "white"); // Set your desired color here

// For vertical grid lines
svg.append('g')
    .attr('class', 'x grid')
    .attr('transform', `translate(0,${height})`)
    .call(xAxisGrid)
    .selectAll("line")
    .style("stroke", "white"); // Set your desired color here

  // Color
  const color = d3.scaleOrdinal()
    .domain(["Adelie", "Gentoo", "Chinstrap" ])
    .range([ "#1b9e77", "#d95f02", "#7570b3"])

// Add Y-Axis and hide the axis line
svg.append("g")
    .attr("class", "y axis")
    .call(yAxis)
    .selectAll(".tick text")
    .style("font-size", "14px");
// Add the X-Axis
svg.append("g")
    .attr("class", "x axis")
    .attr("transform", `translate(0,${height})`)
    .call(xAxis)
    .selectAll(".tick text")
    .style("font-size", "14px");

//I personally don't like showing the first tick label, so I hide
svg.select(".x.axis").selectAll(".tick text")
  .filter(function(d, i) { return i === 0; }) // Select the first tick label based on its index
  .style("display", "none");
svg.select(".y.axis").selectAll(".tick text")
  .filter(function(d, i) { return i === 0; }) // Select the first tick label based on its index
  .style("display", "none");

  //Radius
  const r = d3.scaleLinear()
  .domain([32,60])
  .range([3, 13]);


  // Highlight the specie that is hovered
  const highlight = function(event,d){

    selected_specie = d.species

    d3.selectAll(".dot")
      .transition()
      .duration(200)
      .style("fill", "lightgrey")
      .attr("r", 3)

    d3.selectAll("." + selected_specie)
      .transition()
      .duration(200)
      .style("fill", color(selected_specie))
      .attr("r", function (d) { return r(d.bill_length_mm); } )
  }
var tooltip = d3.select("#scatter")
  .append("div")
  .attr("class", "tooltip")
  .style("opacity", 0)
  .style("position", "absolute")
  .style("background-color", "white")
  .style("border", "solid")
  .style("border-width", "2px")
  .style("border-radius", "5px")
  .style("padding", "5px")
  .style("pointer-events", "none"); // Ensure the tooltip doesn't interfere with mouse events

  // Highlight the specie that is hovered
  const doNotHighlight = function(event,d){
    d3.selectAll(".dot")
      .transition()
      .duration(200)
      .style("fill", d => color(d.species))
      .attr("r", function (d) { return r(d.bill_length_mm); } )
  }


  // Add dots
  svg.append('g')
    .selectAll("dot")
    .data(data_)
    .enter()
    .append("circle")
      .attr("class", function (d) { return "dot " + d.species } )
      .attr("cx", function (d) { return x(d.flipper_length_mm); } )
      .attr("cy", function (d) { return y(d.body_mass_g); } )
      .attr("r", function (d) { return r(d.bill_length_mm); } )
      .style("fill", function (d) { return color(d.species) } )
      .style("opacity", 0.80) // Set the opacity of the circles
      .on("mouseover", function(event, d) {
      highlight(event, d);
      tooltip.transition()
        .duration(200)
        .style("opacity", 1);
      tooltip.html("Specie: " + d.species + "<br/>" +
                   "Flipper Length (mm): " + d.flipper_length_mm + "<br/>" +
                   "Body Mass (g): " + d.body_mass_g + "<br/>" +
                   "Bill Length (mm): " + d.bill_length_mm)
        .style("left", (event.pageX + 10) + "px")
        .style("top", (event.pageY + 10) + "px");
    })
    .on("mousemove", function(event, d) {
      tooltip.style("left", (event.pageX + 10) + "px")
             .style("top", (event.pageY + 10) + "px");
    })
    .on("mouseleave", function(event, d) {
      doNotHighlight(event, d);
      tooltip.transition()
        .duration(500)
        .style("opacity", 0);
    });

  // Style x axis
    svg.append("text")
    .attr("text-anchor", "center")
    .attr("x", (width/2)-70)
    .attr("y", height +50)
    .text("Flipper Length (mm)")
    .style("font-size", "18px")
    .style("font-weight", "bold");

  // Style y axis
  svg.append("text")
    .attr("text-anchor", "end")
    .attr("transform", "rotate(-90)")
    .attr("y", -70)
    .attr("x", -(height/2)+50)
    .text("Body Mass (g)")
    .style("font-size", "18px")
    .style("font-weight", "bold");

// Add Title
  svg.append("text")
    .attr("x", width / 2)
    .attr("y", 0 - (margin.top / 2))
    .attr("text-anchor", "middle")
    .style("font-size", "24px")
    .style("font-weight", "bold")
    .style("fill", "#040404") // Ensure the title is visible on your background
    .text("Assignment 3 - Scatter Plot with d3");

//Add legends
svg.append("rect")
    .attr('x', 65)
    .attr('y', 10)
    .attr("width", 100) // Use the width and height without margins
    .attr("height", 80)
    .attr('stroke', 'black')
    .attr("fill", "#f7f7f7");
// Handmade legend
svg.append("circle").attr("cx",80).attr("cy",20).attr("r", 6).style("fill", "#1b9e77")
svg.append("circle").attr("cx",80).attr("cy",50).attr("r", 6).style("fill", "#7570b3")
svg.append("circle").attr("cx",80).attr("cy",80).attr("r", 6).style("fill", "#d95f02")
svg.append("text").attr("x", 100).attr("y", 20).text("Adelie").style("font-size", "15px").attr("alignment-baseline","middle")
svg.append("text").attr("x", 100).attr("y", 50).text("Chinstrap").style("font-size", "15px").attr("alignment-baseline","middle")
svg.append("text").attr("x", 100).attr("y", 80).text("Gentoo").style("font-size", "15px").attr("alignment-baseline","middle")


})

