% Load the penguin data
data = readtable('penglings.csv');

% Extract relevant columns
flipper_length_mm = data.flipper_length_mm;
body_mass_g = data.body_mass_g;
species = data.species;
bill_length_mm = data.bill_length_mm;

% Create a custom color map with vibrant and darker colors
color_map = [
    0.95, 0.25, 0.15;  % Red
    0.00, 0.50, 0.85;  % Blue
    0.00, 0.70, 0.30;  % Green
    1.00, 0.65, 0.00;  % Orange
    0.75, 0.25, 0.90   % Purple
];

% Map species to colors
species_unique = unique(species);
color_idx = arrayfun(@(x) find(strcmp(species_unique, x)), species);
color = color_map(color_idx, :);

% Define transparency level (e.g., 0.6 means 60% transparency)
transparency = 0.6;

% Create the scatterplot with transparency and a black border
scatter(flipper_length_mm, body_mass_g, 100, color, 'filled', 'MarkerEdgeColor', 'k', 'MarkerFaceAlpha', transparency);
hold on;

% Set axis labels and title
xlabel('Flipper Length (mm)', 'FontName', 'Times New Roman');
ylabel('Body Mass (g)', 'FontName', 'Times New Roman');
title('Diving into Penguin Metrics', 'FontName', 'Times New Roman', 'FontSize', 17, 'FontAngle', 'italic');

% Set axis limits
xlim([170, 240]);
ylim([2000, 7000]);

set(gca, 'FontName', 'Times New Roman');

% Preallocate legend_handles array
legend_handles = gobjects(1, length(species_unique));
for i = 1:length(species_unique)
    legend_handles(i) = scatter(nan, nan, 100, color_map(i, :), 'filled', 'DisplayName', species_unique{i}, 'MarkerEdgeColor', 'k', 'MarkerFaceAlpha', transparency);
end

% Create the legend in the 'Best' location
legend(legend_handles, 'Location', 'southeast', 'FontName', 'Times New Roman');

% Load the background image
bg_image = imread('background.jpg'); 
% Flip the image
bg_image = flipud(bg_image);
% Display image as a background
bg = imagesc([170, 240], [2000, 7000], bg_image);
alpha(bg, 0.6); % Set transparency level (0.6 means 60% transparency)
% Move image to the back
uistack(bg, 'bottom');

% Create caption text
captionText = {
    'This visualization shows the morphological measurements of 3 penguin species,';
    'Adelie, Gentoo, and Chinstrap, from 3 different islands (Torgersen, Biscoe, Dream)';
    'over the years 2007, 2008, and 2009.'
};

% Convert the text to a single string with line breaks
captionText = strjoin(captionText, '\n');

% Create a text box annotation at the top-center of the plot with a margin and left justification
annotation('textbox', [0.15, 0.83, 0.5, 0.1], 'String', captionText, ...
    'FontName', 'Times New Roman', 'FontSize', 10, 'FontWeight', 'bold', 'HorizontalAlignment', 'left', ...
    'LineStyle', 'none', 'Interpreter', 'tex');

% Show plot
hold off;

