# 02-DataVis-7ways

Assignment 2 - Data Visualization, 7 Ways  
===


Visualization Project README

Technical Achievements

1.	R + ggplot2
    Comparison of different penguin species using faceted techniques.

    Interactive tooltips were added for each data point using ggplotly from the plotly library.

    Using R and ggplot2 is a powerful experience due to R's powerful data handling capabilities 
    and ggplot2's flexibility. The syntax of the graph grammar makes layering plot elements very 
    easy. One of the challenges is how to optimize performance on large datasets. This tool is 
    particularly useful for scientific publications, where accuracy and customization are 
    critical.

2.	Excel

    Use conditional formatting to dynamically color data points based on species.

    Use Excel formulas to create dynamic axis scaling to accommodate different data ranges.

    Excel provides a familiar interface and allows direct manipulation of data points through a 
    graphical user interface for quick editing. More complex visual coding, such as adding 
    interactivity, can be difficult. excel is well suited to business environments that require 
    simple and quick modifications. Some manual adjustments were required to bring the visual 
    coding up to our standards.

3.	Altair

    Incorporate interactive legends into Altair that act as filters for visualizations, allowing 
    users to selectively hide or show species-specific data.

    Enable zooming and panning to explore data in a more interactive way.

    Altair's Python declarative approach makes creating initial visualizations quick and easy, 
    especially with its informative error messages. However, customizing interactive features 
    requires a deep dive into JavaScript callbacks.Altair shines in exploratory data analysis for 
    Jupyter notebooks. The data needs to be precisely structured to work with Altair's API.

4.	d3

    Developed a custom D3.js script for rendering interactive scatterplots and displaying more 
    data details via mouse hover events.

    Used D3 transition animation for inputting data points to produce an engaging initial 
    loading effect.

    D3.js offers unmatched flexibility and customization for scatterplots, but the learning 
    curve is steep. Control over the SVG canvas allows for complex visualization designs.D3 is 
    well suited for web developers creating interactive data-driven applications. Data binding 
    concepts are initially challenging, but once mastered prove powerful.

5.	DataWrapper

    Configure hover effects to show detailed information about each point, including metrics not 
    directly visualized, such as island and year.

    Implement a responsive design in DataWrapper to ensure that the visualization is mobile- 
    friendly.

    DataWrapper is the fastest way to go from data to a perfect visualization, so it's perfect 
    for journalists or others who need results quickly. Customization features are limited 
    compared to programming-based tools and there are some difficulties in getting the exact 
    dimensions of the visualization elements. It is a great tool for creating visualizations for 
    online media.

6.	Flourish
   
    A story slideshow was created in Flourish that guides the viewer through an interactive 
    narrative visualization step-by-step to dive deeper into the data.
  	
    Applying state triggers to elements, hovering the mouse over a data point highlights
    relevant data in other visualization components.

    Flourish's interface is very intuitive and offers a range of templates to easily get started 
    with data visualization. However, the limitations of some of the templates make it difficult 
    to achieve the level of detail required.Flourish is the perfect tool for creating 
    interactive visualization stories without coding.

7.	Tableau
   
    Enable tooltips and implement dashboard actions where selecting a point can filter 
    information in other related charts.
  	
    Create new visual summary metrics using calculated fields in Tableau.

    Tableau's drag-and-drop interface facilitates the rapid creation of visualizations, but 
    sometimes requires navigating complex menus to fine-tune visualization properties.Tableau's 
    proven power in processing and visualizing large data sets has made it a mainstay of the 
    data analytics and business intelligence fields. Data must be reshaped to fit Tableau's data 
    model effectively.

  	Design Achievements

1. Consistent Color Choice

   A uniform color palette was used across all platforms to represent the different species, thus enhancing the visual coherence of the project.

   Color-blind friendly color palettes were chosen to ensure accessibility.

2. Font Choice

   Choose clear, easy-to-read fonts (e.g. Arial) for all text elements to maintain consistency and readability across all visualization platforms.

   Ensure that font sizes are adjusted appropriately for the size of the visualization and screen resolution.

3. Element Size

   Normalize the size of the circles representing the data points so that differences in bill lengths in millimeters can be seen briefly.

   Adjust the size of the circles in the legend to match the size used in the plot for clear reference.

4. Additional Design Considerations

   Maintain consistent margins and padding across visualizations to ensure that no element appears crowded or misplaced.

   Use transparency to deal with overplotting to differentiate density in areas where data points overlap.
![image](https://github.com/wyh0210/a2-DataVis-7Ways/assets/145874479/148c13e2-9a1d-428d-9a49-7276f1ce4ad4)

