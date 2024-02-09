let table; // Variable to store the loaded CSV data
let data = []; // Array to store the parsed data
let colors = {}; // Object to store colors for each species
let xOffset = 100; // Offset for moving the graph to the right

function preload() {
    // Load the CSV file
    table = loadTable('penglings.csv', 'csv', 'header');
}

function setup() {
    createCanvas(800, 600); // Create a canvas
    processData(); // Process the loaded data
}

function processData() {
    // Define colors for each species
    colors = {
        'Adelie': color("black"), // Red
        'Chinstrap': color("Red"), // Green
        'Gentoo': color("Green") // Blue
    };

    // Loop through each row in the CSV table
    for (let i = 0; i < table.getRowCount(); i++) {
        // Get the values from the current row as strings
        let flipper_length_mm_str = table.getString(i, 'flipper_length_mm');
        let body_mass_g_str = table.getString(i, 'body_mass_g');
        let species = table.getString(i, 'species');

        // Convert the strings to numbers
        let flipper_length_mm = parseFloat(flipper_length_mm_str);
        let body_mass_g = parseFloat(body_mass_g_str);

        // Add the data to the array
        data.push({ x: flipper_length_mm, y: body_mass_g, species: species });
    }

    // Draw scatter plot
    drawScatterPlot();
    drawAxes();
    drawLegend();
    drawTitle();
}

function drawScatterPlot() {
    background(255); // Set background to white

    // Plot data points
    for (let i = 0; i < data.length; i++) {
        let x = map(data[i].x, 170, 240, xOffset + 50, width - 50 + xOffset); // Map flipper_length_mm to canvas width
        let y = map(data[i].y, 2700, 6300, height - 50, 50); // Map body_mass_g to canvas height
        let col = colors[data[i].species]; // Get color based on species
        fill(red(col), green(col), blue(col), 204); // Set fill color with opacity (204 = 80% opacity)
        noStroke(); // Disable stroke
        ellipse(x, y, 18, 18); // Draw circle for each data point
    }
}

function drawAxes() {
    // Draw x-axis
    stroke(0); // Set stroke color to black
    line(xOffset + 50, height - 50, width - 50 + xOffset, height - 50); // Draw x-axis line
    let startX = 170;
    let endX = 240;
    let stepX = 10;
    for (let x = startX; x <= endX; x += stepX) {
        let xPos = map(x, startX, endX, xOffset + 50, width - 50 + xOffset);
        line(xPos, height - 45, xPos, height - 55); // Draw tick mark
        textAlign(CENTER);
        textSize(10);
        text(x, xPos, height - 30); // Display label
    }
    textAlign(CENTER);
    textSize(12);
    text('flipper_length_mm', (width + xOffset) / 2, height - 10); // X-axis label

    // Draw y-axis
    line(xOffset + 50, 50, xOffset + 50, height - 50); // Draw y-axis line
    let startY = 2700;
    let endY = 6300;
    let stepY = 500;
    for (let y = startY; y <= endY; y += stepY) {
        let yPos = map(y, startY, endY, height - 50, 50);
        line(xOffset + 45, yPos, xOffset + 55, yPos); // Draw tick mark
        textAlign(RIGHT);
        textSize(10);
        text(y, xOffset + 40, yPos); // Display label
    }
    textAlign(RIGHT);
    textSize(12);
    push(); // Save the current drawing state
    translate(xOffset / 2, height / 2); // Translate to the center of the left margin
    rotate(HALF_PI); // Rotate by 90 degrees
    text('body_mass_g', 0, 0); // Y-axis label
    pop(); // Restore the saved drawing state
}

function drawLegend() {
    // Draw legend
    let legendX = 220; // Adjusted position of the legend
    let legendY = 50;
    let legendSize = 20;
    let spacing = 30;
    let legendTitle = "Species";
    textSize(12);
    textAlign(LEFT, TOP);
    text(legendTitle, legendX, legendY);
    for (let species in colors) {
        fill(colors[species]);
        rect(legendX, legendY + spacing, legendSize, legendSize);
        fill(0);
        text(species, legendX + legendSize + 10, legendY + spacing);
        spacing += 30;
    }
}

function drawTitle() {
    // Draw title
    textSize(16);
    textAlign(CENTER, CENTER);
    let title = "Penguin Flipper Length vs Body Mass";
    text(title, width / 2, 20);
}
