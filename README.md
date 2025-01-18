# Calculation of Molecule's Synthetic Accessibility
<p align="center">
  <img src="https://github.com/utenok-malenkiy/koko/blob/main/cute-molecule.jpeg?raw=true" width="300"/>
</p>

## Project Description
Scientists learned how to synthesize certain molecules many-many decades ago. But how can one be sure if a new given molecule can be easily synthesized in real life? Is it necessary to test it experimentally to understand its feasibility? This might waste valuable resources, which is why scientists developed a method for calculating a special score that indicates how difficult it is to synthesize a molecule, based on its structure and the frequency of fragments that make up the molecule in known databases.

My project investigates the method described in the paper *"The Estimation of Synthetic Accessibility Score of Drug-like Molecules"* published in the **Journal of Cheminformatics** and provides a Python implementation of it. My code is tested on a sample of 40 molecules, for which expert chemists' scores and research on the SA score are available for comparison.

## Table of Contents

**Analysis**
- **sas_computation_and_analysis.ipynb**: Jupyter notebook containing the calculation of molecular fragments and SA scores, along with statistical analysis and validation.
  
**Utils**
- **contribution_scores.py**: Calculates fragment counts and contribution scores for molecular fragments.
- **SA_score_calculator.py**: Computes the Synthetic Accessibility score based on fragment contributions and structural complexity.

**Data**
- **40_molecules.csv**: Molecules used for validating the SA score calculation method, downloaded from the paper.
- **list_bits.pkl**: Precomputed fragment features for the 10 most common fragments in the PubChem dataset.
- **total_fragment_counts.pkl**: Precomputed counts of fragments in the PubChem dataset.

## How to Use the Project

To calculate the Synthetic Accessibility (SA) score for new molecules, follow these steps:

1. **Prepare your input data**: Ensure that your molecule data is in a compatible format (e.g., SMILES notation) and stored in a CSV or similar file.

2. **Utilize custom functions from the `utils` folder**: The project includes Python functions for SA score calculation. To use all the utility functions from the `utils` folder, simply include the following import statement:

   ```python
   from utils import *
3. **Ensure access to precomputed fragment data:** The precomputed fragment features in `list_bits.pkl` (which contains fragment counts from a million-molecule dataset) are required for accurate calculation. Ensure that this file is available in your working directory.
  
4. **Run the calculations:** After loading your molecule data and ensuring the required fragment data is present, use the functions to compute the SA score. You can integrate the code into your own workflow or use the provided Jupyter notebook (`sas_computation_and_analysis.ipynb`) for an interactive, guided analysis.

## References
- Ertl, P., Schuffenhauer, A. (2009). The Estimation of Synthetic Accessibility Score of Drug-like Molecules. Journal of Cheminformatics, 1, 8. https://doi.org/10.1186/1758-2946-1-8
- PubChem. (n.d.). PubChem SDF data. National Center for Biotechnology Information. Retrieved December 5, 2024, from https://ftp.ncbi.nlm.nih.gov/pubchem/Compound/CURRENT-Full/SDF/
