# Calculation of Molecule's Synthetic Accessibility

## Project Description
This Python implementation calculates the synthetic accessibility (SA) of molecules, as described in the paper *"The Estimation of Synthetic Accessibility Score of Drug-like Molecules"* published in the *Journal of Cheminformatics*. The method combines the frequency of molecular substructures in a large database with various complexity factors to generate a score ranging from 1 (easy) to 10 (difficult). This score represents the ease of synthesizing a given molecule. Custom functions were written in Python to calculate the necessary metrics and the SA score itself.

The method was validated by comparing the calculated mySAscores with the ease of synthesis ratings provided by experienced medicinal chemists for a set of 40 molecules, as well as the SA scores reported in the paper. The results showed a Pearson correlation of approximately 0.9, indicating strong consistency between the calculated scores and expert evaluations.

## Table of Contents

**Data**
- **40_molecules.csv**: Molecules used for validating the SA score calculation method, downloaded from the paper.
- **list_bits.pkl**: Precomputed fragment features for the 10 most common fragments in the PubChem dataset.
- **total_fragment_counts.pkl**: Precomputed counts of fragments in the PubChem dataset.

**Utils**
- **contribution_scores.py**: Calculates fragment counts and contribution scores for molecular fragments.
- **sa_score_calculator.py**: Computes the Synthetic Accessibility score based on fragment contributions and structural complexity.

**Analysis**
- **sas_computation_and_analysis.ipynb**: Jupyter notebook containing the calculation of molecular fragments and SA scores, along with statistical analysis and validation using the paper's dataset.

## How to Use the Project

To calculate the SA score for new molecules, use the custom functions from the `utils` folder. The precomputed fragment data in `list_bits.pkl` (which contains counts of fragments in a million-molecule dataset) is required for the calculation.
