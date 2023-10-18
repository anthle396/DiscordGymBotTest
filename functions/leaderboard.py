###########################################################################
#                 LEADERBOARD PROGRAM FILE                                #
###########################################################################
# Functionality:                                                          #
# Contributors: Aaron Mai, Anthony Le                                     #
# Date Created: 8/13/2023                                                 #
# Last Updated: 8/18/2023 Aaron, Anthony                                  #
###########################################################################
from functions import parse_PRlist_txt as p
# import numpy as np
# import pandas as panda
# import matplotlib.pyplot as plt
  
def create_leaderboard(name):
  user_dict = p.create_user_dictionary()
  print(user_dict)
  name = p.capitalize_firstletter(name)
  for user, data in user_dict.items():
    print(data[name])
  #sorts the dictionary items by the 1st index of the tuple of the value of bench, reverse=True is most weight to       lowest
  
  # sorted_dict = sorted(user_dict.items(), key=bench_key, reverse=True)
  #print(sorted_dict.items())
  sorted_dict = sorted(user_dict.items(), key=lambda x: float(x[1][name]), reverse=True)
  #sorted_list = [(user, stats) for user, stats in sorted_dict]
  return sorted_dict

def leaderboard(name):
  checker = False
  name = p.capitalize_firstletter(name)
  
  if name.lower() == "pullups" or name.lower() == "pushups": 
    unit = "reps."
  else:
    unit = "lbs."
  leaderboard_list = create_leaderboard(name) 
  return name, unit, leaderboard_list
    
  