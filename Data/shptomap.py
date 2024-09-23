# import geopandas as gpd
# import matplotlib.pyplot as plt


# shapefile_path = './delhi3road_geojson/delhi3.geojson'
# gdf = gpd.read_file(shapefile_path)
# print(gdf.info())
# print(gdf.head())
# unique_highways = gdf['highway'].unique()
# print(unique_highways)
# highway_counts = gdf['highway'].value_counts()


# import geopandas as gpd
# shapefile_path = '../delhi3road_geojson/delhi3.geojson'
# df = gpd.read_file(shapefile_path)
# print(df.info())
# print(df.head())
# highway_properties = [
#     'residential','living_street'
# ]
# filtered_gdf = df[df['highway'].isin(highway_properties)]
# output_file_path = '../delhi3road_geojson/residential.geojson'
# filtered_gdf.to_file(output_file_path, driver='GeoJSON')


import geopandas as gpd
from shapely.geometry import box, Polygon
import pandas as pd
import folium 
from folium.plugins import MarkerCluster

# corr_df=pd.read_csv("4G_highway_presence.csv")
# correlation_value = corr_df['highway_present'].corr(corr_df['cell_tower_present'])
# correlation_value = f"{correlation_value:.3f}"
# print(correlation_value)

# # Define the Delhi clipping boundary as a Polygon
# delhi_boundary = Polygon([[76.84, 28.4], [76.84, 28.88], [77.35, 28.88], [77.35, 28.4], [76.84, 28.4]])

# # Convert the boundary to a GeoDataFrame
# boundary_gdf = gpd.GeoDataFrame(geometry=[delhi_boundary], crs="EPSG:4326")
# print(boundary_gdf)

# # Load the GeoJSON files
# highways_gdf = gpd.read_file("../delhi3road_geojson/highway.geojson")
# cell_towers_gdf = gpd.read_file("../delhitowers/4G.geojson")

# # Set the coordinate reference system (CRS) to a projected CRS for distance calculations
# highways_gdf = highways_gdf.to_crs(epsg=32643)  # UTM zone 43N for Delhi
# cell_towers_gdf = cell_towers_gdf.to_crs(epsg=32643)
# boundary_gdf = boundary_gdf.to_crs(epsg=32643)

# # Get the bounds of the Delhi boundary
# minx, miny, maxx, maxy = boundary_gdf.total_bounds
# print (minx, miny, maxx, maxy)

# # Generate a 1km by 1km grid within the boundary
# grid_cells = []
# grid_size = 1000  # 1km

# x_start = minx
# while x_start < maxx:
#     y_start = miny
#     while y_start < maxy:
#         cell = box(x_start, y_start, x_start + grid_size, y_start + grid_size)
#         # Check if the cell intersects with the Delhi boundary and add it to the grid
#         if cell.intersects(boundary_gdf.geometry[0]):
#             grid_cells.append(cell)
#         y_start += grid_size
#     x_start += grid_size

# # Create a GeoDataFrame for the grid
# grid_gdf = gpd.GeoDataFrame(grid_cells, columns=['geometry'], crs=highways_gdf.crs)
# print(grid_gdf)

# # Check for the presence of highways and cell towers in each grid cell
# def check_presence(grid, gdf):
#     return gdf.intersects(grid).any()

# # Create a list to store the data for each grid cell
# data = []

# for cell in grid_gdf.geometry:
#     highway_present = int(check_presence(cell, highways_gdf))
#     cell_tower_present = int(check_presence(cell, cell_towers_gdf))
#     data.append({'geometry': cell, 'highway_present': highway_present, 'cell_tower_present': cell_tower_present})

# # Convert to a GeoDataFrame
# result_gdf = gpd.GeoDataFrame(data, crs=highways_gdf.crs)

# # Drop the geometry column and export to CSV
# result_df = result_gdf.drop(columns=['geometry'])
# result_df.reset_index(drop=True, inplace=True)
# result_df.index = result_df.index + 1
# result_df.to_csv("../Data/4G_highway_presence.csv",index_label='Index')

# print("CSV file created: grid_highway_cell_tower_presence.csv")


