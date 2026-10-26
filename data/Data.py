# Data preparation: Choose the data of appropriate area

import pandas as pd
import matplotlib.pyplot as plt

# # Extract WA dataset from the original dataset
# input_file = "All facilities in Australia.csv"
# output_file = "western_australia_farms.csv"

# df = pd.read_csv(input_file)

# # Remove leading/trailing spaces
# df["State"] = df["State"].astype(str).str.strip()

# # Select Western Australia
# wa_df = df[df["State"].str.upper() == "WA"].copy()

# # Save the filtered dataset
# wa_df.to_csv(output_file, index=False)

# print("Original records:", len(df))
# print("Western Australia records:", len(wa_df))
# print("Saved to:", output_file)


# df = pd.read_csv("western_australia_farms.csv")

# # Create geographic grid cells
# df["LatGrid"] = (df["Lat"] // 1).astype(int)
# df["LngGrid"] = (df["Lng"] // 1).astype(int)

# # Count farms in each grid cell
# grid_summary = (
#     df.groupby(["LatGrid", "LngGrid"])
#       .size()
#       .reset_index(name="FarmCount")
#       .sort_values("FarmCount", ascending=False)
# )

# print(grid_summary.head(30))


# # Extract South West WA dataset
# df = pd.read_csv("western_australia_farms.csv")

# # Define an initial bounding box for the selected region
# south_west = df[
#     (df["Lat"] >= -35) &
#     (df["Lat"] <= -31) &
#     (df["Lng"] >= 114) &
#     (df["Lng"] <= 118)
# ].copy()

# print("South West candidate farms:", len(south_west))

# print("\nSuburb distribution:")
# print(south_west["Suburb"].value_counts().head(30))

# # Save the candidate dataset
# south_west.to_csv("south_west_wa_candidate.csv", index=False)


# # Choose a appropriate data size within the South West WA 
# df = pd.read_csv("south_west_wa_candidate.csv")

# # Create 1-degree geographic grid cells
# df["LatGrid"] = (df["Lat"] // 1).astype(int)
# df["LngGrid"] = (df["Lng"] // 1).astype(int)

# # Count farms in each grid cell
# grid_summary = (
#     df.groupby(["LatGrid", "LngGrid"])
#       .size()
#       .reset_index(name="FarmCount")
#       .sort_values("FarmCount", ascending=False)
# )

# print(grid_summary.to_string(index=False))


# study area: -35 ≤ Latitude < -33 and 117 ≤ Longitude < 118
df = pd.read_csv("western_australia_farms.csv")

# Define an initial study area in the southern Great Southern region
selected_df = df[
    (df["Lat"] >= -35) &
    (df["Lat"] < -33) &
    (df["Lng"] >= 117) &
    (df["Lng"] < 118)
].copy()

# print("Selected farms:", len(selected_df))

# print("\nSuburb distribution:")
# print(selected_df["Suburb"].value_counts())

# print("\nPostcode distribution:")
# print(selected_df["Postcode"].value_counts())


# # Check if it's continuous space distribution 
# # Scatter plot
# plt.figure(figsize=(10, 8))

# plt.scatter(
#     selected_df["Lng"],
#     selected_df["Lat"],
#     s=30
# )

# # Latitude and Longitude distribution
# plt.xlabel("Longitude")
# plt.ylabel("Latitude")
# plt.title("Selected Farm Locations in the Study Area")
# plt.grid(True)

# plt.show()

# print(
#     selected_df[
#         ["Id", "Name", "Suburb", "Lat", "Lng"]
#     ].sort_values("Lat")
# )

# Save file
selected_df.to_csv(
    "selected_southern_wa_farms.csv",
    index=False
)

print("Saved selected dataset.")
print("Number of farms:", len(selected_df))


candidate_suburbs = [
    "Mount Barker",
    "Narrikup",
    "Cranbrook",
    "Kendenup",
    "Porongurup",
    "Redmond"
]

candidates = selected_df[
    selected_df["Suburb"].isin(candidate_suburbs)
][
    ["Id", "Name", "Suburb", "Lat", "Lng"]
].copy()

print(candidates.to_string(index=False))