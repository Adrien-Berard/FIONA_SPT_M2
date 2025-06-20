import pandas as pd
import os

directory = "/home/adrien/RESULT-crop/RESULT/Rn100nm"

# Loop through all files in the directory
for filename in os.listdir(directory):
    filepath = os.path.join(directory, filename)

    if os.path.isfile(filepath) and filename.endswith('.trxyt'):
        # Read tab-delimited .trxyt file with correct column order
        df = pd.read_csv(filepath, sep='\t', header=None, names=["traj_idx", "x", "y", "frame"])

        # Reorder columns and add z=0
        df = df[["traj_idx", "frame", "x", "y"]]
        df["z"] = 0.00000
        # Ensure 'frame' is integer
        df["frame"] = df["frame"].astype(int)
        # Define output filename with .csv extension
        output_filename = os.path.splitext(filename)[0] + ".csv"
        output_path = os.path.join(directory, output_filename)

        # Write CSV with comma delimiter, headers, no index
        df.to_csv(output_path, index=False)
