import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv("input.csv")

# Create a new column 'VACDAYS_VALID' in the DataFrame
df["VACDAYS_VALID"] = True

# Loop over the 'VACDAYS' column
for i, cell in enumerate(df["VACDAYS"]):
    if pd.isnull(cell) or cell < 0:
        df.loc[i, "VACDAYS_VALID"] = False

# Save the modified DataFrame to output.csv
df.to_csv("output4.csv", index=False)
