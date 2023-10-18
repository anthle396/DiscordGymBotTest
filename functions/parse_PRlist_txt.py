###########################################################################
#                 PARSE_PRLIST_TXT PROGRAM FILE                           #
###########################################################################
# Functionality: Implements all the functionality of adding, removing,    #
# and editing, userPRs                                                    #
# Contributors: Anthony Le, Aaron Mai, Andy Iliesi                        #
# Date Created: 8/11/2023                                                 #
# Last Updated: 8/18/2023 Anthony, Aaron                                  #
###########################################################################

###################### TASKS NEEDED TO FINISH #############################
# NEEDS WORK - Need someone to do that shit                               #
# Check - Check/Debug if function is outputting correct return            #
###########################################################################

########## REFERENCES ############

# The Help Commands Database
# database/help_commands.txt

# The PR_List Database
# https://replit.com/@AnthonyLe12/GymTest#database/pr_list.txt

# Delimiter = |

#userPRs_dict = {
#  "User": 0.0,
#  "Bench": 0.0,
#  "Squat": 0.0, 
#  "Deadlift": 0.0, 
#  "Pullups": 0.0, 
#  "Pushups": 0.0
#}

# ########################################### NOTES ############################################
# enumerate() - allows you to keep track of the number of iterations (loops) in a loop
# strip() - remove the characters from the beginning or end of the string for the characters
# 'in' - is a keyword used to check for membership in a sequence or collection.
# '.join' - takes all the elements of an iterable and joins them into a single string

import math

# Opens the txt file and returns it
def open_txt_file(txtfile_path):
  with open(txtfile_path, 'r') as file:
    content = file.read()
  return content

# Writes in the file
def write_txt_file(txtfile_path, userPRs_dict):  
  with open(txtfile_path, 'a') as file:
    file.write(f"{userPRs_dict}|") # '|' is the delimiter
  return True

# Searches through the dictionaries until it finds the name
def edit_txt_user(txtfile_path, target_user, option, new_value):
  try:
      with open(txtfile_path, 'r') as file:
          content = file.read()

      user_entries = content.split('|')  # Split by '|' to separate user entries
      updated_entries = []

      for entry in user_entries:
          if target_user in entry:
              entry_parts = entry.strip().split(', ') 
              for i, part in enumerate(entry_parts): 
                  if f"'{option}': " in part:
                      entry_parts[i] = f"'{option}': '" + new_value + "'"
                      break  # Stop replacing after the option value is found
              updated_entries.append(', '.join(entry_parts))
          else:
              updated_entries.append(entry)

      updated_content = '|'.join(updated_entries)
      with open(txtfile_path, 'w') as file:
          file.write(updated_content)

      return True
  except FileNotFoundError:
      print("File not found.")
      return False

# Checks is user is already in list
def user_checker(txtfile_path, userPRs_dict, name):
  try:
      with open(txtfile_path, 'r') as file:
          for line in file:
              if userPRs_dict[name] in line:
                  return True
          return False
  except FileNotFoundError:
      print("File not found.")
      return False
  return False

def clear_dict(userPRs_dict, pr_name):
  temp = userPRs_dict[pr_name]
  temp_name = userPRs_dict["User"]
  for item in userPRs_dict:
    userPRs_dict[item] = 0.0
  userPRs_dict["User"] = temp_name
  userPRs_dict[pr_name] = temp
  return userPRs_dict
  
