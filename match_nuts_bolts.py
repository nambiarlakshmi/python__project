def match_nuts_bolts(nuts, bolts):
    nuts.sort()
    bolts.sort()
    return nuts, bolts

nuts = [4, 2, 5, 1, 3]
bolts = [3, 5, 1, 4, 2]
matched_nuts, matched_bolts = match_nuts_bolts(nuts, bolts)
print("Nuts:", matched_nuts)
print("Bolts:", matched_bolts)
#Chat GPT helped me