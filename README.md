# 02-DataVis-7ways

Assignment 2 - Data Visualization, 7 Ways  
==========================================================================================================================================
# (1) DataWrapper Visualization : Live Demo [Here](https://www.datawrapper.de/_/ILbG9/) ||
==========================================================================================
![](img/step2.png)

Datawrapper is an online data visualization tool that allows users to create interactive and customizable charts, maps, and tables from their data. It provides a user-friendly interface where users can easily upload their datasets or connect to external data sources such as Google Sheets, Excel files, or SQL databases.

Key features of Datawrapper include:

1. **Simple Interface**: Datawrapper offers an intuitive and easy-to-use interface that doesn't require any coding skills. Users can quickly create visualizations by uploading their data and customizing the appearance of the charts.
![](img/step2.png)
2. **Wide Range of Visualization Types**: Datawrapper supports various types of visualizations, including line charts, bar charts, scatter plots, choropleth maps, and more. Users can choose the most suitable visualization type for their data and customize it according to their needs.
![](img/step1.png)
3. **Customization Options**: Users can customize various aspects of their visualizations, such as colors, fonts, labels, axes, tooltips, and legends. Datawrapper provides a range of customization options to help users create visually appealing and informative charts.
![](img/step3.png) ![](img/step4.png)
4. **Responsive and Interactive**: The visualizations created with Datawrapper are responsive and can be embedded in websites, blogs, or online articles. They are also interactive, allowing viewers to hover over data points for more information or interact with the charts using filters or zooming functionality.
![](img/step5.png)

==========================================================================================================================================
# (2) D3+Js ||
==============
![](img/step5.png)

This HTML file incorporates D3.js to create a scatter plot visualization of penguin data. Let's break down the code and understand its functions and uses:

1. **Importing D3.js Library**:
   - The script tag imports the D3.js library from an external source (`https://d3js.org/d3.v7.min.js`).

2. **Styling**:
   - CSS styles define the appearance of the tooltip, which will display additional information when hovering over data points.

3. **Body**:
   - The body contains an SVG element (`#scatter-plot`) where the scatter plot will be drawn and a `div` element (`#tooltip`) for the tooltip.

4. **Script**:
   - The script section loads data from a CSV file (`penglings.csv`) using `d3.csv()` function.
   - The data is then parsed, converting certain columns to numeric values using `+d`.

5. **Graph Dimensions and Margins**:
   - Margins and dimensions for the graph are defined.

6. **Color Scale**:
   - A color scale is created using `d3.scaleOrdinal()` to assign different colors to different species.

7. **SVG Elements**:
   - The SVG element is appended to the `#scatter-plot` with appropriate width, height, and margin settings.

8. **Scales**:
   - Linear scales (`xScale`, `yScale`) are defined for x and y axes mapping data to pixel coordinates.

9. **Axes**:
   - x and y axes are created using `d3.axisBottom()` and `d3.axisLeft()` respectively.
   - Axis labels and formatting are also specified.

10. **Legend**:
    - A legend is added to the graph to denote different species, with corresponding colors.

11. **Scatter Points**:
    - Circles representing data points are appended to the SVG.
    - Circle positions (`cx`, `cy`) are determined by the data values and mapped using the scales.
    - Circle radii (`r`) are determined by another scale (`sizeScale`), mapped from bill length.
    - Circle colors (`fill`) are determined by the species and mapped using the color scale.
    - Tooltip events are added to display additional information (`species`, `flipper_length_mm`, `body_mass_g`) when hovering over data points.
    - On mouseover, the circle radius is increased, and the tooltip is displayed. On mouseout, the circle radius is reset, and the tooltip disappears.

12. **Error Handling**:
    - Error handling is done using `.catch()` method to log any errors to the console.
==========================================================================================================================================
# (3,4,5) Visualization using Python||
======================================

*Python + Altair:

This Python code creates scatter plots using Altair library to visualize the relationship between bill length and bill depth of penguins from a given dataset. Let's break down each function and its role within Altair:

1. `alt.Chart`: This function initializes the creation of a new chart. It specifies the dataset to be visualized and provides a means for encoding data attributes onto visual properties such as position, color, and size.

2. `mark_circle`: This function specifies the type of mark (or glyph) to be used in the chart. In this case, it indicates that circles should be used for each data point in the scatter plot.

3. `encode`: This function is used to map data attributes to visual properties of the chart such as x-axis, y-axis, color, size, etc. It specifies how the data should be represented visually. For example, `x='bill_length_mm'` maps the 'bill_length_mm' column from the DataFrame to the x-axis of the chart.

4. `color`: This encoding function is used to set the color of data points based on a specific data attribute. It utilizes the color scale provided to map different categories or values to different colors.

5. `tooltip`: This encoding function determines what information should be displayed when hovering over a data point. It specifies which columns from the DataFrame should be shown as tooltips.

6. `properties`: This function sets various properties of the chart such as width, height, and title.

7. `interactive`: This function enables interactivity in the chart, allowing users to interact with and explore the data.

Now, let's look at the specific charts created in the code:

- **Chart 1**: This chart visualizes the relationship between bill length and bill depth for Adelie and Gentoo penguins.
  
- **Chart 2**: This chart visualizes the relationship between bill length and bill depth for Adelie and Chinstrap penguins.
  
- **Chart 3**: This chart visualizes the relationship between bill length and bill depth for Gentoo and Chinstrap penguins.
  
- **Chart 4**: This chart visualizes the relationship between bill length and bill depth for all three species combined.

Finally, the code combines these charts into a grid layout using the `&` operator and saves the combined plot as an HTML file named 'scatterplots.html' using the `.save()` method.


- R + ggplot2 `<- definitely worth trying`
- Excel


- Altair `<- hugely popular python library. highly recommended `

- Tableau
- PowerBI
- Vega-lite <- `<- very interesting formal visualization model; might be the future of the field`
- Flourish <- `<- popular in recent years`
- GNUplot `<- the former CS department head uses this all the time :)`
- SAS/SPSS/Matlab


