library(ggplot2)
library(plotly)

data <- read.csv("C:/Users/nhein/Documents/Data Visualization/a2-DataVis-7Ways/R_ggplot2/penglings.csv")

# Create a ggplot object
ggplot_obj <- ggplot(data, aes(x = flipper_length_mm, y = body_mass_g, color = species, size = bill_length_mm)) +
  geom_point(alpha = 0.7) +
  labs(
    title = "Penguin Flipper Length vs Body Mass",
    x = "Flipper Length (mm)",
    y = "Body Mass (g)",
    color = "Species"
  ) +
  theme_minimal()

# Convert ggplot object to plotly
plotly_obj <- ggplotly(ggplot_obj, tooltip = c("species", "flipper_length_mm", "body_mass_g", "bill_length_mm"))

# Print the interactive plot
print(plotly_obj)
