r = getOption("repos")
r["CRAN"] = "http://cran.us.r-project.org"
options(repos = r)

library(palmerpenguins)

plot(penguins$flipper_length_mm, penguins$body_mass_g, 
     col = c("darkorange", "darkorchid", "cyan4")[penguins$species],
     pch = c(16, 17, 15),
     cex=penguins$bill_length_mm/30,
     xlab = "Flipper Length (mm)",
     ylab = "Body Mass (g)")
