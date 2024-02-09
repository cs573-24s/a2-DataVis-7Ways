
# links: http://www.sthda.com/english/wiki/ggplot2-scatter-plots-quick-start-guide-r-software-and-data-visualization

# read data
penglings <- read.csv("~/penglings.csv")

# verify data
head(penglings)

# ggplot
library(ggplot2)

# Basic scatter plot
ggplot(penglings, aes(x=flipper_length_mm, y=body_mass_g)) + geom_point()

# Change the point size, and shape with geom_point
ggplot(penglings, aes(x=flipper_length_mm, y=body_mass_g)) +
  geom_point(aes(size=bill_length_mm, color=species), alpha=0.8)+
labs(title="Pengling Flipper Length by Body Mass",
     x="Flipper Length (mm)", y = "Body Mass (g)")


