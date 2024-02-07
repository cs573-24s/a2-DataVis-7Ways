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

# Python + Matplotlib Pyplot

Matplotlib's Pyplot is an API of Python's Matplotlib library. It consists of a collection of functions that enable users to manipulate visualizations similar to MATLAB. 

To visualize the penglings dataset, I first dropped the Null values using the pandas `dropna()` function and then utilized the `plt.scatter()` function to build the baseline graph. Like the first two visualizations, this one was also fairly easy to accomplish; however, it did require some additional code to include the color mapping legend in the graph. 

Overall, this library was very easy to use and was quite similar to Plotly in terms of how much code was required to obtain the baseline graph. As such, this would also be a great library to utilize if in need of quick data visualizations since it has relatively few coding requirements. 

### Technical Achievments 

For this visualization, I decided to add an extra tooltip functionality (coded within the `mplcursors.cursor()`function) to allow users the option to hover and inspect data points within the graph. `mplcursors` is a Python library that provides interactive cursor feedback for Matplotlib plots. Similar to the second graph, I also reformatted the tooltip display names to be visually appealing. 

![PyVis3](img/PyVis3.png)

# Python + Bokeh 

Bokeh is a Python library designed for creating interactive and data-driven visualizations in web browsers. It provides a flexible and easy-to-use interface for building a wide range of interactive plots, dashboards, and applications for data exploration and analysis. 

To visualize the penglings dataset, I first dropped all Null values using pandas' `dropna()` function and then moved on to designing the actual baseline visualization. Unlike the prior 3 libraries, Bokeh required more coding and was generally not as intuitive. I first had to use the `figure()` functionality to establish the graphing object. Then, I implemented some styling changes like axis font sizes and the axis tickers (via the `SingleIntervalTicker()` function). Finally, I went about plotting the actual points using the `p.scatter()` function to specify additional graph details.

Overall, I didn't feel this was quite as intuitive as the the previous graphs; however, it was still easy to use after reading some documentation. Since it requires a bit more code, I wouldn't suggest it as a first choice for making quick visualizations, but I could see it being advantageous for creating interactive and web-based visualizations that require a high degree of customization and interactivity. The Bokeh library itself has lots of sub functionalities that make its capabilities quite broad. 

### Technical Achievments 

For this graph, I also added a hover-to-inspect functionality using Bokeh's `HoverTool()`. Thus, users can hover over points on the graph to inspect the individual values.

![PyVis4](img/PyVis4.png)

# Javascript + D3

D3 is a JavaScript library commonly utilized for crafting dynamic and interactive data visualizations in web browsers. Its data-driven approach, extensive feature set, and flexibility has made it a preferred tool for constructing sophisticated and captivating visual representations. 

To visualize the penglings dataset, I first loaded the csv data asynchronously using the `d3.csv()` function. Attached to this is a `then()` function, which encapsulates the scatterplot design code. Within the design code, I implemented a mixture of SVGs, variables, and filters to manipulate and plot the data (along with corresponding legends/axis labels). Additionally, in order to ensure that the code didn't attempt to build an empty graph if the data failed to load, I added a the `catch()` function to specify that a console error message should be outputted. 

I felt this graph was definitely the hardest to construct due to the amount of coding it required. Unlike the previous tools and libraries used, this needed extensive specifications for design elements like margins, axis scaling, text rotation, legend design, etc. Thus, it is definitely the least beginner-friendly option. This being said, because users can control so many minute details in the code, I see this option being most useful for constructing especially detailed and complex data visualizations. Yes, it would require more time in the long run, but users would be able to have more creative control of the elements.

![D3Vis](img/D3Vis.png)

