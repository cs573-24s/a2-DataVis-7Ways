# 02-DataVis-7ways

Assignment 2 - Data Visualization, 7 Ways  

- Write a paragraph for each visualization tool you use. What was easy? Difficult? Where could you see the tool being useful in the future? Did you have to use any hacks or data manipulation to get the right chart?
===

# Python + Plotly Express (PyVis1)

Plotly Express is a graphing library available for use with Python. Originally developed by the company Plotly, this library provides users with access to DASH graphics with ease through the inclusion of a wide variety of functions and graph objects that negate the necessity of lengthy code segments. 

To visualize the penglings dataset, I first made sure to drop null values (which originally skewed the chart oddly) and then utilized the `scatter()` function to build the baseline requirements for the graph (no hacks required). Thanks to Plotly Express' built in function features, I didn't need to write any additional code to access species filters and hover functionalities. To filter the graph by species, all that's required it tapping (to deselect from one) or double tapping (to deselect from ALL but one) the species legend on the right hand side of the graph. Similarly, to get more insight on points, all that's required is a simple hover over each point with the cursor. 

Overall, I found this tool very easy to use and I can see it being useful in scenarios that might require many simple visualizations. Because it has so many extra features built into its graphing functions, it can save users a lot of time on the coding and design end of things. 

![PyVis1](img/PyVis1.png)




R is a language primarily focused on statistical computing.
ggplot2 is a popular library for charting in R.
R Markdown is a document format that compiles to HTML or PDF and allows you to include the output of R code directly in the document.

To visualized the cars dataset, I made use of ggplot2's `geom_point()` layer, with aesthetics functions for the color and size.

While it takes time to find the correct documentation, these functions made the effort creating this chart minimal.

![ggplot2](img/ggplot2.png)