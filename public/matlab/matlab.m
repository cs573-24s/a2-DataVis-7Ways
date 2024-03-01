data = readtable('penglings.csv');

flipper_length_mm = data.flipper_length_mm;
body_mass_g = data.body_mass_g;
bill_length_mm = data.bill_length_mm;
species = string(data.species); 

uniqueSpecies = unique(species);

speciesColors = {'Adelie', [255, 144, 19]/255; 'Chinstrap', [153, 50, 204]/255; 'Gentoo', [0, 138, 139]/255};

figure;
set(gcf, 'Position', [100, 100, 1200, 600]); 

hold on; 

for i = 1:length(uniqueSpecies)
    idx = species == uniqueSpecies(i); 
    colorIdx = find(strcmp(speciesColors(:,1), uniqueSpecies(i)));
    scatter(flipper_length_mm(idx), body_mass_g(idx), bill_length_mm(idx)*10, ... 
        'filled', 'MarkerFaceColor', speciesColors{colorIdx, 2}, ...
        'DisplayName', uniqueSpecies(i), 'MarkerFaceAlpha', 0.5); 
end

legend(uniqueSpecies, 'Location', 'eastoutside');

xlabel('Flipper Length (mm)');
ylabel('Body Mass (g)');

xlim([min(flipper_length_mm)-10, max(flipper_length_mm)+10]);
ylim([min(body_mass_g)-500, max(body_mass_g)+500]);

hold off;
