import hijri_converter
import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv("input.csv")


# Define a function to check if a value is a valid Hijri date
def is_valid_hijri_date(date_value):
    try:
        hijri_converter.HijriDate(date_value)
        return True
    except ValueError:
        return False


# Apply the function to the "BRTHDAT" column and create a mask for incorrect formats
mask = ~df["BRTHDAT"].apply(is_valid_hijri_date)

# Filter the DataFrame to extract rows with incorrect format
incorrect_rows = df[mask]

# Print the rows with incorrect format
print(incorrect_rows)
