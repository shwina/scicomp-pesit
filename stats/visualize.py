import pandas as pd

cell = pd.read_csv('cellphoneper100.csv', encoding='utf-8')
gdp = pd.read_csv('gdppercapita_with_projections.csv', encoding='utf-8')
dem = pd.read_csv('indicatorpolityiv.csv', encoding='utf-8')

cell = cell.set_index('Country')
gdp = gdp.set_index('Country')
dem = dem.set_index('Country')

countries = ['France', 'Germany', 'Australia', 'Egypt', 'Sweden', 'India', 'Greece', 'China', 'Nigeria', 'Netherlands']
years = range(2000, 2010)
years = [str(year) for year in years]

cell_dat = cell.loc[countries, years]
gdp_dat = gdp.loc[countries, years]
dem_dat = dem.loc[countries, years]




	
