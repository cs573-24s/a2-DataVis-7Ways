# 02-DataVis-7ways

Assignment 2 - Data Visualization, 7 Ways  
===

# D3 + JavaScript Visualization

- **D3:** Offers high flexibility, allowing developers to create custom and intricate visualizations tailored to specific needs. **JavaScript:** Being a general-purpose language, JavaScript provides flexibility and versatility in handling various aspects of web development and visualization.

- In this visualization, I used D3, a powerful JavaScript library for creating dynamic and interactive data visualizations. The goal was to replicate a scatterplot.

- I started by loading the penguins dataset and defining the necessary scales for the x-axis (Flipper Length) and y-axis (Body Mass). Additionally, we employed a color scale for mapping penguin species and a size scale for the circle radius based on Bill Length.

- I utilized D3's data binding and enter-update-exit pattern to create circles representing each penguin observation. The positions on the x and y axes were determined by Flipper Length and Body Mass, respectively. Circle colors were mapped to penguin species, and the circle sizes were determined by Bill Length

- I added x and y axes to provide context to the scatterplot. Axis labels for "Flipper Length (mm)" and "Body Mass (g)" were included to guide the viewer.

- This D3 + JavaScript visualization closely achieves the functionality, allowing for interactive exploration of the penguins dataset.

![alt text](<01 JS + D3/D3.jpg>)


# Python + Plotly Visualization

- **Python + Plotly** is a powerful combination for interactive and visually appealing data visualization. Plotly is a Python graphing library that enables the creation of various types of plots, charts, and dashboards. It provides a high-level interface for creating complex visualizations with ease. 

- Plotly allows the creation of interactive plots, which can be explored and manipulated by end-users. Zoom, pan, hover, and click functionalities enhance the interactivity.
 
 [text](<02 Python + Plotly/Plotly.py>)


# Python + Altair Visualization

- **Python + Altair** 
- 



## Technical Achievements
### JS + D3
- **D3.js Integration**: The combination of D3 and JavaScript library are powerful for data visualization. D3.js allows for dynamic and interactive data-driven visualizations.
- **SVG**: The use of SVG elements for creating the scatterplot provides a scalable and resolution-independent graphical representation.
- **Data Binding and Data Visualization**: The code efficiently binds data from the provided CSV file (d3.csv("penglings.csv").then(data => {...}) and maps it to visual elements like circles, axes, and legends, enabling effective data visualization.
- **Scales and Axes**: Scales (e.g., xScale and yScale) and axes (e.g., d3.axisBottom and d3.axisLeft) are implemented to properly position and scale the data on the scatterplot.
- **Dynamic Tooltip Interaction**: The inclusion of a dynamic tooltip (const tooltip = d3.select("#scatterplot").append("div").attr("class", "tooltip");) enhances user interaction by providing detailed information on mouseover events.

### Python + Plotly
- **Feature Normalization**: Applied normalization to the bill_length_mm column, ensuring that data falls within a consistent range. Used the min-max normalization technique to standardize the values.
- **Scaled Sizes Calculation**: ntroduced a scaled_sizes column based on the normalized bill_length_mm, allowing for more meaningful size representations. Adjusted the scaling factor to enhance the visual impact of the scatter plot.

### Python + Altair 
- **SVG**: 
- **SVG**: 
- **SVG**: 





### Design Achievements
### JS + D3
- **Responsive Design**: The layout of the scatterplot and legend is designed to be responsive (display: flex; flex-direction: row;) and adaptable to different screen sizes.
- **Color Mapping and Legend**: Species information is visually encoded through color mapping, and a legend is provided to enhance the interpretability of the chart.
- **Clear Typography**: Clear and readable typography is employed for axis labels, legend items, and tooltip content, contributing to the overall clarity of the visualization.
- **User Interaction**: The inclusion of mouseover and mouseout events for circles provides a user-friendly interaction by displaying additional information when hovering over data points.


### Python + Plotly
- **Labels and Axes**: learly labeled the x-axis and y-axis as "Flipper Length (mm)" and "Body Mass (g)," respectively, enhancing the interpretability of the scatter plot. Ensured proper titling for axes and legend for a more informative visualization.
- **Margin and Layout**: Adjusted margin settings (left, right, top, bottom) to optimize the layout and spacing of the plot Achieved a balanced and aesthetically pleasing design.

### Python + Altair 
- **SVG**: 
- **SVG**: 
- **SVG**: 