# delhi_boundary = Polygon([[76.84, 28.4], [76.84, 28.88], [77.35, 28.88], [77.35, 28.4], [76.84, 28.4]])
# boundary_gdf = gpd.GeoDataFrame(geometry=[delhi_boundary], crs="EPSG:4326")
# boundary_gdf = boundary_gdf.to_crs(epsg=32643)
# highways_gdf = gpd.read_file("../delhi3road_geojson/highway.geojson")
# cell_towers_gdf = gpd.read_file("../delhitowers/4G.geojson")
# highways_gdf = highways_gdf.to_crs(epsg=32643)
# cell_towers_gdf = cell_towers_gdf.to_crs(epsg=32643)
# minx, miny, maxx, maxy = boundary_gdf.total_bounds
# grid_cells = []
# grid_size = 1000  # 1km in meters
# x_start = minx
# grid_id = 1
# while x_start < maxx:
#     y_start = miny
#     while y_start < maxy:
#         cell = box(x_start, y_start, x_start + grid_size, y_start + grid_size)
#         if cell.intersects(boundary_gdf.geometry[0]):
#             grid_cells.append((grid_id, cell))
#             grid_id += 1
#         y_start += grid_size
#     x_start += grid_size
# grid_gdf = gpd.GeoDataFrame(grid_cells, columns=['id', 'geometry'], crs=boundary_gdf.crs)
# grid_gdf = grid_gdf.to_crs(epsg=4326)
# highways_gdf = highways_gdf.to_crs(epsg=4326)
# cell_towers_gdf = cell_towers_gdf.to_crs(epsg=4326)
# m = folium.Map(location=[28.6139, 77.2090], zoom_start=10)
# for _, row in grid_gdf.iterrows():
#     geo_json = gpd.GeoSeries(row['geometry']).to_json()
#     folium.GeoJson(
#         geo_json,
#         style_function=lambda x: {
#             'fillColor': 'none',
#             'color': 'blue',
#             'weight': 1
#         },
#         popup=folium.Popup(f"Grid Number: {row['id']}", parse_html=True)
#     ).add_to(m)

# folium.GeoJson(highways_gdf.to_json(), style_function=lambda x: {
#     'color': 'red',
#     'weight': 2
# }).add_to(m)
# marker_cluster = MarkerCluster()
# for _, row in cell_towers_gdf.iterrows():
#     folium.Marker(location=[row.geometry.y, row.geometry.x],
#         popup=f"Cell Tower",
#         icon=folium.Icon(color='green', icon='info-sign')).add_to(marker_cluster)
# marker_cluster.add_to(m)
# folium.GeoJson(boundary_gdf.to_crs(epsg=4326), style_function=lambda x: {
#     'fillColor': 'none',
#     'color': 'black',
#     'weight': 2
# }).add_to(m)
# m.save("../static/4G_highways.html")  # Save HTML file in the static folder
    



# import geopandas as gpd
# from shapely.ops import nearest_points
# import plotly.graph_objects as go
# import numpy as np
# import plotly.io as pio

# # Step 1: Load the GeoJSON files
# highways = gpd.read_file("/kaggle/input/a1-data82/celltowers/delhi3road_geojson/residential.geojson")
# cell_towers = gpd.read_file("/kaggle/input/a1-data82/celltowers/delhitowers/3G.geojson")

# # Step 2: Reproject both layers to a projected CRS (e.g., UTM zone 43N for Delhi, EPSG:32643)
# projected_crs = 'EPSG:32643'  # UTM zone 43N (you can adjust based on your location)

# highways = highways.to_crs(projected_crs)
# cell_towers = cell_towers.to_crs(projected_crs)

# # Step 3: Calculate shortest distance from each cell tower to the nearest highway
# distances = []
# for cell_tower in cell_towers.geometry:
#     # Calculate the distance to the nearest highway
#     nearest_highway = highways.distance(cell_tower).min()
#     distances.append(nearest_highway)

# # Convert distances to kilometers (since the CRS is in meters)
# distances_km = np.array(distances) / 1000.0  # Convert from meters to kilometers
# print("hello1")
# # Step 4: Create bins (e.g., <1km, <2km, <3km, etc.)
# bins = np.arange(0, np.max(distances_km) + 0.25, 0.25)  # Bins from 0 to the max distance in increments of 1km

# # Step 5: Calculate the CDF
# hist, bin_edges = np.histogram(distances_km, bins=bins, density=False)
# cdf = np.cumsum(hist) / len(distances_km)

# fig = go.Figure()

# # Add trace for CDF line
# fig.add_trace(go.Scatter(
#     x=bin_edges[1:],  # Exclude the leftmost bin edge
#     y=cdf,
#     mode='lines+markers',
#     marker=dict(color='blue'),
#     line=dict(shape='linear'),
#     name='CDF',
#     hovertemplate='<b>Distance: %{x:.2f} km</b><br>Cumulative Probability: %{y:.5f}<extra></extra>',
# ))

