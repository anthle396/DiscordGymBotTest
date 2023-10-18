###########################################################################
#                 VERTICAL CALC PROGRAM FILE                              #
###########################################################################
# Functionality: Calculates max theoretical vertical jump based on        #
# health stats                                                            #
# Contributors: Carl P                                                    #
# Date Created: 8/18/2023                                                 #
# Last Updated: 8/18/2023 Carl                                            #
###########################################################################

####### REFERENCE ###########
# Dict Var for healthstats
# userHealth = {
#   "User": None,
#   "Age (year)": None,
#   "Gender (m/f)": None,
#   "Height (in)": None,
#   "Weight (lbs)": None, 
#   "Activity (days)": None
# }

# Dict Var for userPRs
# userPRs_dict = {
#   "User": None,
#   "Weight (lbs)": None,
#   "Bench (lbs)": None,
#   "Squat (lbs)": None, 
#   "Deadlift (lbs)": None, 
#   "Pullups (reps)": None, 
#   "Pushups (reps)": None
# }

# Libraries
from functions import conversions as c

def vert_calc(userHealth, userPR_dict):

  weight_lbs  = userHealth["Weight (lbs)"]
  max_squat_lbs = userPRs_dict["Squat (lbs)"]

  vert = ((.1117 * max_squat_lbs) + (0.2233 * weight_lbs)) / 2
  
  return vert

#formula calories/protein for bulk or cut
# bulk_cals = (10 × weight in kilograms) + (6.25 × height in centimeters) – (5 × age in years) + 5
# Cutting: 
# BMR = 88.362 + (13.397 x weight in kg) + (4.799 x height in cm) - (5.677 x age in years)
# multiply BMR by deficit (%)

