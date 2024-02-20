library(ggplot2)

df <- read.csv("https://raw.githubusercontent.com/aria-yan/a2-DataVis-7Ways/main/penglings.csv")

colors <- c("#fba044","#9933cb","#479f9f")

ggplot(df, aes(x=flipper_length_mm, y=body_mass_g, color=species, size=bill_length_mm)) + 
  geom_point(na.rm = TRUE, alpha=0.7) + 
  scale_color_manual(values = colors) +
  xlab("Flipper Length (mm)") +
  ylab("Body Mass (g)")

ggplot(df, aes(x=flipper_length_mm, y=body_mass_g, color=species, size=bill_length_mm)) + 
  geom_point(na.rm = TRUE, alpha=0.7) + 
  scale_color_manual(values = colors) +
  geom_smooth(method=lm) +
  xlab("Flipper Length (mm)") +
  ylab("Body Mass (g)")

ggplot(df, aes(x=flipper_length_mm, y=body_mass_g, color=species, size=bill_length_mm)) + 
  geom_point(na.rm = TRUE, alpha=0.7) + 
  scale_color_manual(values = colors) +
  geom_smooth(method=lm, se=FALSE, fullrange=TRUE)
  xlab("Flipper Length (mm)") +
  ylab("Body Mass (g)")
