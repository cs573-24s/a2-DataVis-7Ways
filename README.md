# 02-DataVis-7ways

Assignment 2 - Data Visualization, 7 Ways  
===
CS573, Spring 2024

Prof. Lane Harrison

Andrew Kerekon

# Excel

Excel is a dedicated tool for graphing, and is widely used in the professional world.

Write a paragraph for each visualization tool you use. What was easy? Difficult? Where could you see the tool being useful in the future? Did you have to use any hacks or data manipulation to get the right chart?

To visualize the Penglings dataset, I utilized Excel's bubble chart feature to incorporate our three variables (flipper length, body mass, and bill length) across all three species (Adelie, Chinstrap, Gentoo). I expected this would be straightforward, as Excel is effectively a "little language" built for this purpose, but the process presented some surprising hiccups. For one, I first had to clean the data of unnecessary columns (island, bill depth, sex, and year) as well as invalid (NA) entries before Excel would allow points to be plotted. I then had to splice our y and "bubble size" columns (body mass and bill length) to separate columns underneath the three species to treat them as separate series. Once this was complete, factors such as adding labels to the chart were not straightforward, nor was changing the size of the bubbles to reflect bill length. I scaled bubble size to 25% and scaled them by width, rather than by area, to make the change more dramatic -- I also rounded each bill length to the nearest 10 to provide better differentiation between bubbles. I also changed transparency of each bubble to 20%, which was opposite my initial intuition (default appeared that 0% was fully visible, and 100% fully transparent). After all of these changes, Excel didn't appear to have the capacity to add legend labels for species nor a legend for the bill length bubble size, so I was not able to add these portions. Despite these setbacks, I could see this tool being useful for non-technical users to create effective visualizations without needing to program them manually.

![excel](img/excel.png)

## Technical Achievements
- 

## Design Achievements
- 
