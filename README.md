
# R + ggplot2 + R Markdown

R is a language primarily focused on statistical computing.
ggplot2 is a popular library for charting in R.
R Markdown is a document format that compiles to HTML or PDF and allows you to include the output of R code directly in the document.

To visualized the cars dataset, I made use of ggplot2's `geom_point()` layer, with aesthetics functions for the color and size.

While it takes time to find the correct documentation, these functions made the effort creating this chart minimal.

![ggplot2](img/ggplot2.png)

# d3...
D3.js, or Data-Driven Documents, is a JavaScript library for manipulating and visualizing data using web standards such as HTML, SVG, and CSS. It is widely used for creating interactive and dynamic data visualizations in web browsers. I am using d3 on pycharm to create an HTML.
To be honest, the result of d3 compared with others is not that fancy, mostly due to the html constraints of pycharm.
However, the size of the circle can cleary be shown which is great, some of the python lib cannot do this.
To visualize the penglings.csv file,I am using the append and selectAll function to create the circles. The detail of the code can be seen in the d3.html file.
<img width="697" alt="d3" src="https://github.com/danile981199/a2-DataVis-7Ways/assets/63995138/50515490-5429-4ca5-94bb-6a6ea8cfb865">

# Altair
Altair is a declarative statistical visualization library for Python that simplifies the process of creating interactive and concise visualizations. It is built on top of the Vega-Lite and Vega visualization grammars, providing a high-level interface for creating a variety of visualizations with minimal code.
It is easy to use altair to visualize the file.
use alt.Color to change the color.
use alt.Chart(data).mark_circle to process the data, and you can use the make_circle function to create the circles you want.
<img width="755" alt="altair" src="https://github.com/danile981199/a2-DataVis-7Ways/assets/63995138/56bc05f2-4696-4d96-9b57-0965ea640fd6">

# Bokeh
Bokeh is an open-source Python library for interactive data visualization that targets modern web browsers. It enables the creation of interactive and real-time plots and dashboards in Python, which can be embedded in web applications or displayed in standalone HTML files.
It is not complicated but I do encounter some problems with it to size the circle. Because it doesn't work when you just adjust the size to the "length" like other python lib. And the end I set the size as the normal.
<img width="769" alt="Bokeh" src="https://github.com/danile981199/a2-DataVis-7Ways/assets/63995138/30e57182-d9de-4a27-a2ad-cb8010c04ad0">

# Plotly 
Plotly is a versatile open-source graphing library for Python, JavaScript, and R. It enables the creation of interactive and visually appealing visualizations, including charts, plots, and dashboards.
Plotly is easy to use as well.
Use px.scatter to create figure.
Use update to create the layout and x,y axes.
<img width="1420" alt="Screen Shot 2024-02-08 at 22 46 36" src="https://github.com/danile981199/a2-DataVis-7Ways/assets/63995138/dff4abf8-def6-4ebc-b18c-c886c5408ad4">

# Vega-lite
Vega-Lite is a high-level visualization grammar for creating expressive and concise visualizations. It is designed to simplify the process of building complex visualizations by providing a declarative syntax that allows users to specify the visual encoding of their data.
I use the online platform vega-editor to use vege-lite. It is great, but kind of confusing because you have to adapt to the new language rule.
One thing to notice is that if you wanna change the color you have to use the function :"scale": {"range": ["orange","purple","green"]},(eg.)
<img width="356" alt="vega editor" src="https://github.com/danile981199/a2-DataVis-7Ways/assets/63995138/d6a027f3-1b42-4244-93d2-08da6db0c22c">

# Seaborn + Matlab
Seaborn is a statistical data visualization library based on Matplotlib. It provides a high-level interface for creating attractive and informative statistical graphics. Seaborn is particularly well-suited for working with complex datasets and is designed to work seamlessly with Pandas DataFrames. 
This is a very useful lib to create the figure, visualizing through it is easy.
Similar to Plotly, just use one fuction scatterplot to process the data.
<img width="1440" alt="seaborn" src="https://github.com/danile981199/a2-DataVis-7Ways/assets/63995138/ceda6cfc-ab21-4182-8a21-3ee54267a828">

