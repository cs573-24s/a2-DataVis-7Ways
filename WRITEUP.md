# 02-DataVis-7ways

Assignment 2 - Data Visualization, 7 Ways  

- Write a paragraph for each visualization tool you use. What was easy? Difficult? Where could you see the tool being useful in the future? Did you have to use any hacks or data manipulation to get the right chart?
===

# Python + Plotly Express (PyVis1)

Plotly Express is a graphing library available for use with Python. Originally developed by the company Plotly, this library provides users with access to DASH graphics with ease through the inclusion of a wide variety of functions and graph objects that negate the necessity of lengthy code segments. 

To visualize the penglings dataset, I first made sure to drop null values (which originally skewed the chart oddly) using the Pandas `dropna()` function and then utilized the `scatter()` function to build the baseline requirements for the graph (no hacks required). Thanks to Plotly Express' built in function features, I didn't need to write any additional code to access species filters and hover functionalities. To filter the graph by species, all that's required it tapping (to deselect from one) or double tapping (to deselect from ALL but one) the species legend on the right hand side of the graph. Similarly, to get more insight on points, all that's required is a simple hover over each point with the cursor. 

Overall, I found this tool very easy to use and I can see it being useful in scenarios that might require many simple visualizations. Because it has so many extra features built into its graphing functions, it can save users a lot of time on the coding and design end of things. 

![PyVis1](img/PyVis1.png)

# Python + Altair (PyVis2)

Altair is a declarative statistical visualization library for Python. It's designed to streamline the coding process, enabling users to spend more time analyzing and understanding visualizations, rather than focusing on the pure coding aspect.

To visualize the penglings dataset, I first dropped the Null values using the pandas `dropna()` function and then utilized the `alt.Chart()` function to implement the visualization requirements. Unlike the Plotly graph, this one did not automatically format the design elements correctly. For example, I had to manually specify domain scales and axis ticks in order to better mimic the original (whereas in plotly it was all done automatically). 

However, overall I would still say this tool is still very easy to use and would be beneficial when in need of quick visualizations of datasets big and small. Like plotly, the streamlined functionalities and limited coding requirements makes this tool very accessible to non-technical audiences. 

### Technical Achievements

For this visualization, I decided to add an extra tooltip functionality (coded within the `alt.Chart()`function) to allow users the option to hover and inspect data points within the graph. I also renamed the tooltip display names to be more visually appealing by removing the original column names and reformatting them into proper titles with units properly parenthesized.

![PyVis2](img/PyVis2.png)

