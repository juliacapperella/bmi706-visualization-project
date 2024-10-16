# bmi706-visualization-project

BMI 706: Visualization Project Dataset & Tasks
Group: Data Ducks
Members: Claire Chu, Julia Capperella

This visualization combines several datasets from the WHO Global Antimicrobial Resistance and Use Surveillance System (GLASS) that are part of the first global collaboration to standardize antimicrobial resistance (AMR) surveillance. GLASS contains epidemiological, clinical, and population-level data, collected through results from laboratory clinical specimens. GLASS-AMR provides information about a set of pathogens that cause common bacterial infections in humans. The data includes information from 2016 until 2022, and countries from all WHO regions are included. Furthermore, it incorporates other datasets which include information on Health Financing from WHO’s Global Health Observatory and information on GDP per country. The health financing datasets  include information about how much money each country is spending on health care relative to their GDP and general government spending.

The visualization was made to complete the following tasks:
- Linking bacterial pathogens to infectious syndrome and antibiotic names
- Comparing resistance of bacterial pathogens on the various antibiotics used to treat them
- Temporal reported BCI by year
- Geospatial AMR trend analysis: comparing bacterial pathogens/reported BCI and antibiotic use by country
- Global map of health financing proportionate to GDP
- Linking antimicrobial resistance to national-level health financing and GDP

The final dataset as seen in this repository has 16 variables, and the ones used to create this visualization are CountryTerritoryArea, BCIs per million population, Year, Infectious Syndrome, Bacterial Pathogen, Antibiotic Group, and gghed_gdp.

Altair, pandas, and streamlit were used to create this visualization.
