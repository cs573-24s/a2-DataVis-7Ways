# 02-DataVis-7ways

Assignment 2 - Data Visualization, 7 Ways  
===

Note: In each of the following pictures, the size of the scatters are not the same. Although in some pictures they look similar, the code underneath has made sure the size of the scatters are based on the bill_length.  

# R_ggplot2

- **ggplot2** 
Using R with ggplot2 was a smooth experience for creating the scatterplot. The grammar of graphics syntax that ggplot2 employs is intuitive and allows for a high level of customization with minimal code. One challenge was fine-tuning the aesthetic elements such as the exact size of points and the transparency level to match the original visualization. ggplot2's strength lies in its versatility and the ability to create complex, multi-layered graphics, which would be useful for academic publications or professional reports. No significant data manipulation was required due to ggplot2's ability to handle data frames effectively.

![penguin_R_ggplot2.png](<img/penguin_R_ggplot2.png>)

# Python_Altair 
Altair in Python provided a declarative approach to data visualization which made the creation of charts quite straightforward. The difficulty arose when trying to replicate the exact look and feel of the sample due to some of Altair's default settings. Altair shines when it comes to creating interactive visualizations for web-based applications due to its seamless integration with Vega-Lite. Some data transformation was necessary to deal with missing values and to adjust size scales. 

![penguin_Python_Altair.png](<img/penguin_Python_Altair.png>)

# JavaScript_D3
D3.js was the most flexible yet the most complex tool to use. It required a deeper understanding of JavaScript and SVG manipulation. The steep learning curve was a challenge, but it offered unparalleled control over the final visualization. D3.js would be highly useful for custom web-based visualizations where unique interactive behaviors are required. To achieve the desired chart, substantial data manipulation was performed using JavaScript array methods. 

![penguin_JavaScript_D3.png](<img/penguin_JavaScript_D3.png>)

 # Tableau
Tableau's drag-and-drop interface made it exceptionally easy to create a scatterplot quickly. The difficulty was in fine-tuning the visualization to match the specific requirements, as Tableau's ease of use can sometimes come at the cost of granular control. Tableau is ideal for business intelligence tasks and rapid prototyping of visualizations. Little to no data manipulation was needed due to Tableau's robust data handling capabilities. 

 ![penguin_Tableau.png](<img/penguin_Tableau.png>)

# Vega-lite
Vega-Lite, being a high-level visualization grammar, allows for quick and concise description of interactive multi-view graphics. The challenge with Vega-Lite was similar to Altair (as Altair is a wrapper for Vega-Lite) in needing to tweak the default behaviors and settings. Vega-Lite is particularly useful for web developers looking to embed visualizations with minimal overhead. Some data transformation was handled within the Vega-Lite specification. 

![penguin_Vega-lite.png](<img/penguin_Vega-lite.png>)

# Flourish
Flourish made it extremely easy to create and share visualizations without any coding. The platform's limitations became apparent when trying to customize the chart beyond the provided templates. Flourish is best suited for journalists and educators who need to convey information quickly and with visual impact. The tool's user-friendly interface negated the need for data manipulation. 

![penguin_Flourish.png](<img/penguin_Flourish.png>)

# Python_Matplotlib
Matplotlib in Python is a foundational library for plotting in Python, offering extensive control over elements. It can be challenging to use for those who are not familiar with its object-oriented interface. It's highly useful for scientific computing and when precise adjustments to plots are needed. Data manipulation was straightforward with pandas integration. 

![penguin_Python_Matplotlib.png](<img/penguin_Python_Matplotlib.png>)


## Technical Achievements
### R_ggplot2
A technical achievement with ggplot2 was adding interactive tooltips using the ggplotly function from the plotly package, enhancing the user experience by displaying detailed information on hover.
### Python_Altair
A technical achievement was the implementation of interactive filters that allow users to dynamically change which species are displayed. 
### JS_D3
Technical achievements involved implementing custom animations and interactivity, such as dynamic data updates. 
### Tableau
The difficulty was in fine-tuning the visualization to match the specific requirements, as Tableau's ease of use can sometimes come at the cost of granular control. 
### Vega-lite
A technical achievement was the addition of interactive legends that update the chart in real time. 
### Flourish
A technical achievement was the use of Flourish's storytelling feature to walk through the data points.
### Python_MatPlotlib
A technical achievement with Matplotlib was creating subplots that provide additional context to the main scatter plot. 

## Design Achievements
### R_ggplot2
Design-wise, achieving a consistent look with theme elements and a color palette that reflected the data's categories was straightforward.
### Python_Altair
Design achievements included using Altair's theming capabilities to match the visualization style to the project's overall design language.
### JS_D3
From a design perspective, D3.js allowed for precise control over the visual elements, enabling a consistent and tailored design schema.
### Tableau
A design achievement was the use of Tableau's formatting options to create a visually appealing and cohesive design that adheres to brand guidelines.
### Vega-lite
Design-wise, Vega-Lite's themes were utilized to maintain consistency with the project's visual standards.
### Flourish
The design was enhanced by Flourish's built-in themes and style options, ensuring a polished and professional look.
### Python_MatPlotlib
Design achievements involved customizing the plot style to create a cohesive appearance, including matching the color palette and font choices to those of the main visualization.