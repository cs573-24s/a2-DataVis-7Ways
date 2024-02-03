# 02-DataVis-7ways

Assignment 2 - Data Visualization, 7 Ways  
===

# D3_JS

- **D3:** Offers high flexibility, allowing developers to create custom and intricate visualizations tailored to specific needs. **JavaScript:** Being a general-purpose language, JavaScript provides flexibility and versatility in handling various aspects of web development and visualization.

- In this visualization, I used D3, a powerful JavaScript library for creating dynamic and interactive data visualizations. The goal was to replicate a scatterplot.

- I started by loading the penguins dataset and defining the necessary scales for the x-axis (Flipper Length) and y-axis (Body Mass). Additionally, we employed a color scale for mapping penguin species and a size scale for the circle radius based on Bill Length.

- I utilized D3's data binding and enter-update-exit pattern to create circles representing each penguin observation. The positions on the x and y axes were determined by Flipper Length and Body Mass, respectively. Circle colors were mapped to penguin species, and the circle sizes were determined by Bill Length

- I added x and y axes to provide context to the scatterplot. Axis labels for "Flipper Length (mm)" and "Body Mass (g)" were included to guide the viewer.

- This D3 + JavaScript visualization closely achieves the functionality, allowing for interactive exploration of the penguins dataset.

![alt text](<01 JS _D3/D3.jpg>)


# Python_Plotly 

- **Python + Plotly** is a powerful combination for interactive and visually appealing data visualization. Plotly is a Python graphing library that enables the creation of various types of plots, charts, and dashboards. It provides a high-level interface for creating complex visualizations with ease. 

- Plotly allows the creation of interactive plots, which can be explored and manipulated by end-users. Zoom, pan, hover, and click functionalities enhance the interactivity.
 
![alt text](<02 Python_Plotly/Plotly.png>)


# Python_Altair 

- **Python + Altair** refers to using the Python programming language in conjunction with the Altair library for data visualization. 
- **Python**: Python is a versatile and widely used programming language. In the context of data visualization, Python is often chosen for its readability, ease of use, and a rich ecosystem of libraries. **Altair**: Altair is a Python library for declarative data visualization. It allows you to express visualizations in a concise and intuitive manner using a grammar of graphics approach. Altair generates Vega-Lite specifications under the hood, which are then rendered into interactive visualizations.
- Both Plotly and Altair can add title for the chart though I did not.

![alt text](<03 Python_Altair/Altair.png>)


 # Python_Matplotlib

 - **Matplotlib** is a comprehensive 2D plotting library for creating static, animated, and interactive visualizations in Python. It provides a versatile and flexible platform for generating high-quality plots and charts and integrates well with Jupyter Notebooks, providing an interactive environment for data exploration and visualization.
 - Matplotlib, Altair and Plotly are kind of similar. Mastering one of them, you'll know how others work.

 
![alt text](<04 Python_Matplotlib/Matplotlib.png>)

# Datawrapper

- **Datawrapper** Enrich your stories with charts, maps, and tables as it's slogan says, it's free and no sign-up is required. You can not image how easy it it to graph the designs based on your dataset. It is the most easiest way to get the scatterplot  for me by now. Just follow the process step by step and you will get your dreamed chart or maps. Really worthy trying.

![alt text](<05 Datawrapper/Datawrapper.png>)


# Flourish

- **Flourishr** is an online platforms designed for creating visualizations from data mostly like Datawrapper. **Flourish and Datawrapper** both prioritize user-friendly interfaces, catering to users without extensive coding or design experience. 
- From it's website, we could see flourish offeres more a range of templates and customization options than datawrapper and provides users with a variety of templates and themes, allowing for quick creation of **professional-looking** visualizations.

![alt text](<06 Flourish/Flourish.png>)

# R_ggplot2

