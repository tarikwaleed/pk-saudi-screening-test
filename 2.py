import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv("input.csv")

# Create a new column 'NIDNO_VALID' in the DataFrame
df["NIDNO_VALID"] = True

# Loop over the 'NIDNO' column
for i, cell in enumerate(df["NIDNO"]):
    if (
        not str(cell).isdigit()
        or len(str(cell)) != 10
        or str(cell)[0] not in ["1", "2"]
    ):
        df.loc[i, "NIDNO_VALID"] = True

# Save the modified DataFrame to output.csv
df.to_csv("output2.csv", index=False)
