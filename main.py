import pandas as pd
from convex_hull_builder import ConvexHullBuilder

# Поменяйте путь на свой
PATH_TO_SAVE = "C:\\Users\\ADMIN\\pythonProject\\kzn_districts_map\\kzn_districts_map_template\\data.csv"

points_df = pd.read_csv("kzn_districts_map_template\points.csv")

builder = ConvexHullBuilder(points_df)

result_df = builder.get_convex_hull()

result_df.to_csv(PATH_TO_SAVE, index=False)