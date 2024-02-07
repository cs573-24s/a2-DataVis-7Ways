library(ggplot2)

data <- read.csv("C:/Users/nhein/Documents/Data Visualization/a2-DataVis-7Ways/R + ggplot2/penglings.csv")


plot <- ggplot(data, aes(x = flipper_length_mm, y = body_mass_g, color = species, size=(bill_length_mm))) +
  geom_point(alpha = 0.7) +  
  labs(title = "Penguin Flipper Length vs Body Mass",
       x = "Flipper Length (mm)",
       y = "Body Mass (g)",
       color = "Species") +  
  theme_minimal() 

print(plot)