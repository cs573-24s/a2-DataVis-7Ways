// Load CSV Data
d3.csv("penglings.csv").then(function(data) {

  // Parse numeric values as numbers
  data.forEach(function(d) {
    d.flipper_length_mm = +d.flipper_length_mm; // Convert from string to number
    d.body_mass_g = +d.body_mass_g; // Convert from string to number
  });

  // Define dimensions and margins of the graph
  const margin = {top: 70, right: 30, bottom: 100, left: 60},
        width = 800 - margin.left - margin.right,
        height = 600 - margin.top - margin.bottom;

  // Define array of colors
  const colors = ["black", "red", "green"]; // Define your own color array

  // Create color scale
  const colorScale = d3.scaleOrdinal()
    .domain(data.map(d => d.species))
    .range(colors);

  // Create SVG elements
  const svg = d3.select("#scatter-plot")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform", `translate(${margin.left},${margin.top})`);

  // Define scales
  const xScale = d3.scaleLinear()
    .domain([d3.min(data, d => d.flipper_length_mm), d3.max(data, d => d.flipper_length_mm)])
    .range([0, width]);

  const yScale = d3.scaleLinear()
    .domain([d3.min(data, d => d.body_mass_g), d3.max(data, d => d.body_mass_g)])
    .range([height, 0]);

  // Define axes
  const xAxis = d3.axisBottom(xScale);
  const yAxis = d3.axisLeft(yScale);

  // Add axes to the SVG
  const xAxisGroup = svg.append("g")
    .attr("transform", `translate(0, ${height})`)
    .call(xAxis);

  const yAxisGroup = svg.append("g")
    .call(yAxis);

  // Style x axis
  svg.append("text")
    .attr("text-anchor", "end")
    .attr("x", width)
    .attr("y", height + margin.top - 20)
    .text("Flipper Length (mm)");

  // Style y axis
  svg.append("text")
    .attr("text-anchor", "end")
    .attr("transform", "rotate(-90)")
    .attr("y", -margin.left + 20)
    .attr("x", -height / 2)
    .text("Body Mass (g)");

 // scatter points
const circles = svg.selectAll("circle")
.data(data)
.enter()
.append("circle")
.attr("cx", d => xScale(d.flipper_length_mm))
.attr("cy", d => yScale(d.body_mass_g))
.attr("r", 8) 
.style("fill", d => colorScale(d.species))
.style("stroke", "#ccc")
.style("stroke-width", "1px")
.style("opacity", 0.8);


 // Add legend
const legend = svg.selectAll(".legend")
.data(colorScale.domain())
.enter()
.append("g")
.attr("class", "legend")
.attr("transform", (d, i) => `translate(${width - 480}, ${margin.top / 2 + i * 20})`);

legend.append("rect")
.attr("x", 0)
.attr("width", 18)
.attr("height", 18)
.style("fill", colorScale);

legend.append("text")
.attr("x", -6)
.attr("y", 9)
.attr("dy", ".35em")
.style("text-anchor", "end")
.text(d => d);


 // Add tooltip
const tooltip = d3.select("body").append("div")
  .attr("class", "tooltip")
  .style("opacity", 0);

circles.on("mouseover", function(d) {
    tooltip.transition()
      .duration(200)
      .style("opacity", .9);
    tooltip.html(`Species: ${d.species}<br>Flipper Length: ${d.flipper_length_mm}<br>Body Mass: ${d.body_mass_g}`)
      .style("left", (d3.event.pageX + 5) + "px")
      .style("top", (d3.event.pageY - 5000) + "px");
  })
  .on("mouseout", function(d) {
    tooltip.transition()
      .duration(500)
      .style("opacity", 0);
  });


// Add mouseover and mouseout event listeners to circles
circles.on("mouseover", handleMouseOver)
  .on("mouseout", handleMouseOut);

// Tooltip hide logic
function handleMouseOut() {
  tooltip.transition()
    .duration(500)
    .style("opacity", 0);
}

// Tooltip mouseover event listener
function handleMouseOver(d) {
  tooltip.transition()
    .duration(200)
    .style("opacity", .9);
  tooltip.html(`Species: ${d.species}<br>Flipper Length: ${d.flipper_length_mm}<br>Body Mass: ${d.body_mass_g}`)
    .style("left", (d3.event.pageX + 5) + "px")
    .style("top", (d3.event.pageY - 5000) + "px");
}
// Add mouseover and mouseout event listeners to circles
circles.on("mouseover", function(d) {
  const species = d.species;
  const flipperLength = d.flipper_length_mm;
  const bodyMass = d.body_mass_g;

  tooltip.transition()
      .duration(200)
      .style("opacity", .9);
  tooltip.html(`Species: ${species}<br>Flipper Length: ${flipperLength}<br>Body Mass: ${bodyMass}`)
      .style("left", (d3.event.pageX + 5) + "px")
      .style("top", (d3.event.pageY - 28) + "px");
})
.on("mouseout", function(d) {
  tooltip.transition()
      .duration(500)
      .style("opacity", 0);
});



}).catch(function(error){
    console.log(error);
});
