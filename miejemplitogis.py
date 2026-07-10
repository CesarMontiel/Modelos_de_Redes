import math
import math

import pandas as pd  # Importing pandas for Excel generation

def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Radius of the Earth in kilometers
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat / 2) ** 2 +
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2)
    c = 2 * math.asin(math.sqrt(a))
    return R * c  # Distance in kilometers

def find_nearest_point(target_point, points):
    nearest_point = None
    min_distance = float('inf')
    
    for point in points:
        distance = haversine(target_point[0], target_point[1], point[0], point[1])
        if distance < min_distance:
            min_distance = distance
            nearest_point = point
            
    return nearest_point, min_distance

# Updated example coordinates (latitude, longitude) with city names
target_points = [
    (40.7128, -74.0060, "New York City"),
    (34.0522, -118.2437, "Los Angeles"),
    (41.8781, -87.6298, "Chicago"),
    (51.5074, -0.1278, "London"),
    (48.8566, 2.3522, "Paris"),
    (35.6895, 139.6917, "Tokyo"),
    (55.7558, 37.6173, "Moscow"),
    (39.9042, 116.4074, "Beijing"),
    (-33.4489, -70.6693, "Santiago"),
    (-23.5505, -46.6333, "São Paulo"),
    (1.3521, 103.8198, "Singapore"),
    (52.5200, 13.4050, "Berlin"),
    (37.7749, -122.4194, "San Francisco"),
    (41.9028, 12.4964, "Rome"),
    (55.6761, 12.5683, "Copenhagen"),
    (19.4326, -99.1332, "Mexico City"),
]

# Updated points list with city names
points = [
    (34.0522, -118.2437, "Los Angeles"),
    (41.8781, -87.6298, "Chicago"),
    (51.5074, -0.1278, "London"),
    (48.8566, 2.3522, "Paris"),
    (35.6895, 139.6917, "Tokyo"),
    (55.7558, 37.6173, "Moscow"),
    (39.9042, 116.4074, "Beijing"),
    (-33.4489, -70.6693, "Santiago"),
    (-23.5505, -46.6333, "São Paulo"),
    (1.3521, 103.8198, "Singapore"),
]

# Finding the nearest point for each target point
results = []
for target_point in target_points:
    nearest_point, distance = find_nearest_point(target_point, points)
    results.append({
        "Target City": target_point[2],
        "Nearest City": nearest_point[2],
        "Distance (km)": distance
    })

# Creating a DataFrame and saving to Excel
df = pd.DataFrame(results)
df.to_excel("nearest_points.xlsx", index=False)

print("Results saved to nearest_points.xlsx")
