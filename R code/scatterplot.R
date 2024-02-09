library(ggplot2)
library(tidyverse)
library(servr)
library(plotly)
library(dplyr)

# Read the penguins.csv dataset
penguins <- read.csv("penglings.csv")

#plot
p <- penguins %>%
  ggplot(aes(x = flipper_length_mm, y = body_mass_g)) +
  geom_point(aes(color=species, size= bill_length_mm, shape=species), alpha = 0.8) +
  scale_size_continuous(name = "Penguin") +
  labs(x = "Flipper Length (mm)",
       y = "Body Mass (g)",
       caption = "Data source: Palmer Station LTER") +
  theme(legend.position = "bottom", 
        plot.caption = element_text(hjust = 0),
        strip.text.x = element_text(face = "bold"),
        plot.title = element_text(size = 18))
interactive_plot <- ggplotly(p)
interactive_plot
ggsave("interactive_plot.png", plot = p)

