###########################################################################
#                 HEALTHCALC PROGRAM FILE                                 #
###########################################################################
# Functionality: Calculates for daily protein and calorie intake          #
# for cutting or bulking                                                  #
# Note this function is a work in progress                                #
# Contributors: Anthony Le                                                #
# Date Created: 8/15/2023                                                 #
# Last Updated: 8/18/2023 Anthony                                         #
###########################################################################

# Sedentary (little or no exercise): Protein Intake Factor = 0.8 - 1.0
# Lightly active (light exercise/sports 1-3 days/week): Protein Intake Factor = 1.2 - 1.4
# Moderately active (moderate exercise/sports 3-5 days/week): Protein Intake Factor = 1.4 - 1.6
# Very active (hard exercise/sports 6-7 days a week): Protein Intake Factor = 1.6 - 1.8
# Extremely active (very hard exercise/sports, physical job, or training twice a day): Protein Intake Factor = 1.8 - 2.0

############ REFERENCE #################
# userHealth = {
#   "User": None,
#   "Age (year)": None,
#   "Gender (m/f)": None,
#   "Height (in)": None,
#   "Weight (lbs)": None, 
#   "Activity (days)": None
# }

# Imports
from functions import parse_healthlist_txt as p
from functions import conversions as c

# Body Mass Index Calc
def BMI_calc(userHealth):
  BMI = 0.0
  BMI = c.lbs_to_kg(float(userHealth["Weight (lbs)"])) / ((c.in_to_m(float(userHealth["Height (in)"])) * c.in_to_m(float(userHealth["Height (in)"]))))
  return BMI
# Gender_Const = 0.32810 Male
# Gender_Const = 0.33929 Female
# Lean Body Mass Calc
def LBM_calc(userHealth):

  # Calculates BMI and userWeight to kg
  Gender_Const = 0
  BMI = BMI_calc(userHealth)
  userWeight = c.lbs_to_kg(float(userHealth["Weight (lbs)"]))
  
  if userHealth["Gender (m/f)"] == 'm':
    Gender_Const = 0.32810

  elif userHealth["Gender (m/f)"] == 'f':
    Gender_Const = 0.33929 

  LBM = userWeight * (1 - Gender_Const * BMI)  
  return LBM


# Bulking Protein Factor = Lower Limit of Range + (Upper Limit of Range - Lower Limit of Range) *
# Activity and Goal Adjustment 0-1

# Determines the protein factor number based on activity
def protein_intake_factor(userHealth, option):

  if option == "Bulk":
    LBM = LBM_calc(userHealth)
    lower_limit = 1.6 / LBM_calc(userHealth)
    upper_limit = 1.8 / LBM_calc(userHealth)
    protein_factor = lower_limit + (upper_limit - lower_limit) * 0.8

  elif option == "Cut":
    LBM = LBM_calc(userHealth)
    lower_limit = 1.2 / LBM_calc(userHealth)
    upper_limit = 1.4 / LBM_calc(userHealth)
    protein_factor = lower_limit + (upper_limit - lower_limit) * 0.9
    
  return protein_factor

# Calcualtes daily protein for given choice bulk/cut in g
def daily_protein_calc(userHealth, option):
  
  if option == "Bulk":
    LBM = LBM_calc(userHealth)
    protein_factor = protein_intake_factor(userHealth, option)
    
    protein = LBM * protein_factor
    return protein
    
  elif option == "Cut":  
    LBM = LBM_calc(userHealth)
    protein_factor = protein_intake_factor(userHealth, option)

    protein = LBM * protein_factor
    return protein

  return -1
  
# For males: BMR = 10 × weight (kg) + 6.25 × height (cm) - 5 × age (years) + 5
# For females: BMR = 10 × weight (kg) + 6.25 × height (cm) - 5 × age (years) - 161
# BMR (Basal Metabolic Rate) Calculator
def bmr_calc(userHealth, option):
  if userHealth["Gender (m/f)"] == 'm':
    userWeight = c.lbs_to_kg(float(userHealth["Weight (lbs)"]))
    userHeight = c.in_to_cm(float(userHealth["Height (in)"]))
    userAge = float(userHealth["Age (year)"])
    bmr = 10 * userWeight + 6.25 * userHeight - 5 * userAge + 5
    return bmr

  elif userHealth["Gender (m/f)"] == 'f':
    userWeight = c.lbs_to_kg(float(userHealth["Weight (lbs)"]))
    userHeight = c.in_to_cm(float(userHealth["Height (in)"]))
    userAge = float(userHealth["Age (year)"])
    bmr = 10 * userWeight + 6.25 * userHeight - 5 * userAge - 161
    return bmr
    
  return -1

def activity_multiplier_calc(userHealth, option):
  act_multiplier = -1
  activity = float(userHealth["Activity (days)"])
  if option == "Bulk":
    # Not active
    if activity < 1:
      act_multiplier = bmr_calc(userHealth, option) * 1.2
  
    # Sorta Active
    elif activity <= 1 or activity <= 3:
      act_multiplier = bmr_calc(userHealth, option) * 1.375
  
    # Moderately Active
    elif activity < 3 or activity <= 5.5:
      act_multiplier = bmr_calc(userHealth, option) * 1.55
  
    # Very Active
    elif activity < 5.5 or activity <= 7:
      act_multiplier = bmr_calc(userHealth, option) * 1.725

  elif option == "Cut":
    # Not active
    if activity < 1:
      act_multiplier = bmr_calc(userHealth, option) * 1.1
  
    # Sorta Active
    elif activity <= 1 or activity <= 3:
      act_multiplier = bmr_calc(userHealth, option) * 1.275
  
    # Moderately Active
    elif activity < 3 or activity <= 5.5:
      act_multiplier = bmr_calc(userHealth, option) * 1.45
  
    # Very Active
    elif activity < 5.5 or activity <= 7:
      act_multiplier = bmr_calc(userHealth, option) * 1.625
      
  return act_multiplier
  
# Calcualtes daily calories for given choice bulk/cut
def daily_calorie_calc(userHealth, option):
  BMR = bmr_calc(userHealth, option)
  act_multiplier = activity_multiplier_calc(userHealth, option)
  calories = BMR * act_multiplier
    
  return calories

# Calculates daily protein and calculator intake
def calc_daily_intake(userHealth, option):
  
  protein = protein_intake_factor(userHealth, option)
  calories = daily_calorie_calc(userHealth, option)
  
  return round(protein,2), round(calories,2)