# Flourish
Flourish is an online data visualization platform that allows users to create interactive and engaging visualizations, charts, and stories without requiring advanced programming skills. It is designed to make data visualization accessible to a wide range of users, including journalists, educators, and data enthusiasts.
It is easy to use! Four steps: upload,check, visualize, publish. You can adjust the parameters at the third steps.

![flourish](https://github.com/danile981199/a2-DataVis-7Ways/assets/63995138/6476833f-2cd8-423a-9fa2-4218a55cf1ce)

# Datawrapper
Datawrapper is an online data visualization platform that simplifies the process of creating charts and visualizations. It is designed to be user-friendly, making it accessible to a wide range of users, including journalists, data analysts, and business professionals.
Honestly, just think this is the best method to visualize the data haha! It is super easy to use and everything is very clear, you can just type the alphat of the column to determine the x,y axes, the color,and the size. Pretty straighforward.

<img width="572" alt="datawrapper" src="https://github.com/danile981199/a2-DataVis-7Ways/assets/63995138/d44f8d4a-bcb1-4641-b7c5-d15d29a2f69c">


## Technical Achievements
- **Proved P=NP**: Using a combination of matlab and the seaborn, and a lot of different kinds python lib (NOT with the matlab!!)
- **Solved NaN values problem**: NaN values in the 'bill_length_mm' column were effectively handled to ensure a clean dataset for visualization.
- **Solved color problem**: For vega-lite, One thing to notice is that if you wanna change the color you have to use the function :"scale": {"range": ["orange","purple","green"]}.
- **Optimized Scatter Plot Size Calculation**: Utilized a default size and handled NaN values appropriately to resolve the 'Invalid element(s) received for the 'size' property' error in Bokeh and Plotly Express scatter plots, ensuring smooth and accurate visualization.

## Design Achievements
- **Color Philosophy**: I combine the knowledge learned in HCI class to create the more accessible visualization for people with deuteranopia and protanopia which can help them better access the information by using different color choice.
 For deuteranopia

<img width="572" alt="Screen Shot 2024-02-08 at 22 59 39" src="https://github.com/danile981199/a2-DataVis-7Ways/assets/63995138/55c1f339-3ef9-419c-8c01-6e65071ead96">
 
 For protanopia

<img width="573" alt="Screen Shot 2024-02-08 at 22 59 46" src="https://github.com/danile981199/a2-DataVis-7Ways/assets/63995138/0089e979-5aa2-417d-aea1-9ffa0386a4a0"> 

- **Shape Philospphy**:Use different shape to clarify the birthplace or sex information of the penguins. We can use different symbols to port various information.

![flourish](https://github.com/danile981199/a2-DataVis-7Ways/assets/63995138/f31831f2-9865-4f21-8960-39731d91438e)

<img width="572" alt="datawrapper" src="https://github.com/danile981199/a2-DataVis-7Ways/assets/63995138/fd18d569-5baa-4883-b779-e371a9b269a9">

- **How Scattered**: This is actually vert important if you wanna present a good visualization because your eyes will just perceive the information based on the density. Personally found the method that with the medium density is the best.

  low:

  <img width="769" alt="Bokeh" src="https://github.com/danile981199/a2-DataVis-7Ways/assets/63995138/8a38924a-5589-4cbf-8bd7-3f37d336af25">
 
  <img width="1440" alt="seaborn" src="https://github.com/danile981199/a2-DataVis-7Ways/assets/63995138/ff42a0ad-ca30-423a-8e85-70ae380fd1f7">
 
  medium:

   <img width="572" alt="datawrapper" src="https://github.com/danile981199/a2-DataVis-7Ways/assets/63995138/737b3b5d-7992-48e4-8a02-5949c5920f8a">
 
  high:

   <img width="356" alt="vega editor" src="https://github.com/danile981199/a2-DataVis-7Ways/assets/63995138/18f4f480-29be-4237-8bb5-4ef5f639be83">
