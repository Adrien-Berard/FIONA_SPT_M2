import pandas as pd
import os

directory = "/home/enora/Téléchargements/RESULT"

# Loop through all files in the directory
for filename in os.listdir(directory):
    filepath = os.path.join(directory, filename)
    
    if os.path.isfile(filepath) and filename.endswith('.csv'):
        # Read the file using pandas
        df = pd.read_csv(filepath)
        
        # Create "t" column from "frame"
        df["t"] = df["frame"]
        
        # Drop the "frame" and "z" columns
        df.drop(columns=["frame","z"], inplace=True)
        
        # Define output filename with .trxyt extension
        output_filename = os.path.splitext(filename)[0] + ".trxyt"
        output_path = os.path.join(directory, output_filename)
        
        # Save without header and with tab separator
        df.to_csv(output_path, sep='\t', index=False, header=False)

