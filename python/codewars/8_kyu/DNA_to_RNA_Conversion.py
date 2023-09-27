def dna_to_rna(dna):
    if "T" in dna:
        dna = dna.replace("T", "U")
    elif "U" in dna:
        dna = dna.replace("U", "T")
    return dna
