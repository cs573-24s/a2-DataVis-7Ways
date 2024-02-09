# Load necessary libraries

library(ggplot2)


# Read the dataset with specified column names and types
penguins <- read.csv("C:/Users/commu/OneDrive/Desktop/WPI/semester 2/DATA VISUALISATION/A2/a2-DataVis-7Ways/assignment 2/submission/R code/penglings.csv")

# Create the scatterplot
p <- ggplot(penguins, aes(x = flipper_length_mm, y = body_mass_g, color = species)) +
  geom_point() +
  labs(x = "Flipper Length (mm)", y = "Body Mass (g)", color = "Species")

# Save the scatterplot as a PNG file
ggsave("scatterplot.png", plot = p)
print(p)
# Confirm that the file was saved
file.exists("scatterplot.png")




