import geopandas as gpd
from shapely import wkt
import json

# Load your GeoJSON file
geojson_file = 'INDIAN_SUB_DISTRICTS.geojson'  

# Read GeoJSON file into a GeoDataFrame
gdf = gpd.read_file(geojson_file)

# Define the path for the output shapefile
shapefile_path = 'sub_districts.shp'  # Replace with your desired shapefile path

# Save the GeoDataFrame to a shapefile
gdf.to_file(shapefile_path, driver='ESRI Shapefile')
