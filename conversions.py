# Calculates Conversions Functions
def lbs_to_kg(lbs):
    kg = lbs * 0.45359237
    kg = round(kg, 2)
    return kg

def kg_to_lbs(kg):
  lbs = kg * 2.20462262
  lbs = round(lbs, 2)
  return lbs