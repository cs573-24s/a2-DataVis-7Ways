library(ggplot2)

data <- read.csv('penglings.csv')

data %>%
ggplot(aes(x = flipper_length_mm, y = body_mass_g)) +
  geom_point(aes(color = species, size=bill_length_mm), alpha=0.8) +
  scale_color_manual(values = c("darkorange","darkorchid","cyan4")) +
  labs(
    x="Flipper Length (mm)",
    y="Body Mass (g)"
  )

