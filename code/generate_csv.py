import csv

def generate_csv():
    filename = "sovereign_molecules.csv"
    
    # FORMAT: Name, SMILES_String, Category, Source_Paper
    data = [
        # --- 1. THE ZENIL DATASET (Low Complexity, High LZW Correlation) ---
        # Zenil argues these prove AT is just Compression.
        ("Adenine", "C1=NC2=NC=NC2=C1N", "Biotic_Low", "Zenil_PLOS_2024"),
        ("Glucose", "C(C1C(C(C(C(O1)O)O)O)O)O", "Biotic_Low", "Zenil_PLOS_2024"),
        ("Tryptophan", "C1=CC=C2C(=C1)C(=CN2)CC(C(=O)O)N", "Biotic_Low", "Zenil_PLOS_2024"),
        ("Porphyrin", "C1=CC2=C(C=C3C=C(C=C4C=C(C=C1N2)N4)N3)N", "Biotic_Mid", "Zenil_PLOS_2024"),
        
        # --- 2. THE WALKER DATASET (High Complexity, LZW Divergence) ---
        # Walker uses these to prove AT measures "History".
        ("Gemcitabine", "C1=CN(C(=O)N=C1N)C2C(C(C(O2)CO)O)(F)F", "Biotic_Threshold", "Nature_2021"),
        ("Taxol", "CC1=C2C(C(=O)C3(C(CC4C(C3C(C(C2(C)C)(CC1OC(=O)C(C(C5=CC=CC=C5)NC(=O)C6=CC=CC=C6)O)O)OC(=O)C7=CC=CC=C7)(CO4)OC(=O)C)O)C)O", "Biotic_High", "Nature_2021"),
        ("ATP", "C1=NC(=C2C(=N1)N(C=N2)C3C(C(C(O3)COP(=O)(O)OP(=O)(O)OP(=O)(O)O)O)O)N", "Biotic_Mid", "Nature_2021"),
        
        # --- 3. THE "FINAL BOSS" (Maitotoxin) ---
        # The largest non-protein natural product. 
        # Note: This is a truncated representation of the core ring system for simulation speed.
        # A full Maitotoxin SMILES is ~3000 chars. We use the 'Core' representing the dense ring structure.
        ("Maitotoxin_Core", "CC1C(C(C(C(O1)OC2C(OC(C(C2O)O)OC3C(OC(C(C3O)O)OC4C(OC(C(C4O)O)OC5C(OC(C(C5O)O)OC6C(OC(C(C6O)O)O)C)C)C)C)C)C)O)O", "Biotic_Extreme", "Nature_2023"),

        # --- 4. THE SOVEREIGN CONTROLS ---
        ("Poly-A_Crystal", "A"*50, "Abiotic_Crystal", "Sovereign_Lab"),
        ("Random_Noise_Short", "ACGT"*10 + "TGCA", "Random", "Sovereign_Lab"),
        ("Random_Taxol_Len", "C1(C)O=N2" * 10, "Random_Control", "Sovereign_Lab"),
        
        # --- 5. SYNTHETIC TEST ---
        # Viagra. It is complex, but designed by humans. Does it score like Nature?
        ("Sildenafil", "CCCC1=NN(C2=C1N=C(NC2=O)C3=CC(=CC=C3)S(=O)(=O)N4CCN(CC4)C)C", "Synthetic_Drug", "Sovereign_Lab"),
        
        # From generate_final_csv.py
        # --- 1. THE ZENIL TRAP (Small E. coli Metabolites) ---
        # Zenil is RIGHT here: These are too small to have "History". LZW = AT.
        ("Pyruvate", "CC(=O)C(=O)O", "Metabolite_Small", "Zenil_PLOS_2024"),
        ("Lactate", "CC(O)C(=O)O", "Metabolite_Small", "Zenil_PLOS_2024"),
        ("Alanine", "CC(N)C(=O)O", "Metabolite_Small", "Zenil_PLOS_2024"),
        ("Citrate", "OC(=O)CC(O)(CC(O)=O)C(O)=O", "Metabolite_Small", "Zenil_PLOS_2024"),

        # --- 2. THE WALKER FORTRESS (High Complexity Biosignatures) ---
        # Walker is RIGHT here: These have deep history. LZW fails to capture it.

        # --- 3. THE SOVEREIGN DEFENSE (Robustness Check) ---
        # Vancomycin (Complex Glycopeptide Antibiotic) -> Proves we handle 'sugar+protein' hybrids.
        ("Vancomycin", "Cl.CNC(CC(C)C)C(=O)NC1C(O)C2=CC(Cl)=C(OC3=CC4=CC(OC5=C(Cl)C=C(C=C5)C(O)C5NC(=O)C(NC(=O)C4NC(=O)C(CC(N)=O)NC1=O)C1=CC(=C(O)C=C1)C1=C(O)C=C(O)C=C1C(NC5=O)C(O)=O)=C3OC1OC(CO)C(O)C(O)C1OC1CC(C)(N)C(O)C(C)O1)C=C2", "Biotic_Complex", "Sovereign_Lab"),
        
        # Gramicidin S (Cyclic Peptide) -> Proves we handle 'repeating biology' (Peptides).
        ("Gramicidin_S", "CC(C)C[C@H]1C(=O)N[C@@H](C(=O)N2CCC[C@H]2C(=O)N[C@H](C(=O)N[C@H](C(=O)N[C@H](C(=O)N[C@@H](C(=O)N3CCC[C@H]3C(=O)N[C@H](C(=O)N[C@H](C(=O)N1)CCCN)C(C)C)CC4=CC=CC=C4)CC(C)C)CCCN)C(C)C)CC5=CC=CC=C5", "Peptide_Cyclic", "Sovereign_Lab"),

        # --- 4. CONTROLS ---
        ("Random_Noise", "C(O)N1"*10, "Random_Control", "Sovereign_Lab")
    ]

    print(f"📝 Generating {filename} with {len(data)} molecular entities...")
    
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Sequence", "Category", "Source"]) # Header
        writer.writerows(data)
        
    print("✅ CSV Generation Complete.")

if __name__ == "__main__":
    generate_csv()
