###########################################################################
#                 PARSE_PRLIST_TXT PROGRAM FILE                           #
###########################################################################
# Functionality: Implements all the functionality of adding, removing,    #
# and editing, userPRs                                                    #
# Contributors: Anthony Le, Aaron Mai, Andy Iliesi                        #
# Date Created: 8/11/2023                                                 #
# Last Updated: 8/12/2023 Anthony                                         #
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
#  "User": None,
#  "Bench": None,
#  "Squat": None, 
#  "Deadlift": None, 
#  "Pullups": None, 
#  "Pushups": None
#}

# ########################################### NOTES ############################################
# enumerate() - allows you to keep track of the number of iterations (loops) in a loop
# strip() - remove the characters from the beginning or end of the string for the characters
# 'in' - is a keyword used to check for membership in a sequence or collection.
# '.join' - takes all the elements of an iterable and joins them into a single string

# Opens the txt file and returns it
def open_txt_file(txtfile_path):
  with open(txtfile_path, 'r') as file:
    content = file.read()
  return content

# Writes in the file
def write_txt_file(txtfile_path, userPRs_dict,name):  
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
def user_checker(txtfile_path, userPRs_dict,name):
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

# Adds a pr
def add_pr(userPRs_dict, pr_name):
  # Var to database filepath
  txtfile_path = "database//pr_list.txt"

  print("User Checker = ",user_checker(txtfile_path, userPRs_dict,"User")) # To Debug user_checker
  
  # If user is not detected will create a new database for user
  if user_checker(txtfile_path, userPRs_dict,"User") == False: # Check Boolean
    # Adds new user bench pr to pr_list.txt
    if pr_name.lower() == "bench":
      write_txt_file(txtfile_path, userPRs_dict, pr_name)
      return True
      
    elif pr_name.lower() == "squat":
      write_txt_file(txtfile_path, userPRs_dict, pr_name)
      return True
      
    elif pr_name.lower() == "deadlift":
      write_txt_file(txtfile_path, userPRs_dict, pr_name)
      return True
      
    elif pr_name.lower() == "pullups":
      write_txt_file(txtfile_path, userPRs_dict, pr_name)
      return True
      
    elif pr_name.lower() == "pushups":
      write_txt_file(txtfile_path, userPRs_dict, pr_name)
      return True
      
  # This is if the user is already detected in the database
  else:
    if pr_name.lower() == "bench":
      print("USER BENCH = ",userPRs_dict["Bench"])
      edit_txt_user(txtfile_path, userPRs_dict["User"], "Bench", userPRs_dict["Bench"])
      return True
      
    elif pr_name.lower() == "squat":
      print("USER SQUAT = ",userPRs_dict["Squat"])
      edit_txt_user(txtfile_path, userPRs_dict["User"], "Squat", userPRs_dict["Squat"])
      return True
      
    elif pr_name.lower() == "deadlift":
      print("USER DEADLIFT = ",userPRs_dict["Deadlift"])
      edit_txt_user(txtfile_path, userPRs_dict["User"], "Deadlift", userPRs_dict["Deadlift"])
      return True
      
    elif pr_name.lower() == "pullups":
      print("USER PULLUPS = ",userPRs_dict["Pullups"])
      edit_txt_user(txtfile_path, userPRs_dict["User"], "Pullups", userPRs_dict["Pullups"])
      return True
      
    elif pr_name.lower() == "pushups":
      print("USER PUSHUPS = ",userPRs_dict["Pushups"])
      edit_txt_user(txtfile_path, userPRs_dict["User"], "Pushups", userPRs_dict["Pushups"])
      return True

  # If nothing works
  return False

############### NEEDS WORK ################
def set_userPRs(txtfile_path, userPRs_dict, user):
  checker = False
  return checker

############### NEEDS WORK ################
def setCurrent_userStats(user, userPRs_dict):
  # Sets/Declares Var
  txtfile_path = "database//pr_list.txt"
  
  new_userPRs_dict = set_userPRs(txtfile_path, userPRs_dict, user) # Returns values from database associated with the user
  
  return new_userPRs_dict

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
      return None
    
  except FileNotFoundError:
      print("File not found.")
      return None
  return None
  
def display_stats(user_id):
  txtfile_path = "database//pr_list.txt"
  stats = user_checker_display(txtfile_path, user_id)
  
  if not stats:
    raise Exception("No lifts recorded")
  return stats