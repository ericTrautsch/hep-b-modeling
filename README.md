# Problem Statement: Hepatitis B Virus (HBV) Data Analysis

## Project Overview

### Background
Hepatitis B virus (HBV) remains a major global health issue, affecting millions worldwide. Data-driven analysis plays a critical role in understanding patterns of disease progression, treatment responses, and patient outcomes, which can ultimately guide more effective healthcare strategies.

### Objective
The objective of this project is to analyze a provided HBV dataset to uncover key trends related to patient demographics, viral load progression, and treatment outcomes. By applying efficient data exploration techniques, the goal is to produce actionable insights that can enhance understanding of HBV-related factors.

### Key Challenges
- **Data Quality:** Handling potential inconsistencies or missing data entries to ensure reliable analysis.
- **Scope of Analysis:** Focusing on critical trends and patterns within the dataset for effective insights.

### Proposed Solution
This project will involve:
- Preparing and cleaning the dataset to resolve any inconsistencies or missing values.
- Performing exploratory data analysis (EDA) to identify and visualize important trends, such as demographic distributions, changes in viral load, and treatment outcomes.
- Generating clear, concise visualizations that present the findings in an accessible manner.

### Expected Outcomes
- A well-prepared HBV dataset suitable for analysis.
- Key insights into patient demographics, viral load patterns, and treatment efficacy through data visualizations.
- A summary of findings that can provide a basis for further analysis or inform future HBV-related research.

## Getting Started

### Prerequisites

1. Install [nix: the package manager](https://nixos.org/download/) into your shell environment
2. Enable [Flakes](https://nixos.wiki/wiki/Flakes)
3. Run `nix develop` in your terminal (or setup `nix-direnv`)

### Creating The Dataset

This repository does not contain the dataset used to train and evaluate this hepb prediction model. To build the data locally (requires an internet connection), run

```bash
Rscript data/create_dataset.R
```

### Training Models

To train the model, ensure the dataset is built and Run

```bash
python models/train_model.py
```

### Viewing Results