# Adds a pr
def add_pr(userPRs_dict, pr_name):
  # Var to database filepath
  txtfile_path = "database//pr_list.txt"

  print("User Checker = ",user_checker(txtfile_path, userPRs_dict,"User")) # To Debug user_checker
  
  # If user is not detected will create a new database for user
  if user_checker(txtfile_path, userPRs_dict,"User") == False: # Check Boolean
    # Adds new user weight to pr_list.txt
    if pr_name.lower() == "weight (lbs)":
      userPRs_dict = clear_dict(userPRs_dict, pr_name)
      write_txt_file(txtfile_path, userPRs_dict)
      return True
    # Adds new user bench pr to pr_list.txt
    elif pr_name.lower() == "bench (lbs)":
      userPRs_dict = clear_dict(userPRs_dict, pr_name)
      write_txt_file(txtfile_path, userPRs_dict)
      return True
      
    elif pr_name.lower() == "squat (lbs)":
      userPRs_dict = clear_dict(userPRs_dict, pr_name)
      write_txt_file(txtfile_path, userPRs_dict)
      return True

    elif pr_name.lower() == "deadlift (lbs)":
      userPRs_dict = clear_dict(userPRs_dict, pr_name)
      write_txt_file(txtfile_path, userPRs_dict)
      return True
      
    elif pr_name.lower() == "pullups (reps)":
      userPRs_dict = clear_dict(userPRs_dict, pr_name)
      write_txt_file(txtfile_path, userPRs_dict)
      return True
      
    elif pr_name.lower() == "pushups (reps)":
      userPRs_dict = clear_dict(userPRs_dict, pr_name)
      write_txt_file(txtfile_path, userPRs_dict)
      return True
      
  # This is if the user is already detected in the database
  else:
    if pr_name.lower() == "weight (lbs)":
      print("USER BENCH = ",userPRs_dict[pr_name])
      edit_txt_user(txtfile_path, userPRs_dict["User"], pr_name, str(userPRs_dict[pr_name]))
      return True
      
    elif pr_name.lower() == "bench (lbs)":
      print("USER BENCH = ",userPRs_dict[pr_name])
      edit_txt_user(txtfile_path, userPRs_dict["User"], pr_name, str(userPRs_dict[pr_name]))
      return True
      
    elif pr_name.lower() == "squat (lbs)":
      print("USER SQUAT = ",userPRs_dict[pr_name])
      edit_txt_user(txtfile_path, userPRs_dict["User"], pr_name, str(userPRs_dict[pr_name]))
      return True
      
    elif pr_name.lower() == "deadlift (lbs)":
      print("USER DEADLIFT = ",userPRs_dict[pr_name])
      edit_txt_user(txtfile_path, userPRs_dict["User"], pr_name, str(userPRs_dict[pr_name]))
      return True
      
    elif pr_name.lower() == "pullups (reps)":
      print("USER PULLUPS = ",userPRs_dict[pr_name])
      edit_txt_user(txtfile_path, userPRs_dict["User"], pr_name, str(userPRs_dict[pr_name]))
      return True
      
    elif pr_name.lower() == "pushups (reps)":
      print("USER PUSHUPS = ",userPRs_dict[pr_name])
      edit_txt_user(txtfile_path, userPRs_dict["User"], pr_name, str(userPRs_dict[pr_name]))
      return True

  # If nothing works
  return False

#checks to see if user exists, and if they do, extract their stats
def user_checker_display(txtfile_path, user_id):
  try:
      with open(txtfile_path, 'r') as file:
        content = file.read()
        entries = content.split('|')
        
        for entry in entries:
          if user_id in entry:
            # Extract only the information inside the curly braces
              data = entry[entry.find("{")+1:entry.find("}")]
              stats = {}
              for item in data.split(','):
                  # Splitting by ':' gives us the key and value for each item
                  key, value = item.split(':')
                  key = key.strip().strip("'")
                  value = value.strip().strip("'")
                  stats[key] = value
              return stats
      return 0.0
    
  except FileNotFoundError:
      print("File not found.")
      return 0.0
  return 0.0

#display stats when given user id
def display_stats(user_id):
  txtfile_path = "database//pr_list.txt"
  stats = user_checker_display(txtfile_path, user_id)
  
  if not stats:
    raise Exception("No Health Stats Recorded")
  return stats

#idk how this works, chatgpt wrote it
def extract_data_from_entry(entry):
    # Removing curly braces from the entry
    entry = entry.strip("{}")
    
    data = {}
    for item in entry.split(','):
        # Separating the key and value based on the first occurrence of ":"
        parts = item.split(':', 1)
        
        if len(parts) == 2:
            key, value = parts
            key = key.strip().strip("'").strip('"')
            value = value.strip().strip("'").strip('"')
            data[key] = value
    
    return data
  
#nested dictionary of weight and bench
def create_user_dictionary():
  
  txtfile_path = "database//pr_list.txt"
  content = open_txt_file(txtfile_path)
  entries = content.split('|')
  user_dict = {}

  for entry in entries:
    if entry:
      data = extract_data_from_entry(entry)
      if 'User' in data:
        user = data['User']
  
        user_dict[user] = {
          'Bench': data.get('Bench (lbs)', 0.0),
          'Weight': data.get('Weight (lbs)', 0.0),
          "Squat": data.get('Squat (lbs)', 0.0),
          "Deadlift": data.get('Deadlift (lbs)', 0.0),
          "Pullups": data.get('Pullups (reps)', 0.0),
          "Pushups": data.get('Pushups (reps)', 0.0),
        }
    
  return user_dict
  
def capitalize_firstletter(name):
  name1 = name[0].capitalize()
  name2 = name[1:]
  name = name1 + name2
  return name
  
def check_correct_prname(name):
 # Set Vars
  checker = False
  name_list = ["Bench","Squat","Deadlift","Weight","Pullups","Pushups"]

  # Searches if name has names in list
  for i in range(len(name_list)):
    if name == name_list[i].lower():
      checker = True
      return checker
  return checker

def setpr_name(name):
  # Sets vars
  name_list = ["Bench","Weight","Squat","Deadlift","Pullups","Pushups"]
  name_list_dict = ["Bench (lbs)","Weight (lbs)","Squat (lbs)","Deadlift (lbs)","Pullups (reps)","Pushups (reps)"]
  
  for i in range(len(name_list)):
    if name.lower() == name_list[i].lower():
      name = name_list_dict[i]
      return name

  return "N/A"

   