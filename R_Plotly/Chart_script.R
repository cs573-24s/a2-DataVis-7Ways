library(plotly)

peng = read.csv('penglings.csv')

col1 = c('#FC7D0B', '#9D53F2', '#27AAB0')
col2 = c('#FC7D0B', '#1170AA', '#57606C')

chart1 <- plot_ly(data=peng, x=~flipper_length_mm, y=~body_mass_g, 
                  type='scatter', mode='markers',
                  color=~species,
                  colors=col1,
                  size=~bill_length_mm,
                  sizes=c(8,28),
                  marker=list(opacity=.8, sizemode='diameter'))%>%
  layout(xaxis=list(title='Flipper Length (mm)'), 
         yaxis=list(title='Body Mass (g)', dtick=1000, tick0=3000),
         legend=list(title=list(text='Species')))
chart1

chart2 <- plot_ly(data=peng, x=~flipper_length_mm, y=~body_mass_g, 
                  type='scatter', mode='markers',
                  color=~species,
                  colors=col2,
                  size=~bill_length_mm,
                  sizes=c(8,28),
                  marker=list(opacity=.8, sizemode='diameter'))%>%
  layout(xaxis=list(title='Flipper Length (mm)'), 
         yaxis=list(title='Body Mass (g)', dtick=1000, tick0=3000),
         legend=list(title=list(text='Species')))
chart2