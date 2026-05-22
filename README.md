# Asaia Detection in *Anopheles stephensi* — Computational Analysis

Computational analysis of real experimental data from my bachelor thesis:  
**"Mosquitoes rearing and detection of bacteria symbionts in malaria vectors"**  
Laboratory of Prof. Guido Favia, University of Camerino, Italy

---

## Background

### Why *Anopheles stephensi* matters

*Anopheles stephensi* is an Asian malaria vector that has been spreading into
sub-Saharan Africa since its first confirmed detection in Djibouti in 2012 and
Ethiopia in 2019. Its invasion has placed an estimated 126 million people in
urban Africa at new risk of malaria transmission — a region that had previously
lacked a competent urban vector for *Plasmodium falciparum*. Because it thrives
in man-made water containers, standard vector-control measures designed for
*An. gambiae* are less effective against it.

### Asaia and paratransgenesis

*Asaia* is an acetic-acid bacterium in the family Acetobacteraceae that
naturally colonises the midgut, salivary glands, and reproductive organs of
several *Anopheles* species. Prof. Favia's laboratory, one of the pioneering
groups in paratransgenesis research, has demonstrated that *Asaia* can be
genetically modified to express anti-*Plasmodium* effector molecules and spread
horizontally through mosquito populations via co-feeding, mating, and
transovarial transmission.

If engineered *Asaia* strains can be stably introduced into wild populations,
they could reduce the vectorial capacity of the mosquito without killing it —
a key advantage over insecticide-based approaches that drive resistance
evolution. Confirming the natural presence of *Asaia* in a laboratory colony
is therefore a prerequisite before any paratransgenesis experiment can begin.

### This study

I bred four mosquito species in the insectary at Camerino:
*An. stephensi*, *An. gambiae*, *Aedes aegypti*, and *Ae. albopictus*.
For the Asaia screening I used 10 female *An. stephensi* individuals from the
Sind-Kasur colony. DNA was extracted from whole bodies using a standard
CTAB-based protocol, and purity was assessed by NanoDrop spectrophotometry
before PCR amplification with *Asaia*-specific 16S rRNA primers.

**Result: 7 out of 10 mosquitoes (70%) tested PCR-positive for *Asaia*.**

### The Sind-Kasur strain

The *An. stephensi* Sind-Kasur strain used in this study is a laboratory
strain — the original mosquito population was collected from the Sind/Kasur
region of the Indian subcontinent (most likely Pakistan) and subsequently
maintained for many generations under controlled insectary conditions.
Laboratory strains are reared in stable environmental conditions, including
controlled temperature, humidity, and feeding, allowing researchers to perform
reproducible experiments with mosquitoes of known genetic and biological
background. This study therefore did not investigate wild mosquitoes currently
circulating in Pakistan or India, but rather a laboratory-maintained descendant
colony originating from that geographic area.

### Significance of the 70% prevalence

The detection of *Asaia* in 7 out of 10 Sind-Kasur mosquitoes by PCR is
scientifically significant because it demonstrates that this symbiotic
bacterium is naturally maintained in an important malaria vector strain even
after long-term laboratory colonisation. This finding supports the hypothesis
that *Asaia* forms a stable association with *An. stephensi* and may be
suitable for paratransgenic approaches aimed at malaria control.

Since *Asaia* has been proposed as a bacterial carrier for anti-*Plasmodium*
molecules, confirming its presence in the Sind-Kasur strain suggests that this
mosquito line could be useful as an experimental model for microbiome-based
malaria intervention strategies relevant to regions where *An. stephensi* is
an important vector — including Pakistan, India, Iran, and the emerging African
endemic areas where the species has been invading since 2019.

---

## Repository structure

```
Asaia-project/
├── asaia_data.csv          Real NanoDrop + PCR data (n=10 An. stephensi)
├── analysis.py             Summary statistics and purity flagging
├── visualizations.py       Figures 1 & 2: concentration bar chart + purity scatter
├── outputs/                Generated figures (not tracked by Git)
├── requirements.txt        Python dependencies
└── README.md               This file
```

---

## Scripts

### `analysis.py`
Loads the CSV with pandas and produces:
- Descriptive statistics (mean, min, max) for DNA concentration and both purity ratios
- A list of samples whose A260/A280 ratio falls outside the acceptable 1.8–2.0 window
- Final detection prevalence (7/10, 70%)

### `visualizations.py`
Generates two figures saved to `outputs/`:
- **Figure 1** — Bar chart of DNA concentration per sample, colour-coded by PCR result
- **Figure 2** — Scatter plot of A260/A280 vs A260/A230, with shaded reference band

---

## How to run

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/Asaia-project.git
cd Asaia-project

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the scripts
py analysis.py
py visualizations.py
```

Figures are saved automatically to the `outputs/` folder.

---

## Data description

| Column | Description |
|---|---|
| `sample` | Sample ID (1F–10F; F = female) |
| `ng_ul` | DNA concentration in ng/µL (NanoDrop) |
| `ratio_260_280` | A260/A280 absorbance ratio — protein contamination indicator (acceptable: 1.8–2.0) |
| `ratio_260_230` | A260/A230 absorbance ratio — salt/solvent contamination indicator (acceptable: 2.0–2.2) |
| `asaia_detected` | PCR result: `yes` = Asaia-positive, `no` = Asaia-negative |

---

## Key results

| Metric | Value |
|---|---|
| Mean DNA concentration | 76.22 ng/µL |
| Mean A260/A280 | 1.97 |
| Samples outside 260/280 range | 3/10 (all slightly >2.0, still PCR-amplifiable) |
| Asaia prevalence | **70%** (7/10) |

---

## Dependencies

- Python 3.8+
- pandas
- matplotlib

---

## Author

**Areti Barakou**  
BSc + MSc in Biosciences and Biotechnology  
University of Camerino, Italy  
Thesis laboratory: Prof. Guido Favia

---

## References

- Favia G. et al. (2007) Bacteria of the genus *Asaia* stably associate with *Anopheles stephensi*, an Asian malarial mosquito vector. *PNAS* 104(21):9047–9051.  
- Crotti E. et al. (2009) *Asaia*, a versatile acetic acid bacterial symbiont, able to colonize different insect species and organs. *Appl Environ Microbiol* 75(10):3252–3258.  
- Rossi P. et al. (2012) A *Wolbachia*-free *Asaia* paratransgenic approach to block *Plasmodium* transmission in *Anopheles* mosquitoes. *Parasites & Vectors* 5:140.  
- Valzano M. et al. (2016) *Asaia* sp. associated with *Anopheles stephensi* and implications for malaria control. *Parasites & Vectors* 9:111.  
- Bghoul W. et al. (2022) Invasion of *Anopheles stephensi* in Africa: a review. *Parasites & Vectors* 15:96.
