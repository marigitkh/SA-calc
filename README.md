# Calculation of Molecule's Synthetic Accessibility

## Project Description
It is a well-known fact that people have been creating chemical molecules for many years. To develop new methods for molecule synthesis, scientists learned to transfer information about molecules into computers and perform analyses. But how can one be sure if a given molecule can be easily synthesized in real life? Is it necessary to test it experimentally to understand its feasibility? This might waste valuable resources, which is why scientists developed a method for calculating a special score that indicates how difficult it is to synthesize a molecule, based on its structure and the frequency of fragments that make up the molecule in known databases.

My project investigates the method described in the paper "The Estimation of Synthetic Accessibility Score of Drug-like Molecules" published in the Journal of Cheminformatics and provides a Python implementation of it. My code is tested on a sample of 40 molecules, for which expert chemists' scores and research on the SA score are available for comparison.

## Table of Contents

**Analysis**
- **sas_computation_and_analysis.ipynb**: Jupyter notebook containing the calculation of molecular fragments and SA scores, along with statistical analysis and validation using the paper's dataset.

**Utils**
- **contribution_scores.py**: Calculates fragment counts and contribution scores for molecular fragments.
- **sa_score_calculator.py**: Computes the Synthetic Accessibility score based on fragment contributions and structural complexity.

**Data**
- **40_molecules.csv**: Molecules used for validating the SA score calculation method, downloaded from the paper.
- **list_bits.pkl**: Precomputed fragment features for the 10 most common fragments in the PubChem dataset.
- **total_fragment_counts.pkl**: Precomputed counts of fragments in the PubChem dataset.

## How to Use the Project

To calculate the SA score for new molecules, use the custom functions from the `utils` folder. The precomputed fragment data in `list_bits.pkl` (which contains counts of fragments in a million-molecule dataset) is required for the calculation.

## References
- Ertl, P., Schuffenhauer, A. (2009). The Estimation of Synthetic Accessibility Score of Drug-like Molecules. Journal of Cheminformatics, 1, 8. https://doi.org/10.1186/1758-2946-1-8
- PubChem. (n.d.). PubChem SDF data. National Center for Biotechnology Information. Retrieved December 5, 2024, from https://ftp.ncbi.nlm.nih.gov/pubchem/Compound/CURRENT-Full/SDF/
