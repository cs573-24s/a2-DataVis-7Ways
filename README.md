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
In this project, R with ggplot2 excelled in creating an accurate and visually appealing scatterplot. The technical achievement was the precise control over the aesthetics, enabling us to match the features specified, such as color mapping to species and size mapping to bill length. This level of detail is essential for scientific data visualization where clarity and accuracy are paramount. However, managing the scale to not start at zero required careful adjustment of the scale_y_continuous and scale_x_continuous functions. 
### Python_Altair
Altair's declarative nature made creating the scatterplot straightforward, as it required simply stating the desired outcome in terms of data mappings. The technical achievement in this project was leveraging Altair's ability to encode the size of the points based on the bill length and to map colors to species without extensive coding. The challenge was to customize the scale properties to ensure that the axes did not start at zero. 
### JS_D3
D3.js offered the greatest flexibility and control over the final visualization, which was a significant technical achievement in itself. For this project, we were able to manually position data points and customize scales to match the non-zero starting point requirement. The difficulty lay in the complexity of D3's approach, requiring detailed understanding of SVG and JavaScript. 
### Tableau
Tableau's intuitive interface allowed for rapid creation of the scatterplot, which was a technical achievement in terms of efficiency. Aligning the scale to not start at zero was effortlessly handled by adjusting the axis properties.
### Vega-lite
With Vega-Lite, creating a compliant chart was a technical achievement due to its compact JSON syntax, which made encoding visual properties like color, size, and opacity straightforward. The semi-transparent effect was easily implemented by adjusting the mark properties. The challenge was to set the axes to not begin at zero, which required some adjustments to the scale domain. 
### Flourish
Flourish's ease of use was a technical achievement in terms of accessibility, allowing for the quick setup of the visualization without coding. It managed the non-zero axes and the mapping of colors and sizes to the respective data properties effectively. The platform's limitation was in customization, which was overcome by selecting the appropriate template to match the project's needs closely.
### Python_MatPlotlib
Using Python with Matplotlib was a technical achievement in data visualization fundamentals, providing granular control over every aspect of the plot. Customizing the axes to avoid starting at zero required manipulation of the xlim and ylim properties. Size mapping to bill length and color mapping to species were implemented with careful tuning of the scatter method parameters. 

## Design Achievements
### R_ggplot2
Design-wise, ggplot2 allowed for consistent use of theme elements, ensuring that the color choices and the transparency of the circles matched the project's requirements. The result was a clear, publication-ready chart that effectively communicated the data.
### Python_Altair
In terms of design, Altair's default settings provided a modern look with clean aesthetics, and the adjustment of point opacity to 0.8 achieved the semi-transparent effect needed for the visualization.
### JS_D3
Design achievements included creating custom interactions, such as tooltips that provide more details on mouseover, enhancing the user experience. D3.js was instrumental in creating a highly interactive and customizable visualization for web deployment.
### Tableau
While Tableau's drag-and-drop functionality made it easy to map color to species and size to bill length, the design achievement was in the tool's ability to quickly apply a polished and consistent style to the chart, making it suitable for business and analytics presentations.
### Vega-lite
Vega-Lite's design achievements were notable in the clean and crisp presentation of the data, with a focus on minimalistic design that is well-suited for web interfaces.
### Flourish
The design achievement was leveraging Flourish's built-in design templates, which provided a visually engaging and professional look suitable for storytelling and journalistic purposes.
### Python_MatPlotlib
The design achievements were in the creation of a chart with a consistent and clear visual language, with the use of custom color maps and the fine-tuning of opacity levels to achieve the semi-transparent effect, demonstrating Matplotlib's potential for detailed scientific visualization.