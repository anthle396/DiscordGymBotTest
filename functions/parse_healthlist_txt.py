###########################################################################
#                 PARSE_HEALTHLIST_TXT PROGRAM FILE                       #
###########################################################################
# Functionality: This file stores the healthlist in the healthlist        #
# database                                                                #
# Contributors: Anthony Le                                                #
# Date Created: 8/15/2023                                                 #
# Last Updated: 8/16/2023 Anthony                                         #
###########################################################################

########## REFERENCES ############
# txtfile_path = "database/heathlist.txt"
#
# Dict Var for userPRs
# userHealth = {
#   "User": None,
#   "Age (year)": None,
#   "Gender (m/f)": None,
#   "Height (in)": None,
#   "Weight (lbs)": None, 
#   "Activity (days)": None
# }
################################ 
# Opens the txt file and returns it
def open_txt_file(txtfile_path):
  with open(txtfile_path, 'r') as file:
    content = file.read()
  return content

# Writes in the file
def write_txt_file(txtfile_path, userHealth):  
  with open(txtfile_path, 'a') as file:
    file.write(f"{userHealth}|") # '|' is the delimiter
  return True

# Searches through the dictionaries until it finds the name
def edit_health_user(txtfile_path, target_user, option, new_value):
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
def user_checker(txtfile_path, userHealth, name):
  try:
      with open(txtfile_path, 'r') as file:
          for line in file:
              if userHealth[name] in line:
                  return True
          return False
  except FileNotFoundError:
      print("File not found.")
      return False
  return False

def clear_dict(userHealth, health_name):
  temp = userHealth[health_name]
  temp_name = userHealth["User"]
  for item in userHealth:
    userHealth[item] = None
  userHealth["User"] = temp_name
  userHealth[health_name] = temp
  return userHealth
  
# Adds a pr
def add_health(userHealth, health_name):
  # Var to database filepath
  txtfile_path = "database//heathlist.txt"

  print("User Checker = ",user_checker(txtfile_path, userHealth ,"User")) # To Debug user_checker
  
  # If user is not detected will create a new database for user
  if user_checker(txtfile_path, userHealth,"User") == False: # Check Boolean
    # Adds new age to heathlist.csv
    if health_name.lower() == "age (year)":
      health_name = clear_dict(userHealth, health_name)
      write_txt_file(txtfile_path, userHealth)
      return True
      
    # Adds new gender to heathlist.csv
    elif health_name.lower() == "gender (m/f)":
      health_name = clear_dict(userHealth, health_name)
      write_txt_file(txtfile_path, health_name)
      return True
      
    # Adds new height to heathlist.csv
    elif health_name.lower() == "height (in)":
      health_name = clear_dict(userHealth, health_name)
      write_txt_file(txtfile_path, health_name)
      return True

    # Adds new weight to heathlist.csv
    elif health_name.lower() == "weight (lbs)":
      health_name = clear_dict(userHealth, health_name)
      write_txt_file(txtfile_path, health_name)
      return True

    # Adds new activity to heathlist.csv
    elif health_name.lower() == "activity (days)":
      health_name = clear_dict(userHealth, health_name)
      if userHealth[health_name] <= 7:
        write_txt_file(txtfile_path, health_name)
      else:
        health_name[health_name] = None
      return True
      
  # This is if the user is already detected in the database
  else:
    if health_name.lower() == "age (year)":
      print("USER AGE = ",userHealth[health_name])
      edit_health_user(txtfile_path, userHealth["User"], health_name, str(userHealth[health_name]))
      return True
      
    elif health_name.lower() == "gender (m/f)":
      print("USER GENDER = ",userHealth[health_name])
      edit_health_user(txtfile_path, userHealth["User"], health_name, str(userHealth[health_name]))
      return True
      
    elif health_name.lower() == "height (in)":
      print("USER HEIGHT (In in.) = ",userHealth[health_name])
      edit_health_user(txtfile_path, userHealth["User"], health_name, str(userHealth[health_name]))
      return True
      
    elif health_name.lower() == "weight (lbs)":
      print("USER WEIGHT (In lbs) = ",userHealth[health_name])
      edit_health_user(txtfile_path, userHealth["User"], health_name, str(userHealth[health_name]))
      return True
      
    elif health_name.lower() == "activity (days)":
      print("USER ACTIVITY (In Days) = ",userHealth[health_name])
      if userHealth[health_name] <= 7:
        edit_health_user(txtfile_path, userHealth["User"], health_name, str(userHealth[health_name]))
      else:
        userHealth[health_name] = None
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
      return None
    
  except FileNotFoundError:
      print("File not found.")
      return None
  return None

#display stats when given user id
def display_stats(user_id):
  txtfile_path = "database/heathlist.txt"
  stats = user_checker_display(txtfile_path, user_id)
  
  if not stats:
    raise Exception("No Health Stats Recorded")
  return stats