- **ggplot2** is a powerful data visualization package in the R programming language. It is part of the tidyverse ecosystem and provides a flexible and layered grammar for creating a wide variety of static and interactive plots.
- Transitioning to plotnine in Python will be smoother. The syntax and concepts are very similar, allowing us to leverage our existing knowledge. 

![alt text](<07 R_ggplot2/ggplot.png>)

## Technical Achievements

### JS_D3
- **D3.js Integration**: The combination of D3 and JavaScript library are powerful for data visualization. D3.js allows for dynamic and interactive data-driven visualizations.
- **SVG**: The use of SVG elements for creating the scatterplot provides a scalable and resolution-independent graphical representation.
- **Data Binding and Data Visualization**: The code efficiently binds data from the provided CSV file (d3.csv("penglings.csv").then(data => {...}) and maps it to visual elements like circles, axes, and legends, enabling effective data visualization.
- **Scales and Axes**: Scales (e.g., xScale and yScale) and axes (e.g., d3.axisBottom and d3.axisLeft) are implemented to properly position and scale the data on the scatterplot.
- **Dynamic Tooltip Interaction**: The inclusion of a dynamic tooltip (const tooltip = d3.select("#scatterplot").append("div").attr("class", "tooltip");) enhances user interaction by providing detailed information on mouseover events.

### Python_Plotly
- **Feature Normalization**: Applied normalization to the bill_length_mm column, ensuring that data falls within a consistent range. Used the min-max normalization technique to standardize the values.
- **Scaled Sizes Calculation**: ntroduced a scaled_sizes column based on the normalized bill_length_mm, allowing for more meaningful size representations. Adjusted the scaling factor to enhance the visual impact of the scatter plot.

### Python_Altair & Matplotlib
- **Grammar of Graphics**: Altair is based on the Grammar of Graphics, providing a consistent and principled approach to data visualization. This allows for a high level of customization and flexibility in creating a wide range of visualizations.
- **Data Transformation**: Altair simplifies data transformation tasks, such as normalization and scaling, making it easy to prepare data for visualization without extensive preprocessing steps.
- **Compatibility with Pandas**: Altair seamlessly integrates with Pandas DataFrames, a popular data manipulation library in Python. This integration simplifies the process of loading, cleaning, and visualizing data.


### R_ggplot2
- **Grammar of Graphics in Python**: **plotnine** brings the Grammar of Graphics framework to Python, providing a consistent and expressive way to create complex visualizations.
- **Integration with Pandas**: The code seamlessly integrates with pandas DataFrames, a common data manipulation tool in Python, making it easy to work with structured data.


## Design Achievements

### JS_D3
- **Responsive Design**: The layout of the scatterplot and legend is designed to be responsive (display: flex; flex-direction: row;) and adaptable to different screen sizes.
- **Color Mapping and Legend**: Species information is visually encoded through color mapping, and a legend is provided to enhance the interpretability of the chart.
- **Clear Typography**: Clear and readable typography is employed for axis labels, legend items, and tooltip content, contributing to the overall clarity of the visualization.
- **User Interaction**: The inclusion of mouseover and mouseout events for circles provides a user-friendly interaction by displaying additional information when hovering over data points.


### Python_Plotly
- **Labels and Axes**: learly labeled the x-axis and y-axis as "Flipper Length (mm)" and "Body Mass (g)," respectively, enhancing the interpretability of the scatter plot. Ensured proper titling for axes and legend for a more informative visualization.
- **Margin and Layout**: Adjusted margin settings (left, right, top, bottom) to optimize the layout and spacing of the plot Achieved a balanced and aesthetically pleasing design.

### Python_Altair & Matplotlib
- **User-Friendly API**: Altair's API is designed to be user-friendly and intuitive. The consistent and clear syntax contributes to a smooth user experience, allowing users to focus on the visualization logic rather than dealing with complex configurations.


###  R_ggplot2
- **Theme Customization**: The code showcases the ability to customize the theme of the plot, allowing users to control the appearance of various elements, such as background color and grid lines.
