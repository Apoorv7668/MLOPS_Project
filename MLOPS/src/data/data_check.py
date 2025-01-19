import os

# data_filepath = r"C:/Users/Dell/Downloads/archive (1)/water_potability.csv"
data_filepath = r"C:\Users\Dell\OneDrive\Pictures\water_potability.csv"
params_filepath = "params.yaml"

print(f"Data file exists: {os.path.exists(data_filepath)}")
print(f"Params file exists: {os.path.exists(params_filepath)}")
