// Example dataset
const data = [
  { flipper_length_mm: 181, body_mass_g: 3750, species: 'Adelie' },
  { flipper_length_mm: 186, body_mass_g: 3800, species: 'Gentoo' },
  // Add more data points here
];

// Set the dimensions and margins of the graph
const margin = {top: 10, right: 30, bottom: 30, left: 60},
    width = 800 - margin.left - margin.right,
    height = 600 - margin.top - margin.bottom;

// Append the svg object to the body of the page
const svg = d3.select("svg")
  .attr("width", width + margin.left + margin.right)
  .attr("height", height + margin.top + margin.bottom)
  .append("g")
  .attr("transform", `translate(${margin.left},${margin.top})`);

// Add X axis
const x = d3.scaleLinear()
  .domain([170, 230]) // Define the range of flipper lengths here
  .range([ 0, width ]);
svg.append("g")
  .attr("transform", `translate(0,${height})`)
  .call(d3.axisBottom(x));

// Add Y axis
const y = d3.scaleLinear()
  .domain([3000, 6000]) // Define the range of body mass here
  .range([ height, 0]);
svg.append("g")
  .call(d3.axisLeft(y));

// Add dots
svg.append('g')
  .selectAll("dot")
  .data(data)
  .join("circle")
    .attr("cx", d => x(d.flipper_length_mm))
    .attr("cy", d => y(d.body_mass_g))
    .attr("r", 5) // Radius of the dots; you can map another variable to the size if needed
    .attr("fill", d => {
      // Map the species to a color
      if (d.species === 'Adelie') {
        return "orange";
      } else if (d.species === 'Gentoo') {
        return "blue";
      } else if (d.species === 'Chinstrap') {
        return "purple";
      }
    });
