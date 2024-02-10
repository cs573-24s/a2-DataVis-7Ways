library(ggplot2)

penglings <- read.csv("penglings.csv")

ggplot(penglings, aes(flipper_length_mm, body_mass_g, color = species)) + geom_point(size=15, alpha = 0.8) + xlab("Flipper Length(mm)") + ylab("Body Mass(g)") + scale_color_manual(values=c('red', 'blue', 'orange'))