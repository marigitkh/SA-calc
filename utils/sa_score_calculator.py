import math
from rdkit import Chem
from rdkit.Chem import AllChem
from collections import Counter


def calculate_fragment_score(molecule: Chem.Mol, contribution_scores):
    """
    Compute the fragment-based contribution score for a molecule.

    Parameters:
        molecule: RDKit molecule object.
        contribution_scores: Dictionary of fragment contribution scores.

    Returns:
        float: The fragment score derived from the contributions of molecular fragments.
    """
    # Extract ECFC_4# fragment counts from the molecule
    fragment_counts = Counter(
        AllChem.GetMorganFingerprint(molecule, 2).GetNonzeroElements()
    )

    # Calculate the total fragment contribution score
    total_fragment_score = sum(
        # since the smalles fragment contribution score is -6.87, for the fragment which is not found in db a score of -7 is assigned
        contribution_scores.get(fragment, -7) * count
        for fragment, count in fragment_counts.items()
    )

    # Calculate the number of fragments
    total_fragments = sum(fragment_counts.values())
    fragment_score = total_fragment_score / total_fragments if total_fragments > 0 else 0

    return fragment_score


def calculate_complexity_score(molecule: Chem.Mol):
    """
    Compute the complexity score for a molecule based on structural features.

    Parameters:
        molecule: RDKit molecule object.

    Returns:
        float: A score quantifying the structural complexity of the molecule.
    """
    # Ring complexity: accounts for bridgehead and spiro atoms
    ring_info = molecule.GetRingInfo()
    n_ring_bridge_atoms = AllChem.CalcNumBridgeheadAtoms(molecule)
    n_spiro_atoms = AllChem.CalcNumSpiroAtoms(molecule)
    ring_complexity_score = math.log(n_ring_bridge_atoms + 1) + math.log(n_spiro_atoms + 1)

    # Stereo complexity: based on chiral centers
    n_stereo_centers = len(Chem.FindMolChiralCenters(molecule, includeUnassigned=True))
    stereo_complexity_score = math.log(n_stereo_centers + 1)

    # Macrocycle penalty: penalizes large rings (size > 8)
    n_macrocycles = sum(1 for ring in ring_info.AtomRings() if len(ring) > 8)
    macrocycle_penalty = math.log(n_macrocycles + 1)

    # Size penalty: based on the number of heavy atoms
    n_atoms = molecule.GetNumHeavyAtoms()
    size_penalty = n_atoms**1.005 - n_atoms

    # Total complexity score
    complexity_score = (
        ring_complexity_score
        + stereo_complexity_score
        + macrocycle_penalty
        + size_penalty
    )

    return complexity_score


def calculate_sa(molecule: Chem.Mol, contribution_scores):
    """
    Calculate the Synthetic Accessibility score for a molecule.

    Parameters:
        molecule: RDKit molecule object.
        contribution_scores: Dictionary of fragment contribution scores.

    Returns:
        float: SA score scaled between 1 and 10.
    """
    fragment_score = calculate_fragment_score(molecule, contribution_scores)
    complexity_score = calculate_complexity_score(molecule)
    raw_score = fragment_score - complexity_score
    inverted_score = -raw_score
    min_score = -6.87
    max_score = 8.65
    normalized_score = (inverted_score - min_score) / (max_score - min_score)
    sa_score = 1 + 9 * normalized_score

    return sa_score
