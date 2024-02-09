library(ggplot2)
library(readr)
library(dplyr)

# Read the dataset 'penglings.csv' into a variable
penguins <- read_csv("penglings.csv")

# Remove rows with missing values if they are not relevant for the visualization
#penguins <- penguins %>% drop_na()
#penguins <- dplyr::drop_na(penguins)
# Filter out rows with NA values using base R
penguins <- penguins[complete.cases(penguins), ]

# Next, create the scatter plot using ggplot2
penguin_plot <- ggplot(penguins, aes(x = flipper_length_mm, y = body_mass_g, color = species, size = bill_length_mm)) +
  # Add the scatter plot layer with specified opacity
  geom_point(alpha = 0.8) +
  # Define the scale of the size for better visualization
  scale_size_continuous(name = "Bill Length (mm)", range = c(3, 8)) +
  # Add labels to the axes
  labs(x = "Flipper Length (mm)", y = "Body Mass (g)") +
  # Customize the color scale to match species
  scale_color_manual(values = c("Adelie" = "orange", "Chinstrap" = "purple", "Gentoo" = "#008080")) +
  # Adjust the axis limits and breaks for better matching the data
  scale_x_continuous(breaks = seq(170, 233, by = 10), limits = c(170, 233)) +
  scale_y_continuous(breaks = seq(2500, 6500, by = 500), limits = c(2500, 6500)) +
  # Remove the legend for size
  theme(legend.position = "right")

# Print the plot
print(penguin_plot)
ggsave("penguin_R_ggplot2.png", plot = penguin_plot, width = 10, height = 7.5, dpi = 300)



