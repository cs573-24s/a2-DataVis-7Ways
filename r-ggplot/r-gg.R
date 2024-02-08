r = getOption("repos")
r["CRAN"] = "http://cran.us.r-project.org"
options(repos = r)
# install.packages("jsonlite", repos = 'https://cran.r-project.org')
# install.packages(c('palmerpenguins', 'tidyverse'))
# install.packages("tidyverse", dependencies=TRUE, type="source")
# install.packages("magrittr")
install.packages("plotly")
install.packages("shiny")
# install.packages("ggplot2", dependencies=TRUE)
library(palmerpenguins)
# library(magrittr)
library(ggplot2)
library(plotly)
library(tidyverse)

p <-penguins %>% 
ggplot(aes(x = flipper_length_mm, y = body_mass_g)) +
  geom_smooth(aes(group = species, color=species), method = "lm") +
  geom_point(aes(color = species, size=bill_length_mm, shape=island), alpha=0.8) +
  scale_color_manual(values = c("darkorange","darkorchid","cyan4")) +
  scale_shape_manual(values = c(15, 16, 17)) +
  labs(
    x="Flipper Length (mm)",
    y="Body Mass (g)"
  )
ggplotly(p)
# https://stackoverflow.com/questions/38412817/draw-a-trend-line-using-ggplot
# https://plotly.com/ggplot2/hover-text-and-formatting/