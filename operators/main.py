# Do not modify these lines
__winc_id__ = 'd0d3cdcefbb54bc980f443c04ab3a9eb'
__human_name__ = 'operators'

# Add your code after this line
spoken_language_switzerland = 'German' 
spoken_language_spain = 'Spanish'
print(spoken_language_switzerland == spoken_language_spain)

switzerland_religion = 'Roman Catholic'
spain_religion = 'Roman Catholic'
print(switzerland_religion == spain_religion)

spain_capital = 'Madrid'
switzerland_capital = 'bern'
print(len(spain_capital) != len(switzerland_capital))

spain_gpd = 1715
switzerland_gpd = 590.7
print(switzerland_gpd > spain_gpd)

switzerland_population_growth = -0.03
spain_population_growth = 0.65
print(switzerland_population_growth and spain_population_growth < 1)

switzerland_population_count = 47.3
spain_population_count = 8.5
print(switzerland_population_count > 10 or spain_population_count > 10)
print((switzerland_population_count > 10 or spain_population_count > 10) == 1)
