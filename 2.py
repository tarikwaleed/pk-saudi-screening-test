import pandas as pd

df = pd.read_csv("input.csv")

df["NIDNO_VALID"] = True

x = 0
y = 0

report_file = open("NIDNO_REPORT.txt", "w")

for i, cell in enumerate(df["NIDNO"]):
    cell_str = str(cell)
    if len(cell_str) != 10:
        x += 1
        df.loc[i, "NIDNO_VALID"] = False
    if not cell_str.startswith(("1", "2")):
        y += 1
        df.loc[i, "NIDNO_VALID"] = False

df.to_csv("output2.csv", index=False)

report_file.write(f"{x} numbers out of range\n")
report_file.write(f"{y} numbers don't begin with 1 or 2\n")

report_file.close()
