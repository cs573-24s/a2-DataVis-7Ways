library(ggplot2)
library(plotly)

# load data
data <- read.csv("C:\\CS 573\\Assignments\\a2-DataVis-7Ways\\penglings.csv")
# View(data)

# setting color mapping
custom_colors <- c("Adelie" = "#F5761A","Gentoo" = "#00FF00", "Chinstrap" = "#800080")

# create the scatter plot
gg <- ggplot(data=data, aes(x=flipper_length_mm, y=body_mass_g, color=species,
                      size = ifelse(bill_length_mm < 40, 45, # mapping the size of the dots
                                    ifelse(bill_length_mm >= 40 & bill_length_mm < 50, 50, 60)),
                      alpha = 0.75,  text = paste("Species: ", species, "Flipper Length: ", flipper_length_mm,
                                                  "Body Mass: ", body_mass_g, "Size: ", bill_length_mm))) + # change opacity
  geom_point() +
  scale_color_manual(values = custom_colors) + # setting custom colors
  scale_size_continuous(breaks = c(45, 50, 60), guide = FALSE) + # maps the size and not show the label
  # adding titles and labels
  ggtitle("R + ggplot2 Graph") + 
  xlab("Flipper Length (mm)") +
  ylab("Body Mass (g)") +
  labs(color="Species") +
  guides(alpha = FALSE, color = guide_legend(order = 1)) # remove the alpha legend that keeps appearing 

# making the plot interactive
plotly_ggplot <- ggplotly(gg, tooltip = "text", dynamicTicks = TRUE) 
 
plotly_ggplot

