# 02-DataVis-7ways

Assignment 2 - Data Visualization, 7 Ways  
===

Your goal is to use 7 different tools to make the following chart:

![](img/ggplot2.png)

These features should be preserved as much as possible in your replication:

- Data positioning: it should be a upward-trending scatterplot as shown.  Flipper Length should be on the x-axis and Body Mass on the y-axis.
- Scales: Note the scales do not start at 0.
- Axis ticks and labels: both axes are labeled and there are tick marks at a reasonable interval, e.g 10, 20, 30, etc.
- Color mapping to species.
- Size mapping to Bill Length.
- Opacity of circles set to 0.8 or similar for a semi-transparent effect.

Libraries, Tools, Languages
---
The 3 libraries I used include: `Python, R, Javascript` with tools including `d3, altair, plotly, seaborn, ggplot, lattice, and Flourish`.

Readme Requirements
---

A good readme with screenshots and structured documentation is required for this project. 
It should be possible to scroll through your readme to get an overview of all the tools and visualizations you produced.

- Write a paragraph for each visualization tool you use. What was easy? Difficult? Where could you see the tool being useful in the future? Did you have to use any hacks or data manipulation to get the right chart?

Other Requirements
---
Your writeup (readme.md in the repo) should also contain the following:

- Description of the Technical achievements you attempted with this visualization.
  - Some ideas include interaction, such as mousing over to see more detail about the point selected.
- Description of the Design achievements you attempted with this visualization.
  - Some ideas include consistent color choice, font choice, element size (e.g. the size of the circles).

GitHub Details
---

- Fork the GitHub Repository. You now have a copy associated with your username.
- To submit, make a [Pull Request](https://help.github.com/articles/using-pull-requests/) on the original repository.

# R + ggplot2 + R Markdown

R is a language primarily focused on statistical computing.
ggplot2 is a popular library for charting in R.
R Markdown is a document format that compiles to HTML or PDF and allows you to include the output of R code directly in the document.

To visualize the penguins dataset, I made use of ggplot2's `aes()` function to visualize the correct data with the correct color categories and size dimentions. Additionally, I used `geom_point()` to adjust the opacity of the data points distributed throughout the graph. 

The documentation of ggplot(2) was rather easy to find and to follow. While it didn't make the most elegant chart, it was extremely easy to put this chart together. Despite the data having NaN values, ggplot() didn't account for any of them within the graph which made the cleaning of the data one step easier. I would use ggplot() in the future when I am trying to create an aesthetically easy yet simple chart to make. 

![ggplot2](img/ggplot2.png)

# R + lattice + R Markdown
R is a language primarily focused on statistical computing.
lattice is a popular statistical graphin library used to create visualizations for multivariate relationships. 
R Markdown is a document format that compiles to HTML or PDF and allows you to include the output of R code directly in the document.

I have no experience with lattice, so this was completely new to me. By using the libraries `xyplot()` feature, plotting was equally as straightforward as ggplot. Lattice, did allow me to use its multivariate analysis of features by visualizing each specie type in its own graph parallel to the other. I was also able to easily add in colors for each specie type making the categories very distinguishable. In the future, I intend to utilize lattice to visualize a plot in a manner that better conveys its meaning by separating the categories rather than stacking them on top of each other.

![lattice](img/ggplot2.png)

# Python + altair + VSCode
Python is a wide-ranging dynamic programming language used for general-purpose. It's design philosphy emphasizes the readability of code. 
Altair is a declarative statistical visualization library for Python.
VSCode is an IDE (integrated development environment) used for scripting, debugging, embedding Git, etc. 

To visualize the penguin dataset with Python and altair I first had to load in and clean the data by removing NaN values and the first column. Once the data processing was complete, I employed altair's `alt.Chart().mark_point().encode()` documentation. Altair was not the easiest to use and gave me a lot of trouble once I was attempting to plot or visualize the data. Eventually, I used `chart.save()` in order to be able to view the plot. Nevetheless, I did enjoy how much I was able to control with the graph such as the x and y-axis ranges and where they started. 

Altair also allows the user to interact with the graph by clicking and dragging. Simple features such as this go a long way within a visualization. I would use altair in the future if I was using it within a webpage. 

![altair](img/ggplot2.png)

# Python + plotly + VSCode
Python is a wide-ranging dynamic programming language used for general-purpose. It's design philosphy emphasizes the readability of code. 
Plotly is a python library designed to make graphing and data visualizations interactive.
VSCode is an IDE (integrated development environment) used for scripting, debugging, embedding Git, etc. 

To visualize the penguin dataset with Python and plotly I first had to load in and clean the data by removing NaN values and the first column. Once the data processing was complete, I employed plotly's `px.scatter()` function to plot the data. Plotly was extremely easy to use and customize. I was seamlessly able to change the color and shape for each specie type. Plotly scatterplots also have built in functions that let the user interact with the data by using a lasso effect to focus only on a portion of the data. Additionally, there are options to zoom in and out of the data making the view of the information flexible. 

![plotly](img/ggplot2.png)

# Python + seaborn + VSCode
Python is a wide-ranging dynamic programming language used for general-purpose. It's design philosphy emphasizes the readability of code. 
Seaborn is a python library based on matplotlib that provides a high-level interace for attractive/informative statistical graphs. 
VSCode is an IDE (integrated development environment) used for scripting, debugging, embedding Git, etc. 

To visualize the penguin dataset with Python and seaborn I first had to load in and clean the data by removing NaN values and the first column. Once the data processing was complete, I employed seaborn's `sns.scatterplot()` function to plot the data. Seaborn had very robust documentation and allowed the creator to edit almost all components of the figure. Once the data was plotted and shown, it reminded me very much of plotly's features I mentioned above. Click and drag, zoom, and save were all available. My favorite feature was the undo and redo button within the figure. 

![seaborn](img/ggplot2.png)

# Flourish
Flourish is an interactive data visualization tool that enables the creation of data stories through a web-based app. 

Visualizing the penguin dataset using Flourish was an extremely easy task. Honestly, it took longer to sign-up for Flourish than to create the scatterplot. I enjoyed exploring and messing around with Flourishs' features. I was able to change the animation of the graph, the text-style, and include filter's to adjust the data on the scatterplot. I thing Flourish was a less complicated Tableau and Power BI. 

![flourish](img/ggplot2.png)

# d3 + JS + VSCode
d3 is a JS library used to produce dynamic, interactive data visualizations in web browsers using SVG's.
JS (JaveScript) is a programming language used alognside CSS and HTML to design webpages. JS controls the interactions within the website. 
VSCode is an IDE (integrated development environment) used for scripting, debugging, embedding Git, etc. 

![d3JS](img/ggplot2.png)

Visualizing the penguin dataset using d3 and JS was easily the hardest but most validating graph to make out of the 7. I completed this interactive plot by using `svg.append(), function()`, and `scaleLinear()`. Every feature seen previous in other graphs had to be manually coded in such as the legend, the size of the dots, and the color of the dots. If I truly wanted to make something that was my own, I would use d3 + JS as it gave me a blank canvas and allowed me to craft whatever I envisioned. For this specific graph, I included a mouseover function that would highlight all the species in the group. This simple interaction really made the entire graph come together for me. 

## Technical Achievements
- **Proved P=NP**: Using a combination of...
- **Solved AI Forever**: ...

### Design Achievements
- **Re-vamped Apple's Design Philosophy**: As demonstrated in my colorscheme...
