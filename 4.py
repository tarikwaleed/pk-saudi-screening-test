import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv("input.csv")

# Create a new column 'VACDAYS_VALID' in the DataFrame
df["VACDAYS_VALID"] = True

# Initialize counters
x = 0
y = 0

# Open the report file for writing
report_file = open("VACDAYS_REPORT.txt", "w")

# Loop over the 'VACDAYS' column
for i, cell in enumerate(df["VACDAYS"]):
    if pd.isnull(cell):
        x += 1
        df.loc[i, "VACDAYS_VALID"] = False
    elif cell < 0:
        y += 1
        df.loc[i, "VACDAYS_VALID"] = False

# Save the modified DataFrame to output.csv
df.to_csv("output2.csv", index=False)

# Write the content to the report file
report_file.write(f"Number of empty cells: {x}\n")
report_file.write(f"Number of negative cells: {y}\n")

# Close the report file
report_file.close()
