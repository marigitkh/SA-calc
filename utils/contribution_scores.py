from rdkit.Chem import AllChem
from collections import Counter
import math

def calculate_fragment_counts(molecules: list):
    """
    Calculates the count of each fragment in the dataset from a list of RDKit Mol objects.
    
    Parameters:
        molecules: List of RDKit Mol objects.

    Returns:
        Counter: Fragment counts as {fragment_hash: count}.
    """
    def get_fragment_counts(mol):
        return Counter(AllChem.GetMorganFingerprint(mol, 2).GetNonzeroElements())
    
    return sum((get_fragment_counts(mol) for mol in molecules), Counter())


def calculate_contribution_scores(fragment_counts: Counter):
    """
    Calculates contribution scores for molecular fragments using fragment counts.
    
    Parameters:
        fragment_counts (Counter): Fragment counts as {fragment_hash: count}.
    
    Returns:
        dict: Contribution scores as {fragment_hash: score}.
    """
    total_fragments = sum(fragment_counts.values())
    if not total_fragments:
        return {}
    
    # Determine 80% cumulative contribution
    cumulative_count, frequent_fragment_types = 0, set()
    for fragment, count in sorted(fragment_counts.items(), key=lambda x: -x[1]):
        cumulative_count += count
        frequent_fragment_types.add(fragment)
        if cumulative_count >= total_fragments * 0.8:
            break

    num_frequent_types = len(frequent_fragment_types)
    return {
        fragment: math.log(count / num_frequent_types) if num_frequent_types > 0 else float('-inf')
        for fragment, count in fragment_counts.items()
    }
