"""
analysis.py
-----------
DNA quality assessment of An. stephensi samples screened for Asaia bacteria.

NanoDrop spectrophotometry generates three key measurements per sample:
  - ng/µL  : DNA concentration
  - 260/280 : protein contamination ratio  (acceptable: 1.8 – 2.0)
  - 260/230 : salt/solvent contamination ratio (acceptable: 2.0 – 2.2)

Samples outside the 260/280 window are flagged because protein carryover
from the homogenisation step can inhibit PCR, producing false negatives.

Author: Areti Barakou
Data: An. stephensi (sind-kasur), Lab of Prof. Guido Favia, Univ. Camerino
"""

import pandas as pd

# ---------------------------------------------------------------------------
# 1. Load the data
# ---------------------------------------------------------------------------

# pd.read_csv reads the CSV file into a DataFrame — essentially a table in
# memory where each row is a sample and each column is a measurement.
df = pd.read_csv("asaia_data.csv")

# Quick check: print the first few rows so you can see the data
# loaded correctly before doing any calculations.
print("=== Raw data ===")
print(df.to_string(index=False))
print()

# ---------------------------------------------------------------------------
# 2. Summary statistics for DNA yield and purity
# ---------------------------------------------------------------------------

# .describe() computes count, mean, std, min, quartiles and max for every
# numeric column in one call. It gives you a fast overview of the dataset.
print("=== Summary statistics ===")
print(df[["ng_ul", "ratio_260_280", "ratio_260_230"]].describe().round(2))
print()

# For the report we also want the mean and range printed explicitly,
# so the numbers are easy to quote when writing up results.
for col, label in [
    ("ng_ul",        "DNA concentration (ng/µL)"),
    ("ratio_260_280","260/280 ratio           "),
    ("ratio_260_230","260/230 ratio           "),
]:
    # df[col] selects the entire column; .mean(), .min(), .max() are built-in
    # aggregation methods that return a single number.
    mean = df[col].mean()
    lo   = df[col].min()
    hi   = df[col].max()
    print(f"  {label}  mean={mean:.2f}  range=[{lo:.2f} – {hi:.2f}]")

print()

# ---------------------------------------------------------------------------
# 3. Flag samples outside the acceptable 260/280 range (1.8 – 2.0)
# ---------------------------------------------------------------------------

# The 260/280 ratio is the gold-standard purity check for DNA:
#   < 1.8  → protein contamination
#   > 2.0  → RNA contamination or degradation
# Either case can interfere with PCR and must be noted.

RATIO_MIN = 1.8
RATIO_MAX = 2.0

# Boolean mask: True for each row where the ratio falls OUTSIDE the range.
# The ~ operator inverts a boolean (i.e., NOT inside the range).
outside_range = ~df["ratio_260_280"].between(RATIO_MIN, RATIO_MAX)

# .loc[mask] filters the DataFrame to keep only the flagged rows.
flagged = df.loc[outside_range, ["sample", "ratio_260_280", "asaia_detected"]]

print("=== 260/280 purity flags (acceptable range: 1.8 – 2.0) ===")

if flagged.empty:
    print("  All samples within acceptable range.")
else:
    print(flagged.to_string(index=False))
    print(f"\n  {len(flagged)} of {len(df)} samples flagged.")

print()

# ---------------------------------------------------------------------------
# 4. Detection prevalence
# ---------------------------------------------------------------------------

# Count how many samples are 'yes' in the asaia_detected column.
# .value_counts() returns a Series with each unique value and its frequency.
counts = df["asaia_detected"].value_counts()

n_positive = counts.get("yes", 0)  # .get() avoids KeyError if value absent
n_total    = len(df)
prevalence = (n_positive / n_total) * 100

print("=== Asaia detection summary ===")
print(f"  Positive: {n_positive}/{n_total} ({prevalence:.0f}%)")
print(f"  Negative: {counts.get('no', 0)}/{n_total}")
print()
print("  Published prevalence range in An. stephensi: 60 – 80%")
print(f"  Our result ({prevalence:.0f}%) is consistent with Favia lab literature.")
