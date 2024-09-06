
# import pandas as pd
# df=pd.read_csv('./5G_Number_of_cell_towers_csv/5G_Vodafone.csv')
# count=0
# for _,row in df.iterrows():
#     count+=row['number_of_cell_towers']

# print(count)


# import geopandas as gpd
# import pandas as pd
# subdistricts = gpd.read_file('INDIAN_SUB_DISTRICTS.geojson')
# cell_towers = gpd.read_file('./5G_Geojson/5G_Vodafone.geojson')
# joined = gpd.sjoin(cell_towers, subdistricts, how="inner", predicate="within")
# tower_counts = joined.groupby(['sdtname', 'dtname', 'stname']).size().reset_index(name='number_of_cell_towers')
# tower_counts['sdtname'] = tower_counts['sdtname'].str.strip()
# tower_counts = tower_counts[tower_counts['sdtname'] != ""]
# tower_counts.to_csv('./5G_Number_of_cell_towers_csv/5G_Vodafone.csv', index=False)
# print("CSV file has been created successfully.")


import geopandas as gpd
import pandas as pd

# Load the subdistricts GeoJSON file
subdistricts = gpd.read_file('INDIAN_SUB_DISTRICTS.geojson')

# Load the CSV file with the number of cell towers
tower_counts = pd.read_csv('./3G_Number_of_cell_towers_csv/3G_Airtel.csv')

# Merge the GeoDataFrame with the DataFrame on subdistrict name
merged = subdistricts.merge(tower_counts, left_on='sdtname', right_on='sdtname', how='left')

# Save the merged data as a new GeoJSON file
merged.to_file('./3G_Number_of_cell_towers_geojson/3G_Airtel.geojson', driver='GeoJSON')

print("Merged GeoJSON file has been created successfully.")


