import pandas as pd
from hijridate import Hijri

# Read the CSV file into a DataFrame
df = pd.read_csv("input.csv")

# Create a new column 'valid' in the DataFrame
df["BRTHDAT_VALID"] = True

# Loop over the 'birthdate' column
x=0
y=0
report_file = open("BRTHDAT_REPORT.txt", "w")
for i, cell in enumerate(df["BRTHDAT"]):
    try:
        # Convert the cell value to Hijri date
        cell_str = str(cell)
        year = int(cell_str[:4])
        month = int(cell_str[4:6])
        day = int(cell_str[6:8])
        Hijri(year, month, day, validate=True)
    except OverflowError:
        x += 1
        df.loc[i, "BRTHDAT_VALID"] = False
    except ValueError:
        y += 1
        df.loc[i, "BRTHDAT_VALID"] = False

# Save the modified DataFrame to output.csv
df.to_csv("output1.csv", index=False)

report_file.write(f"Gregorian Date: {x} Fields\n")
report_file.write(f"Invalid Hijri Dates: {y} Fields\n")
report_file.close()
