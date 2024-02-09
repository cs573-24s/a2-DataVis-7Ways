// Load CSV data
d3.csv("penglings.csv").then(function(data) {
  // Convert string data to numbers
  data.forEach(function(d) {
    d.flipper_length_mm = +d.flipper_length_mm; // Convert flipper_length_mm to number
    d.body_mass_g = +d.body_mass_g; // Convert body_mass_g to number
  });

  // Define Vega-Lite specification with legend
  const spec = {
    "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
    "title": "Penguin Flipper Length vs Body Mass",
    "description": "A scatter plot with color encoding based on species",
    "width": 800, // Adjust width as desired
    "height": 600, // Adjust height as desired
    "data": {
      "values": data // Use the loaded CSV data here
    },
    "mark": {
      "type": "circle",
      "shape": "circle",
      "size": 300, // Set the size of the circles
      "update": {"enter": {"opacity": {"value": 1}, "duration": 2000}} // Add animation for entering points
    },
    "encoding": {
      "x": {
        "field": "flipper_length_mm",
        "type": "quantitative",
        "scale": {"zero": false} // Start x-axis from 170
      },
      "y": {"field": "body_mass_g", "type": "quantitative"},
      "color": {
        "field": "species",
        "type": "nominal",
        "scale": {"range": ["#19282F", "#CD1818", "#2ca02c"]} // Custom color scheme
      }
    },
    "legend": {"title": "Species"} // Add legend with title
  };

  // Render the visualization using Vega-Embed
  vegaEmbed("#vis", spec);
}).catch(function(error) {
  // Handle any errors that occur during data loading
  console.error("Error loading data:", error);
});
