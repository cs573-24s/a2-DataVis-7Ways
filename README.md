Assignment 2 - Data Visualization, 7 Ways  
===
This assignment explores the visualization capabilities of several different tools and libraries across programming languages and software, including D3.js, Altair, Plotly, Bokeh, ggplot2 in R, OriginLab, and Excel.

# D3.js
Data Driven Documents (D3) is a JavaScript library for producing dynamic, interactive data visualizations in web browsers. This part was a complete challenge for me, as I have no experience in JavaScript, but I am amazed with its capabilities, especially hovering on functionalities.

D3.js was utilized to create an interactive scatter plot that showcases the relationship between flipper length and body mass, with the points colored by species and sized by bill length. This visualization was designed to be both informative and engaging, allowing users to explore the dataset in an intuitive manner.

Key features implemented with D3.js include some interactive elements, such as tooltips added to each data point, displaying detailed information about the penguin (e.g., species, measurements) on hover, enhancing the interactivity and accessibility of the data. In addition to the tooltip, when a user hovers over a penguin species, the plot emphasizes the selected species in its original color while dimming the others to grey. To achieve this effect, D3.js's event listeners were utilized to modify the opacity, color and size of the data points based on mouse events. Upon hovering (`mouseover` event) over a data point, a JavaScript function adjusts the styling of all other points to a lower opacity and changes their color to grey. Conversely, when the mouse leaves a data point (`mouseout` event), the plot returns to its original state, with all species displayed in their respective colors and full opacity. I possible extension could be zoom feature, which is useful when overlapping data points are visualized.

**Challenges**
- Learning Curve: D3.js has a steep learning curve, especially for those new to web development or JavaScript. Mastering its selection and data-binding model requires time and patience.
- Complexity in Implementation: Building a visualization from scratch with D3.js can be more time-consuming and complex compared to using high-level libraries, due to the need for detailed setup of scales, axes, and other plot components.

![d3_1](img/d3_1.png)

![d3_2](img/d3_2.png)

# Python - Plotly
Plotly is a very useful library that I've taken advantage of many times when I wanted to share something interactive. It comes with a default tooltip for users to investigate each data point. Also, I like the default zooming feature that I could not implement in javascript. It also guides user to 
![plotly](img/plotly.png)

# Python - Altair

Altair is a  visualization library for Python. It was quite easy to implement, yet I had to specify the x-axis and y-axis domains, which I would expect to be automatic. Also, I did not find the zooming feature user-friendly, as one could easily misorient the graph (and there is no guide how to reset it). 

![altair](img/altair.png)
# Python - Bokeh

This is another interactive visualization library that I used in Python. I found this one visually more appealing, because of several reasons: 1) Zooming options: box or wheel. 2) Tooltip: you can see all information for overlapping data points, and also tooltip can be deactivated.
![bokeh](img/bokeh.png)
# R - ggplot

R is the first analytical tool that I used for data visualization, and I wanted to try something different! I remember doing some visual graphic animations with `ggplot2` and `gganimate` libraries. In this animation, we observe changes in body mass and flipper length by species.

I am not aware of a similar animation library in Python, so I will definitely use it while presenting historical change of data.

![penguin_growth_over_time](img/penguin_growth_over_time.gif)
# OriginLab

OriginLab (my latest discovery) known for its advanced data analysis and graphing capabilities, offers a comprehensive solution for scientists and engineers looking to explore and visualize their data. I use this software when I do not need interactive visualizations for research papers, but highly quality custom plots. The good news is that WPI owns it!

I've used OriginLab quite a lot, so creating this chart was not a challenge for me. It has a very detailed interface, so it requires watching some tutorials before using it.

![Originlab](img/Originlab.png)

# Excel

Known for its spreadsheet capabilities, Excel also offers a range of built-in tools for basic to intermediate data visualization tasks. Surprisingly, excel took much more time than others (not d3), for several reasons: 1) I figured out late I should have used a bubble chart, but not a scatter plot; 2) Because of formatting issues, excel did not recognize x-axis values and generated completely wrong data points, which is a very common issue.

It does not have extensive customization capabilities, such as adjusting the legend freely, but it is a good option when no other software is available.

![excel](img/excel.png)

## Technical Achievements
- **Proved P=NP**: Using a combination of...
- **Solved AI Forever**: ...

### Design Achievements
- **Re-vamped Apple's Design Philosophy**: As demonstrated in my colorscheme...