# # Add titles and labels
# fig.update_layout(
#     title='Cumulative Distribution Function (CDF) of Distances from Cell Towers to Roads',
#     xaxis_title='Distance (km)',
#     yaxis_title='Cumulative Probability',
#     xaxis=dict(
#         tickvals=np.arange(0, np.max(bin_edges[1:]) + 0.50, 0.50),  
#         ticktext=[f"{v}" for v in np.arange(0, np.max(bin_edges[1:]) + 0.50,0.50)]  
#     ),
#     hovermode='closest',
#     template='plotly_white',
#     width=900,
#     height=600,
#     showlegend=False
# )
# pio.write_html(fig, file='/kaggle/working/3G_residential_cdf.html', auto_open=False)
# # Show plot
# fig.show() 

import geopandas as gpd
from shapely.geometry import Point
from shapely.ops import nearest_points
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.io as pio

# Load GeoJSON files for highways and cell towers
highways = gpd.read_file('../delhi3road_geojson/highway.geojson')  # LineString geometries
cell_towers = gpd.read_file('../delhitowers/4G.geojson')  # Point geometries

projected_crs = 'EPSG:32643'  # UTM zone 43N (you can adjust based on your location)
highways = highways.to_crs(projected_crs)
cell_towers = cell_towers.to_crs(projected_crs)

# Ensure both datasets are in the same CRS (coordinate reference system)
# cell_towers = cell_towers.to_crs(highways.crs)

# Build a spatial index for highways to speed up the nearest-neighbor search
highway_sindex = highways.sindex

# Function to calculate the minimum distance from a cell tower to the nearest highway using spatial indexing
def min_distance_to_highway(cell_tower, highways, sindex):
    # Get the bounding box of the cell tower to limit the search area
    possible_matches_index = list(sindex.intersection(cell_tower.bounds))
    possible_matches = highways.iloc[possible_matches_index]
    
    # If no possible matches are found, return np.nan (or you can return a large number like float('inf'))
    if possible_matches.empty:
        return np.nan  # No matches found, return NaN to handle later
    
    # Calculate distances between the cell tower and the possible nearby highways
    distances = possible_matches.geometry.apply(lambda highway: cell_tower.distance(highway))
    # print(distances.head())
    # Return the minimum distance (a float), handling any NaN values
    print(distances.min())
    return distances.min()

# Apply the min_distance_to_highway function for each cell tower
distances = cell_towers.geometry.apply(lambda tower: min_distance_to_highway(tower, highways, highway_sindex))
print(distances) 
distances = np.array(distances) / 1000.0
distances = distances[~np.isnan(distances)]
# Create distance intervals (bins) for CDF
distance_bins = np.arange(0, np.max(distances)+0.25, 0.25)  # From 0 to 5000 meters in steps of 500 meters
hist, bin_edges = np.histogram(distances, bins=distance_bins, density=False)

cdf = np.cumsum(hist) / len(distances)

fig = go.Figure()

# Add trace for the CDF line
fig.add_trace(go.Scatter(
    x=bin_edges[1:],  # Exclude the leftmost bin edge
    y=cdf,
    mode='lines+markers',
    marker=dict(color='blue'),
    line=dict(shape='linear'),
    name='CDF',
    hovertemplate='<b>Distance: %{x:.2f} km</b><br>Cumulative Probability: %{y:.5f}<extra></extra>',
))

# Add titles and labels
fig.update_layout(
    title='Cumulative Distribution Function (CDF) of Distances from Cell Towers to Roads',
    xaxis_title='Distance (km)',
    yaxis_title='Cumulative Probability',
    xaxis=dict(
        tickvals=np.arange(0, np.max(bin_edges[1:]) + 0.50, 0.50),  # Tick every 0.25 km (250m)
        ticktext=[f"{v}" for v in np.arange(0, np.max(bin_edges[1:]) + 0.50,0.50)]  # Show as meters
    ),
    hovermode='closest',
    template='plotly_white',
    width=900,
    height=600,
    showlegend=False
)

# Step 8: Save the plot as an HTML file
pio.write_html(fig, file='../static/4G_highway_cdf.html', auto_open=False)

# Show the plot
fig.show()


# import geopandas as gpd
# from shapely.geometry import Point
# from rtree import index
# import numpy as np
# import plotly.graph_objects as go
# import plotly.io as pio

# # Step 1: Load the GeoJSON files
# highways = gpd.read_file("../delhi3road_geojson/highway.geojson")
# cell_towers = gpd.read_file("../delhitowers/3G.geojson")

