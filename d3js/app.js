// set the dimensions and margins of the graph
const margin = { top: 10, right: 30, bottom: 40, left: 60 },
    width = 460 - margin.left - margin.right,
    height = 400 - margin.top - margin.bottom;

// Append the svg object to the div called "chart"
const svg = d3.select("#chart")
    .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform",
        "translate(" + margin.left + "," + margin.top + ")");

// Read the data
d3.csv("data/penglings.csv").then(function (data) {

    // Add X axis
    const x = d3.scaleLinear()
        .domain([170, 250])
        .range([0, width]);
    svg.append("g")
        .attr("transform", "translate(0," + height + ")")
        .call(d3.axisBottom(x));

    // Add Y axis
    const y = d3.scaleLinear()
        .domain([2500, 6500])
        .range([height, 0]);
    svg.append("g")
        .call(d3.axisLeft(y));

    // Color scale
    const color = d3.scaleOrdinal()
        .domain(["Adelie", "Chinstrap", "Gentoo"])
        .range(['#FF8C00', '#9932CC', '#008B8B']);

    // add gridlines
    svg.append('g')
        .attr('class', 'grid')
        .attr('transform', 'translate(0,' + height + ')')
        .call(d3.axisBottom(x)
            .tickSize(-height)
            .tickFormat(''))
        .selectAll('.tick line')
        .style('stroke', '#e9e9e9')
        .style('stroke-opacity', 0.7)
        .style('shape-rendering', 'crispEdges')
        .style('stroke-width', 1)
        .style('stroke-linecap', 'round')
        .style('stroke-linejoin', 'round')
        .style('stroke-miterlimit', 1)
        ;

    svg.append('g')
        .attr('class', 'grid')
        .call(d3.axisLeft(y)
            .tickSize(-width)
            .tickFormat(''))
            .selectAll('.tick line')
            .style('stroke', '#e9e9e9')
            .style('stroke-opacity', 0.7)
            .style('shape-rendering', 'crispEdges')
            .style('stroke-width', 1)
            .style('stroke-linecap', 'round')
            .style('stroke-linejoin', 'round')
            .style('stroke-miterlimit', 1);

    // Add dots
    svg.append('g')
        .selectAll("dot")
        .data(data)
        .enter()
        .append("circle")
        .attr("cx", function (d) { return x(d.flipper_length_mm); })
        .attr("cy", function (d) { return y(d.body_mass_g); })
        .attr("r", function (d) { return d.bill_length_mm / 6; })
        .style("fill", function (d) { return color(d.species); })
        .style("opacity", "0.8");

    // Add labels
    svg.append('text')
        .attr('text-anchor', 'end')
        .attr('x', width/2 + margin.left)
        .attr('y', height + margin.top + 25)
        .text('Flipper Length (mm)')
        .style('fill', 'black')
        .style('font-size', 10)
        .style('font-family', 'sans-serif');


    svg.append('text')
        .attr('text-anchor', 'end')
        .attr('transform', 'rotate(-90)')
        .attr('y', -margin.left + 20)
        .attr('x', -margin.top - height/2 + 20)
        .text('Body Mass (g)')
        .style('fill', 'black')
        .style('font-size', 10)
        .style('font-family', 'sans-serif');

    // Legend for species colors
    const species = ["Adelie", "Chinstrap", "Gentoo"];

    // Create a legend container
    const legend = svg.append("g")
        .attr("font-family", "sans-serif")
        .attr("font-size", 10)
        .attr("text-anchor", "end")
        .selectAll("g")
        .data(species)
        .enter().append("g")
            .attr("transform", function(d, i) { return "translate(0," + i * 20 + ")"; });

    // Draw legend colored circles
    legend.append("circle")
        .attr("cx", width - 10)
        .attr("cy", 10)
        .attr("r", 5)
        .attr("fill", color);
  
    // Draw legend text
    legend.append("text")
        .attr("x", width - 20)
        .attr("y", 10)
        .attr("dy", "0.32em")
        .text(function(d) { return d; });

    // Draw legend for size of bill length
    const size = d3.scaleSqrt()
        .domain([d3.min(data, d => d.bill_length_mm), d3.max(data, d => d.bill_length_mm)]) // Assuming bill_length_mm is your size metric
        .range([4, 10]); // Change these values based on your desired min and max circle sizes in the plot

    // Representative sizes and their labels (customize as needed)
    const sizeValues = [40, 50, 60]; // Example bill lengths
    const sizeLabels = ["40mm", "50mm", "60mm"]; // Customize labels as needed

    // Create a size legend container
    const sizeLegend = svg.append("g")
        .attr("transform", `translate(${width - 60}, 300)`); // Adjust for positioning

    // Add circles for size legend
    sizeValues.forEach((val, i) => {
    sizeLegend.append("circle")
        .attr("cx", 0)
        .attr("cy", i * 20) // Space out circles vertically
        .attr("r", size(val)) // Use size scale to determine radius
        .style("fill", "none")
        .style("stroke", "black");
    
    // Add labels
    sizeLegend.append("text")
        .attr("x", 20) // Position text to the right of circles
        .attr("y", i * 20)
        .attr("dy", "0.32em") // Center text vertically with circles
        .text(sizeLabels[i])
        .style("fill", "black")
        .style("font-size", 10)
        .style("font-family", "sans-serif");
    });
});
