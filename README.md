# 02-DataVis-7ways

Assignment 2 - Data Visualization, 7 Ways  
===

Tips
---

- If you're using d3, key to this assignment is knowing how to load data.
You will likely use the [`d3.json` or `d3.csv` functions](https://d3js.org/d3-dsv) to load the data you found.

**Beware that these functions are *asynchronous*, meaning it's possible to "build" an empty visualization before the data actually loads. Figuring out how to do this properly can be a major hiccup if you haven't used async functions before. If this means you, start part of this project early so you don't end up in a rush!**

- *For web languages like d3* Don't forget to run a local webserver when you're debugging.
See my a1 video or online tutorials for how to do this.
Being able to host a local webserver is an essential web development skill and very common in visualization design as well.


**NOTE: THE BELOW IS A SAMPLE ENTRY TO GET YOU STARTED ON YOUR README. YOU MAY DELETE THE ABOVE.**

# R + ggplot2 + R Markdown

R is a language primarily focused on statistical computing.
ggplot2 is a popular library for charting in R.
R Markdown is a document format that compiles to HTML or PDF and allows you to include the output of R code directly in the document.

To visualized the cars dataset, I made use of ggplot2's `geom_point()` layer, with aesthetics functions for the color and size.

While it takes time to find the correct documentation, these functions made the effort creating this chart minimal.

![ggplot2](img/ggplot2.png)

# d3...
---
![Alt text](img/d3.png)
Tool: d3 

**What steps are done:**
- create login
- upload data
- draw report

**Advantage:**
- flexible
- plenty of examples and templates
           
**Disadvantage:** 
- comparing to the drag and drop tools programming knowledge required
**Where do I see this in future:**
- Due to the specialized nature of technical skills, particularly in coding, their widespread adoption among non-coders may be limited.
Hacks: 
- 

# Flourish
---
![Alt text](img/flourish.png)
Tool: flourish 
[Link:](https://app.flourish.studio/projects)

**What steps are done:**
- create login
- upload data
- draw report

**Advantage:** 
- easy to work
- free edition for try
- plenty of examples and templates
           
**Disadvantage:** 
- not flexible <-- for example: only 1 legend is available
- lack of data manipulation opportunities (you can add and delete columns but you can't do basic data maniplation such as create a new column as a sum of 2 other columns)

**Where do I see this in future:**
- if it improves the data manipulation ection it has potential to grow
Hacks: 
- Because of the technical limitation of the tool, I couldn't display the both legend but I customized the color legend to show required colors for related category

# powerbi 
---
![Alt text](img/pbi.png)
Tool: flourish 
Link: https://app.flourish.studio/projects

**What steps are done:** 
- upload data
- draw report

**Advantage:** 
- easy to work
- free desktop edition
- data manipulation capabilities
- plenty of examples and communities
           
**Disadvantage:** 
- not flexible enough like ggplot, d3
- for example: only 1 legend is available

**Where do I see this in future:**
      - it's already quite popular, so that will be continue
**Hacks:**
- Because of the technical limitation of the tool, but using the table trick I display the second legend

# vega-lite
![Alt text](img/vega-lite.png)

**Advantage:** 
- easy to learn
- flexible
- plenty of examples and communities
           
**Disadvantage:** 
- Coding knowledge required.

**Technical achievements:**
Declarative Syntax & Effective Data Mapping: Uses a concise and high-level syntax for visualization configuration and efficiently maps variables to visual channels for a comprehensive representation. 

Color Encoding & Palette Usage & Opacity Control: Implements a meaningful color scale for enhanced data interpretation, and applies a distinct and visually appealing color palette for species differentiation. Includes opacity for transparency, improving visibility in crowded regions. 

Dynamic Data Source: Enables dynamic loading of data from an external CSV file for adaptability.

Scale Configuration & Size Variation: Defines scales for accurate data representation and distribution and uses varying point sizes to convey additional information effectively.

**Design achievements:**
Data Range and size consideration: Carefully chosen scales prevent crowding or sparse regions, optimizing distribution.

Consistent Aesthetics: Unified color palette, color harmony,  opacity for Clarity and visual elements contribute to a cohesive design.

# Altair
---
![Alt text](img/altair.png)

**Advantage:**
- easy to work
- free edition for try
- plenty of examples and templates
           
**Disadvantage:**
- not flexible <-- for example: only 1 legend is available
- lack of data manipulation opportunities (you can add and delete columns but you can't do basic data maniplation such as create a new column as a sum of 2 other columns)

**Where do I see this in future:**
- if it improves the data manipulation ection it has potential to grow
**Hacks:**
- Because of the technical limitation of the tool, I couldn't display the both legend but I customized the color legend to show required colors for related category

**Technical achievements:**
Altair Chart Configuration: Utilizes Altair to create an interactive scatter plot with circles. Applies color mapping to species and sets a custom color range. Encodes size based on bill length, contributing an additional data dimension.

Tooltip Integration: Incorporates tooltips for interactive exploration, providing details on species and numerical variables when hovering over data points.

Mark Configuration: Configures the circle marks with a specified opacity level for better visibility.

Interactive Display: Uses the IPython display function to showcase the interactive chart within the Jupyter Notebook environment. In summary, the code effectively leverages Altair's capabilities to create an interactive and visually informative scatter plot, showcasing technical achievements in data visualization and exploration.

**Design achievements:**
Consistent Aesthetics: Maintains a consistent aesthetic with a specified color range and opacity, contributing to a unified and visually appealing design.

Color Mapping for Species: Implements a custom color mapping for each penguin species, enhancing visual distinction and facilitating species identification.

Size Encoding for Additional Insight: Utilizes point size to encode bill length, adding an extra layer of information to the plot and making it more informative.

# R + ggplot2 (plotly) + R Markdown
---
![Alt text](img/plotly.png)
Tool: flourish 
Link: https://app.flourish.studio/projects

What steps are done: 
- create login
- upload data
- draw report
Advantage: 
- easy to work
- free edition for try
- plenty of examples and templates
           
Disadvantage: 
- not flexible <-- for example: only 1 legend is available
- lack of data manipulation opportunities (you can add and delete columns but you can't do basic data maniplation such as create a new column as a sum of 2 other columns)
Where do I see this in future:
- if it improves the data manipulation ection it has potential to grow
Hacks: 
- Because of the technical limitation of the tool, I couldn't display the both legend but I customized the color legend to show required colors for related category