# # Step 2: Reproject both layers to a projected CRS (e.g., UTM zone 43N for Delhi, EPSG:32643)
# projected_crs = 'EPSG:32643'  # UTM zone 43N (you can adjust based on your location)
# highways = highways.to_crs(projected_crs)
# cell_towers = cell_towers.to_crs(projected_crs)

# # Step 3: Create an R-tree spatial index for the highways
# highway_idx = index.Index()
# for i, highway in enumerate(highways.geometry):
#     highway_idx.insert(i, highway.bounds)

# # Step 4: Calculate shortest distance from each cell tower to the nearest highway using spatial index
# distances = []
# for cell_tower in cell_towers.geometry:
#     # Find the nearest highway using the R-tree spatial index
#     nearest_highway_id = list(highway_idx.nearest(cell_tower.bounds, 1))[0]
#     print(nearest_highway_id)
#     nearest_highway = highways.geometry.iloc[nearest_highway_id]

#     # Calculate the distance to the nearest highway
#     distance = cell_tower.distance(nearest_highway)
#     distances.append(distance)

# # Convert distances to kilometers (since the CRS is in meters)
# distances_km = np.array(distances) / 1000.0  # Convert from meters to kilometers

# # Step 5: Create bins (e.g., <1km, <2km, <3km, etc.)
# bins = np.arange(0, np.max(distances_km) + 0.25, 0.25)  # Bins from 0 to the max distance in increments of 0.5km
# print(np.max(distances_km))
# # Step 6: Calculate the CDF
# hist, bin_edges = np.histogram(distances_km, bins=bins, density=False)
# cdf = np.cumsum(hist) / len(distances_km)
# print(len(distances_km))
# print(hist)
# print(bin_edges)
# print(cdf)

# # Step 7: Create a Plotly figure for the CDF
# fig = go.Figure()

# # Add trace for the CDF line
# fig.add_trace(go.Scatter(
#     x=bin_edges[1:],  # Exclude the leftmost bin edge
#     y=cdf,
#     mode='lines+markers',
#     marker=dict(color='blue'),
#     line=dict(shape='linear'),
#     name='CDF',
#     hovertemplate='<b>Distance: %{x:.2f} km</b><br>Cumulative Probability: %{y:.5f}<extra></extra>',
# ))

# # Add titles and labels
# fig.update_layout(
#     title='Cumulative Distribution Function (CDF) of Distances from Cell Towers to Roads',
#     xaxis_title='Distance (km)',
#     yaxis_title='Cumulative Probability',
#     xaxis=dict(
#         tickvals=np.arange(0, np.max(bin_edges[1:]) + 0.50, 0.50),  # Tick every 0.25 km (250m)
#         ticktext=[f"{v}" for v in np.arange(0, np.max(bin_edges[1:]) + 0.50,0.50)]  # Show as meters
#     ),
#     hovermode='closest',
#     template='plotly_white',
#     width=900,
#     height=600,
#     showlegend=False
# )

# # Step 8: Save the plot as an HTML file
# pio.write_html(fig, file='../static/4G_highway_cdf.html', auto_open=False)

# # Show the plot
# fig.show()







# gdf = gpd.read_file('./delhi3road_geojson/delhi3.geojson')
# fig, ax = plt.subplots(figsize=(10, 10))
# gdf.plot(ax=ax)
# plt.savefig('figure-2.png', dpi=300)
# plt.show()


# import pandas as pd
# import geopandas as gpd
# from shapely.geometry import box, Polygon,Point
# file_1='../5G_CSV/india.csv'
# file_2='../delhitowers/5G.geojson'
# delhi_boundary = Polygon([[76.84, 28.4], [76.84, 28.88], [77.35, 28.88], [77.35, 28.4], [76.84, 28.4]])
# df = pd.read_csv(file_1)

# # Create a GeoDataFrame from the DataFrame
# # Assuming the CSV file has columns 'lat' and 'long'
# geometry = [Point(xy) for xy in zip(df['long'], df['lat'])]
# gdf = gpd.GeoDataFrame(df, geometry=geometry)

# # Set the coordinate reference system (CRS) to WGS84
# gdf.crs = 'EPSG:4326'

# # Filter the rows that are within the Delhi boundary
# gdf_within_boundary = gdf[gdf.geometry.within(delhi_boundary)]

# # Convert the filtered GeoDataFrame to GeoJSON
# gdf_within_boundary.to_file(file_2, driver='GeoJSON')




