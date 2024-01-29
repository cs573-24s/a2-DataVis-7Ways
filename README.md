# Assignment 2

## JavaScript + D3

This visualization tool was actually pretty difficult to use.
It takes a lot of effort to create a visualization, but it is a very customizable tool.
To visualize the data, I used a combination of d3's "csv" function and other tools to create shapes in svgs.
Since every element had to be created manually, the effort involved with this visualization was great.

![d3_no_hover](./img/d3_1.png)
![d3_hover](./img/d3_2.png)

#### Sources:

[1](https://d3-graph-gallery.com/graph/scatter_basic.html)
[2](https://stackoverflow.com/questions/11189284/d3-axis-labeling)
[3](https://d3-graph-gallery.com/graph/custom_legend.html)
[4](https://medium.com/@kj_schmidt/show-data-on-mouse-over-with-d3-js-3bf598ff8fc2)

## Python + Seaborn + Pandas + Matplotlib

This visualization tool was extremely easy to use.
It takes almost no effort (one line) to create a very nice looking graph and legend from the data.
To visualize the data, all you have to do is pass load the csv with pandas,
then use seaborn and matplotlib tools to plot this data.
When you make differentiate things by color, or size (ex. species and bill_depth_mm)
the program automatically creates a legend for you.
The program also offers a good amount of customizability, allowing the user to choose things in depth,
while also offering many different themes that work out of the box.

![seaborn_plot](./img/seaborn.png)

#### Sources

[1](https://stackoverflow.com/questions/14885895/color-a-scatter-plot-by-column-values)

### Design Achievements

Some of the design achievements that I attempted to achieve is clearly showing the visualization to the user.
I also clearly allowed the user to see which element they were hovering on in the main visualization by
having a red circle (as can be seen in photo 2).
This, linked with the detailed numbers shown on the bottom depending on which element is hovered on provides
a good experience for the user.

### Technical Achievements

Some of the technical achievements I achieved, was showing an element's detailed information on hover in D3.
I did this by adding "mousehover" and "mouseoff" elements to each circle when it was drawn.
When the user hovers over the element, the bottom updates with the information relevant to that element,
as well as adds a red outline to show which element is being hovered over.
When the user stops hovering, this red outline goes away, and the information on the bottom disappears.
