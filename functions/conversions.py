###########################################################################
#                 CONVERSIONS PROGRAM FILE                                #
###########################################################################
# Functionality: Implements all the functionality of adding, removing,    #
# and editing, userPRs                                                    #
# Contributors: Anthony Le                                                #
# Date Created: 8/11/2023                                                 #
# Last Updated: 8/11/2023 Anthony                                         #
###########################################################################
# Calculates Conversions Functions
# "!lbstokg" - Converts lbs to kg ["lbs -> kg."]
# "!kgtolbs" - Converts kg to lbs ["kg -> lbs."]
# "!fttoin" - Converts ft to in  ## WORK IN PROGRESS
# "!intoft" - Converts in to ft ## WORK IN PROGRESS
# "!cmtoin" - Converts in to ft ## WORK IN PROGRESS
# "!mtoin" - Converts in to ft ## WORK IN PROGRESS
# "!intocm" - Converts in to ft ## WORK IN PROGRESS
# "!intom" - Converts in to ft ## WORK IN PROGRESS

# Converts lbs -> kg
def lbs_to_kg(lbs):
    kg = lbs * 0.45359237
    kg = round(kg, 2)
    return kg
  
# Converts kg -> lbs
def kg_to_lbs(kg):
  lbs = kg * 2.20462262
  lbs = round(lbs, 2)
  return lbs

# Converts ft -> in
def ft_to_in(ft):
  inch = ft * 12
  inch = round(inch, 2)
  return inch

# Converts in -> ft
def in_to_ft(inch):
  ft = float(inch) / 12.0
  ft = round(ft, 2)
  return ft

# Converts cm -> in
def cm_to_in(cm):
  inch = cm * 0.393700787
  inch = round(inch, 2)
  return inch

# Converts m -> in
def m_to_in(m):
  inch = m * 39.3700787
  inch = round(inch, 2)
  return inch

# Converts in -> cm
def in_to_cm(inch):
  cm = inch * 2.54
  cm = round(cm, 2)
  return cm

# Converts in -> m
def in_to_m(inch):
  m = inch * 0.0254 
  m = round(m, 2)
  return m



