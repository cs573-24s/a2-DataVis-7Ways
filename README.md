# Assignment 2

## JavaScript + D3

This visualization tool was actually pretty difficult to use.
It takes a lot of effort to create a visualization, but it is a very customizable tool.
To visualize the data, I used a combination of d3's "csv" function and other tools to create shapes in svgs.
Since every element had to be created manually, the effort involved with this visualization was great.

![d3_no_hover](./img/d3_1.png)
![d3_hover](./img/d3_2.png)

#### Sources

[1](https://d3-graph-gallery.com/graph/scatter_basic.html)
[2](https://stackoverflow.com/questions/11189284/d3-axis-labeling)
[3](https://d3-graph-gallery.com/graph/custom_legend.html)
[4](https://medium.com/@kj_schmidt/show-data-on-mouse-over-with-d3-js-3bf598ff8fc2)

## Python + Seaborn + Pandas + Matplotlib

This visualization tool was extremely easy to use.
It takes almost no effort (one line) to create a very nice looking graph and legend from the data.
These tools are used a lot to preprocess and explore data when viewing data for AI / ML
To visualize the data, all you have to do is pass load the csv with pandas,
then use seaborn and matplotlib tools to plot this data.
When you make differentiate things by color, or size (ex. species and bill_depth_mm)
the program automatically creates a legend for you.
The program also offers a good amount of customizability, allowing the user to choose things in depth,
while also offering many different themes that work out of the box.
To get the chart to closer mimic the example plot, I had to change a few of the pre-set stylings, such as the color.

![seaborn_plot](./img/seaborn.png)

#### Sources

[1](https://stackoverflow.com/questions/14885895/color-a-scatter-plot-by-column-values)

## Python + Altair + Pandas

This visualization tool was also extremely easy to use.
It took almost no effort to create a very nice looking graph and legend from the data.
The syntax was very nice and easy to pick up and allowed me to quickly create a graph with
relevant visuals and customize it how I liked.
I think compared to the other tool I used in Python (Seaborn), Seaborn has a little bit nicer default settings
which makes it easy to quickly visualize something, but Altair makes it a lot easier to customize the visualization and
get it exactly how you like it. I think between the two I would prefer Altair better, as you can display things very easily
and the library feels a bit more Pythonic and simple.

![altair_chart](./img/altair.png)

#### Sources

[1](https://altair-viz.github.io/user_guide/customization.html#customizing-colors)
[2](https://altair-viz.github.io/gallery/scatter_tooltips.html)

## R + ggplot2

This visualization tool was a bit tricky to use for me,
as I had no prior experience with R. It took me a little
bit to set up a working R environment, and download the necessary
libraries such as the penglings dataset as well as the tidyverse library
among others. I think that with more experience, R and ggplot2 is a nice
and easy way to make visualizations and color schemes that are customizable.
It did seem, however, that as you want to make more specific / detailed
changes, it was more and more difficult to do in ggplot2, and I had to resort
to using helper libraries such as colorspace and ggnewscale specifically
for managing color schemes.
For this visualization I used the basic code provided in the starter files
and expanded on it.
Instead of showing all of the penguins in one chart, I split the observations
into charts according to island. I also drew a line of best fit for each
species in each chart to help visualize the overall relationship between
body mass and flipper length per species on each island.

### Visualzation 1: Free X Axis Scale

I first created a visualization (Visualization 1) with a free X axis scale.
This aesthetically looks nicer, however when comparing the lines of best fit
and the graphs for each island, I realized that it was misleading when the
axes were not evenly spaced for each island.

![r_chart](./img/r.png)

### Visualzation 2: Fixed X Axis Scale

o remedy this, I created Visualization 2, where I evenly spaced the axes
for each sub-chart. This way, a viewer of the charts can more easily make
connections and comparisons between the sub-visualizations.

![r_chart](./img/r2.png)

## Technical Achievements

### Show an Element's Detailed information on Hover in D3

I did this by adding "mousehover" and "mouseoff" elements to each circle when it was drawn.
When the user hovers over the element, the bottom updates with the information relevant to that element,

### Show a Red Circle Around Hovered Item in D3

I did this by also using the "mousehover" and "mouseoff" elements.
When the user hovers over an element, I add a red outline to the
selected element so the user knows which element is selected
When the user stops hovering, this red outline goes away, and the
information on the bottom disappears.

### Display Observations Per Island in R

I did this by using the facet_grid() function included in ggplot2.

### Display Lines of Best Fit Per Species in R

I did this by using the geom_smooth() function in ggplot2. This function
automatically creates a line of best fit for the current dataset. I
also grouped this functionality to create a line of best fit for each
species in each subplot. To achieve custom colors different from the color
scheme specified for the species for the point graph, I needed to use
two different libraries: colorspace, and ggnewscale. Colorspace allowed me
to darken the existing color scheme to use again for the lines of best fit,
and ggnewscale allowed me to create a separate color scheme for the
geom_smooth() function. 

## Design Achievements

### Clear Legend on All Charts

For every chart, I included a legend showing which species corresponded with which color,
as well as an example circle size for the bill_length_mm value

### Consistent Color Choice

For every chart, I used the same colors, matching the hex colors used in the example plot.

### Allow User to See Which Element is Being Hovered in D3

I clearly allowed the user to see which element they were hovering on in the main visualization by
having a red circle (as can be seen in photo 2 in the D3 section).
This, linked with the detailed numbers shown on the bottom depending on which element is hovered on provides
a good experience for the user.

### Display Observations Per Island in R

I did this by using the facet_grid() function included in ggplot2. This
allows the viewer of the visualization to make connections between the
island that the observation occured on, and the flipper length and body mass
of each species.

### Show Lines of Best Fit Colors Clearly on Chart and Match to Species in R

I allowed the lines of best fit to match the species color, but darkened
these lines so that they were more visible and did not blend in with the
points themselves on the graph. To do this I used the darken functionality
in the colorspace library as well as the ggnewscale library.
