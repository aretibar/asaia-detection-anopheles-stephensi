"""
visualizations.py
-----------------
Two publication-style figures from the An. stephensi NanoDrop + PCR dataset:

  Figure 1 — DNA concentration per sample, coloured by Asaia detection result.
             Samples are ordered as extracted (1F–10F); the colour encodes
             whether each mosquito tested PCR-positive for the symbiont.

  Figure 2 — Scatter plot of the two NanoDrop purity ratios (260/280 vs
             260/230), coloured by detection result. Reference lines at 1.8
             and 2.0 mark the acceptable 260/280 window for downstream PCR.

Both figures are saved as high-resolution PNGs in the outputs/ folder so the
working directory stays clean.

Author: Areti Barakou
Data: An. stephensi (sind-kasur), Lab of Prof. Guido Favia, Univ. Camerino
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import os

# ---------------------------------------------------------------------------
# Setup
# ---------------------------------------------------------------------------

# Load the dataset — same file used by analysis.py
df = pd.read_csv("asaia_data.csv")

# Make sure the outputs folder exists before trying to save into it.
# os.makedirs with exist_ok=True does nothing if the folder is already there.
os.makedirs("outputs", exist_ok=True)

# Define colours that will be reused in both figures.
# A dictionary lets us map the string values directly to colours.
COLOURS = {"yes": "#2ecc71", "no": "#95a5a6"}  # green for positive, grey for negative

# Build a list of colours in the same row-order as the DataFrame.
# df["asaia_detected"].map(COLOURS) replaces each "yes"/"no" with its colour.
bar_colours = df["asaia_detected"].map(COLOURS)

# ---------------------------------------------------------------------------
# Figure 1 — DNA concentration bar chart
# ---------------------------------------------------------------------------

fig1, ax1 = plt.subplots(figsize=(10, 5))

# ax1.bar draws one vertical bar per sample.
# x positions come from df["sample"] (the labels), heights from df["ng_ul"].
ax1.bar(df["sample"], df["ng_ul"], color=bar_colours, edgecolor="white", linewidth=0.6)

# A dashed horizontal line at 50 ng/µL marks the practical lower limit for
# reliable PCR amplification from mosquito whole-body extracts.
ax1.axhline(50, color="#e74c3c", linestyle="--", linewidth=1.2, label="PCR threshold (50 ng/µL)")

# Axis labels and title — written as they would appear in a thesis figure legend
ax1.set_xlabel("Sample", fontsize=12)
ax1.set_ylabel("DNA concentration (ng/µL)", fontsize=12)
ax1.set_title(
    "DNA yield per An. stephensi individual\n(sind-kasur colony, n=10)",
    fontsize=13, fontweight="bold"
)

# Build a legend manually: one patch per detection category + the threshold line.
# mpatches.Patch creates a coloured rectangle suitable for a bar-chart legend.
legend_handles = [
    mpatches.Patch(color=COLOURS["yes"], label="Asaia-positive (PCR+)"),
    mpatches.Patch(color=COLOURS["no"],  label="Asaia-negative (PCR−)"),
    plt.Line2D([0], [0], color="#e74c3c", linestyle="--", linewidth=1.2,
               label="PCR threshold (50 ng/µL)"),
]
ax1.legend(handles=legend_handles, framealpha=0.9)

# Remove the top and right spines for a cleaner, more academic look.
ax1.spines["top"].set_visible(False)
ax1.spines["right"].set_visible(False)

plt.tight_layout()
fig1.savefig("outputs/fig1_dna_concentration.png", dpi=150)
print("Saved: outputs/fig1_dna_concentration.png")
plt.close(fig1)  # close so it doesn't display interactively (important for scripts)

# ---------------------------------------------------------------------------
# Figure 2 — Purity ratio scatter plot (260/280 vs 260/230)
# ---------------------------------------------------------------------------

fig2, ax2 = plt.subplots(figsize=(7, 6))

# Scatter each sample as a point. The colour again encodes detection result.
# s=90 sets the marker size; zorder=3 draws points on top of the reference lines.
for _, row in df.iterrows():
    ax2.scatter(
        row["ratio_260_280"],
        row["ratio_260_230"],
        color=COLOURS[row["asaia_detected"]],
        s=90, zorder=3, edgecolors="white", linewidths=0.5
    )
    # Label each point with its sample name, offset slightly so it doesn't
    # overlap the marker.
    ax2.annotate(
        row["sample"],
        (row["ratio_260_280"], row["ratio_260_230"]),
        textcoords="offset points", xytext=(6, 4),
        fontsize=8, color="#555555"
    )

# Vertical reference lines at 1.8 and 2.0 mark the acceptable 260/280 window.
# A shaded band between them visually highlights the acceptable zone.
ax2.axvline(1.8, color="#3498db", linestyle="--", linewidth=1.1, label="260/280 = 1.8")
ax2.axvline(2.0, color="#e67e22", linestyle="--", linewidth=1.1, label="260/280 = 2.0")
ax2.axvspan(1.8, 2.0, alpha=0.07, color="#3498db")  # subtle blue shading

ax2.set_xlabel("A260/A280 ratio", fontsize=12)
ax2.set_ylabel("A260/A230 ratio", fontsize=12)
ax2.set_title(
    "NanoDrop purity ratios — An. stephensi DNA extracts\n(acceptable 260/280 range: 1.8 – 2.0)",
    fontsize=13, fontweight="bold"
)

legend_handles2 = [
    mpatches.Patch(color=COLOURS["yes"], label="Asaia-positive (PCR+)"),
    mpatches.Patch(color=COLOURS["no"],  label="Asaia-negative (PCR−)"),
    plt.Line2D([0], [0], color="#3498db", linestyle="--", linewidth=1.1, label="260/280 = 1.8"),
    plt.Line2D([0], [0], color="#e67e22", linestyle="--", linewidth=1.1, label="260/280 = 2.0"),
]
ax2.legend(handles=legend_handles2, framealpha=0.9, fontsize=9)

ax2.spines["top"].set_visible(False)
ax2.spines["right"].set_visible(False)

plt.tight_layout()
fig2.savefig("outputs/fig2_purity_ratios.png", dpi=150)
print("Saved: outputs/fig2_purity_ratios.png")
plt.close(fig2)

print("\nBoth figures saved to outputs/")
