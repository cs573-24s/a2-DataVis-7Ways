library(tidyverse)
library(ggnewscale)
library(palmerpenguins)
library(colorspace)

cols <- c("darkorange","darkorchid","cyan4")
penguins %>% 
  ggplot(aes(x = flipper_length_mm, y = body_mass_g)) +
  scale_color_manual(values = cols) +
  geom_point(aes(color = species, size=bill_length_mm), alpha=0.8) +
  new_scale_color()+
  geom_smooth(aes(color = species, group = species), method=lm, se=FALSE, fullrange=TRUE)+
  scale_color_manual(values = darken(cols, .15)) +
  facet_grid(~island, scales='free') + 
  labs(
   x="Flipper Length (mm)",
   y="Body Mass (g)"
  )  
