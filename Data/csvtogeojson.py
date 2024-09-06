import pandas as pd
import geojson
from geojson import Feature, FeatureCollection, Point

df = pd.read_csv('./5G_CSV/Vodafone.csv')
df.dropna(subset=['long', 'lat'], inplace=True)
# df.fillna({'radio': 'unknown', 'mcc': -1, 'mnc': -1, 'lac': -1, 'cid': -1, 'operator': 'unknown'}, inplace=True)

features = []

for _, row in df.iterrows():
    point = Point((row['long'], row['lat']))
    feature = Feature(geometry=point, properties={
        'city': row['city_name'],
        'operator': row['operator']
    })
    features.append(feature)
feature_collection = FeatureCollection(features)
with open('./5G_Geojson/5G_Vodafone.geojson', 'w') as f:
    geojson.dump(feature_collection, f)

print("GeoJSON file created successfully.")
