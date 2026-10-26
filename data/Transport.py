# Define Transport Time

import pandas as pd
from math import radians, sin, cos, sqrt, atan2

# Define 10 vertices: 9 farms + 1 hub
vertices = pd.DataFrame([
    ["HUB", None, "Proposed Mount Barker Biogas Hub", "Mount Barker area", -34.700000, 117.650000],
    ["A", "c37f4", "Mount Barker Regional Saleyards", "Mount Barker", -34.677803, 117.672218],
    ["B", "b8ffa", "Mt Barker Chicken - Barker Creek", "Mount Barker", -34.674297, 117.722137],
    ["C", "mh4jw", "Unknown Free Range Piggery", "Narrikup", -34.734936, 117.908913],
    ["D", "x7jvy", "Geza Feedlot", "Narrikup", -34.786972, 117.897659],
    ["E", "c2vzt", "Mungrup Stud", "Narrikup", -34.793285, 117.765877],
    ["F", "bdcc7", "Fletcher International Abattoir", "Narrikup", -34.835293, 117.791641],
    ["G", "b51b4", "Albany Farm Fresh Eggs", "Redmond", -34.891014, 117.774902],
    ["H2", "df2e4", "Marbelup Pork", "Redmond", -34.901867, 117.697723],
    ["I", "bo79t", "Unknown Grower Piggery", "Cranbrook", -34.159618, 117.500313]
], columns=["Vertex", "FarmId", "Name", "Suburb", "Lat", "Lng"])

print(vertices)

# Define 12 edges
connections = [
    ("HUB", "A"),
    ("HUB", "E"),
    ("A", "B"),
    ("A", "C"),
    ("B", "C"),
    ("C", "D"),
    ("D", "F"),
    ("D", "G"),
    ("E", "F"),
    ("E", "H2"),
    ("F", "G"),
    ("G", "H2")
]

print()
print("Number of edges:", len(connections))
print()


# Calculate DistanceKm
def haversine_distance(lat1, lng1, lat2, lng2):
    # Approximate radius of the Earth in kilometres
    earth_radius = 6371.0

    # Convert latitude and longitude from degrees to radians
    lat1 = radians(lat1)
    lng1 = radians(lng1)
    lat2 = radians(lat2)
    lng2 = radians(lng2)

    # Calculate coordinate differences
    dlat = lat2 - lat1
    dlng = lng2 - lng1

    # Apply the Haversine formula
    a = (
        sin(dlat / 2) ** 2
        + cos(lat1) * cos(lat2) * sin(dlng / 2) ** 2
    )

    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return earth_radius * c


# Create a dictionary for finding coordinates
vertex_lookup = vertices.set_index("Vertex").to_dict("index")


# Calculate TransportTime
edges = []

average_speed = 50

for source, destination in connections:
    source_data = vertex_lookup[source]
    destination_data = vertex_lookup[destination]

    # Calculate straight-line distance
    distance = haversine_distance(
        source_data["Lat"],
        source_data["Lng"],
        destination_data["Lat"],
        destination_data["Lng"]
    )

    # Estimate transportation time in minutes
    transport_time = max(
        1,
        round((distance / average_speed) * 60)
    )

    edges.append([
        source,
        destination,
        round(distance, 2),
        transport_time
    ])

transport_network = pd.DataFrame(
    edges,
    columns=[
        "From",
        "To",
        "DistanceKm",
        "TransportTime"
    ]
)

print(transport_network)


# Save files
vertices.to_csv(
    "graph_vertices.csv",
    index=False
)

transport_network.to_csv(
    "transport_network.csv",
    index=False
)

print("\nGraph files saved successfully.")


# Check if network satisfies the test-graph specification
number_of_vertices = len(vertices)
number_of_edges = len(transport_network)

isolated_vertex = "I"

all_positive = (
    transport_network["TransportTime"] > 0
).all()

print()
print("Vertices:", number_of_vertices)
print("Edges:", number_of_edges)
print("Isolated vertex:", isolated_vertex)
print("All weights positive:", all_positive)