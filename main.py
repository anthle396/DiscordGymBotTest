###########################################################################
#                          MAIN PROGRAM FILE                              #
###########################################################################
# Functionality: This program will store your gym prs                     #
# and other gym necesities                                                #
# Contributors: Anthony Le, Aaron Mai, Andy Iliesi                        #
# Date Created: 8/11/2023                                                 #
# Last Updated: 8/15/2023 Aaron, Anthony                                  #
###########################################################################
# idk what this is but it was here in the discord template.               #
# This code is based on the following example:                            #
# https://discordpy.readthedocs.io/en/stable/quickstart.html#a-minimal-bot#
###########################################################################

################# TASKS NEEDED TO BE COMPLETED ############################
#  When Tasks Are Completed Remember To Delete Them*                      
# - Work On Health Calc fixing calculations
# - Implement a set userHealth 
# - Implement if userHealth is filled out or checks to see if value is None
#  - Brainstorm additional ideas                                            


############################## IDEAS? ############################
# - Implement protein calculator per weight (could do this by using other websites)
# - Vertical calculator 
# - Implement whether user choses to bulk or cut and display calculated protein and calorie intake per day
# - implement graphs for leaderboard using PANDAS
# - gif of them hitting the pr

# Libraries
import numpy as np
import discord
import os
from functions import keep_alive
from functions import parse_PRlist_txt as pt
from functions import conversions as c
from functions import leaderboard as board
from discord.ext import commands
from functions import parse_healthlist_txt as health
from functions import healthcalc
# CREATES A NEW BOT OBJECT WITH A SPECIFIED PREFIX. IT CAN BE WHATEVER YOU WANT IT TO BE.
bot = commands.Bot(command_prefix="!")

# Activates client or smth idk
intents = discord.Intents.default()
intents.messages = True
client = discord.Client(intents=intents)
  
# Dict Var for userPRs
userPRs_dict = {
  "User": "N/A",
  "Weight (lbs)": 0.0,
  "Bench (lbs)": 0.0,
  "Squat (lbs)": 0.0, 
  "Deadlift (lbs)": 0.0, 
  "Pullups (reps)": 0.0, 
  "Pushups (reps)": 0.0
}

# Dict Var for healthstats
userHealth = {
  "User": "N/A",
  "Age (year)": 0,
  "Gender (m/f)": "N/A",
  "Height (in)": 0.0,
  "Weight (lbs)": 0.0, 
  "Activity (days)": 0.0
}

# Informs client that bot is online
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

# Activates from a message or reaction
@client.event
# idk what this does but makes it not infinitely loop
async def on_message(message):
  if message.author == client.user:
    return

  # lowercases user command cause bot is dumb as fuck
  msg = (message.content).lower()
  
    # Once this is finished re-add the Try Except To This
  ###################STORE PR STATS###########################
  
    ################# ADD BODY WEIGHT ########################
  if msg.startswith('!storepr'): 
    arguments = msg.split()

    #no extra command line args
    if len(arguments) == 1:
      # Displays the types of options to store
      await message.channel.send(f'### Hello there {message.author.mention}!\n' + f'### To store a pr do !storepr [lift]' + f' `Lifts = [weight, bench, squat, deadlift, pullups, pushups]`\nEverything is defaulted to lbs') 
      
    #extra commands line args
    elif len(arguments) == 3:
      user = message.author.mention
      try:
        # Stores name and lift_val
        name = arguments[1].lower()
        lift_value = float(arguments[2])
        if np.isnan(lift_value):
          lift_value = 0.0
        
        if (lift_value <= 0.0 or lift_value >= 9999.99):
          print(undefined_variable) # Creates an error

        print(lift_value)
        
        # Formats so that add_pr understands and correct input and stores userPRs
        if pt.check_correct_prname(name) == True:
          userPRs_dict["User"] = message.author.mention
          name = pt.capitalize_firstletter(name)
          pr_name = pt.setpr_name(name)
          userPRs_dict[pr_name] = lift_value
          
          # Adds pr to txt database
          pt.add_pr(userPRs_dict, pr_name)
          # To Check/Debug userPRs
          print(userPRs_dict["User"])
          print(userPRs_dict[pr_name])
          print(userPRs_dict)
          
          # Outputs user's pr
          await message.channel.send(f"{user}'s PR for {name} is {userPRs_dict[pr_name]}.")
      except:
          await message.channel.send(f"Hey {user}, not a valid number dummy!")
    ################# ADDS AGE STATS ########################
  elif msg.startswith('!storehealth age'): 

    (temp1,temp2,userHealth["Age (year)"]) = msg.split(" ")
    print("User =",userHealth["Age (year)"])
    userHealth["Age (year)"] = int(userHealth["Age (year)"])
    userHealth["User"] = message.author.mention
    await message.channel.send("Age of {}: {} years old.".format(userHealth["User"],userHealth["Age (year)"]))
    health.add_health(userHealth,"Age (year)")


   ################# ADDS GENDER STATS ########################
  elif msg.startswith('!storehealth gender'): 
    try:
      (temp1,temp2,userHealth["Gender (m/f)"]) = msg.split(" ")
      userHealth["User"] = message.author.mention
      print("USER GENDER =",userHealth["Gender (m/f)"])
      if userHealth["Gender (m/f)"].lower() == 'm' or userHealth["Gender (m/f)"].lower() == 'male':
        userHealth["Gender (m/f)"] = 'm'
        await message.channel.send("{}'s' Gender is: {}.".format(userHealth["User"],"Male"))
      elif userHealth["Gender (m/f)"].lower() == 'f' or userHealth["Gender (m/f)"].lower() == 'female':
        userHealth["Gender (m/f)"] = 'f'
        await message.channel.send("{}'s' Gender is: {}.".format(userHealth["User"],"Female"))
      else:
        userHealth["Gender (m/f)"] = None
        
      print("USER GENDER =",userHealth["Gender (m/f)"])
      health.add_health(userHealth,"Gender (m/f)")
    except:
      print("Invalid Input")

  ################# ADDS HEIGHT STATS ########################
  elif msg.startswith('!storehealth height'): 
    try:
      (temp1,temp2,userHealth["Height (in)"]) = msg.split(" ")
      userHealth["Height (in)"] = float(userHealth["Height (in)"])
      userHealth["User"] = message.author.mention
      await message.channel.send("{}'s' Height currently is: {} in.".format(userHealth["User"],userHealth["Height (in)"]))
      health.add_health(userHealth,"Height (in)")

    except:
      print("Invalid Input")
  
  ################# ADDS WEIGHT STATS ########################
  elif msg.startswith('!storehealth weight'): 
    try:
      (temp1,temp2,userHealth["Weight (lbs)"]) = msg.split(" ")
      userHealth["Weight (lbs)"] = float(userHealth["Weight (lbs)"])
      userHealth["User"] = message.author.mention
      await message.channel.send("{}'s' Weight currently is: {} lbs.".format(userHealth["User"],userHealth["Weight (lbs)"]))
      health.add_health(userHealth,"Weight (lbs)")

    except:
      print("Invalid Input")  

  ################# ADDS WEIGHT STATS ########################
  elif msg.startswith('!storehealth activity'): 
    try:
      (temp1,temp2,userHealth["Activity (days)"]) = msg.split(" ")
      userHealth["Activity (days)"] = float(userHealth["Activity (days)"])
      userHealth["User"] = message.author.mention
      if userHealth["Activity (days)"] <= 7:
        await message.channel.send("{}'s Daily Activity currently is: {} days a week.".format(userHealth["User"],userHealth["Activity (days)"]))
        health.add_health(userHealth,"Activity (days)")
      else:
        userHealth["Activity (days)"] = None

    except:
      print("Invalid Input")
  
      return
      
  # Displays all the commands that the bot can use
  elif msg.startswith('!help'):
    help_var = pt.open_txt_file("database//help_commands.txt")
    await message.channel.send(help_var)
    
  # Displays all the commands that the bot can use
  elif msg.startswith('!conversions'):
    help_var = pt.open_txt_file("database/conversions.txt")
    await message.channel.send(help_var)

  # Converts lbs to kg
  elif msg.startswith('!lbstokg'):
      try:
        message_unit = float(msg.split(' ')[1])
        await message.channel.send(f"{message_unit} lbs -> {c.lbs_to_kg(message_unit)} kg.")
      except:
         print("This is not a valid answer dummy.")

  # Converts kg to lbs
  elif msg.startswith('!kgtolbs'):
      try:
        message_unit = float(msg.split(' ')[1])
        await message.channel.send(f"{message_unit} kg -> {c.kg_to_lbs(message_unit)} lbs.")
      except:
         print("This is not a valid answer dummy.")

  # Converts kg to lbs
  elif msg.startswith('!fttoin'):
      try:
        message_unit = float(msg.split(' ')[1])
        await message.channel.send(f"{message_unit} ft -> {c.ft_to_in(message_unit)} in.")
      except:
         print("This is not a valid answer dummy.")

  # Converts lbs to kg or vice versa
  elif msg.startswith('!hello') or msg.startswith('!hi') or msg.startswith('!hey'):
    await message.channel.send(f'### Hello there {message.author.mention}!')

  # hidden easter egg
  elif msg.startswith('!fuck you') or msg.startswith('!fuckyou'):
    await message.channel.send(f'### NO FUCK YOU {message.author.mention} BITCH!')
    # Once completed the program pls remove this lol

  # Displays stats of current user
  elif msg.startswith('!stats'):
    arguments = msg.split()

    #no extra command line args
    if len(arguments) == 1:
      user_id = message.author.mention
    #extra commands line args
    elif len(arguments) == 2 and arguments[1].startswith('<@'):
      user_id = arguments[1]
    else:
      await message.channel.send("Invalid command, type !help for list of commands")
      return
      #scan for the user's stats in txt
    try:
      stats = pt.display_stats(user_id)
      await message.channel.send(f"All measurments are weighted in lbs.\n----------------------")
      for item in stats:
        await message.channel.send(f"{item}: {stats[item]}")
    except Exception as e:
      await message.channel.send(e)

    # Displays stats of current user
  elif msg.startswith('!healthstats'):
    arguments = msg.split()

    #no extra command line args
    if len(arguments) == 1:
      user_id = message.author.mention
    #extra commands line args
    elif len(arguments) == 2 and arguments[1].startswith('<@'):
      user_id = arguments[1]
    else:
      await message.channel.send("Invalid command, type !help for list of commands")
      return
      #scan for the user's stats in txt
    try:
      stats = health.display_stats(user_id)
      for item in stats:
        await message.channel.send(f"{item}: {stats[item]}")
    except Exception as e:
      await message.channel.send(e)

  #leaderboard of bench
  elif msg.startswith('!leaderboard'):
    arguments = msg.split()

    #no extra command line args
    if len(arguments) == 1:
      await message.channel.send(f"### To check different leaderboards, do !leaderboard [pr_name].\n### For pr_names, see !healthstats.")
    #extra commands line args
    elif len(arguments) == 2:
      name = arguments[1].lower()
      n = 0
      if pt.check_correct_prname(name) == True:
        name, unit, leaderboard = board.leaderboard(name)
        await message.channel.send(f"| Leaderboard for {name} PR's |\n-----------------------------")
        for user, stats in leaderboard:
          n += 1
          # Displays output  
          await message.channel.send(f"### Rank #{n} | {user} | {stats[name]} {unit}")
  
      

  elif msg.startswith('!storehealth'):
    await message.channel.send(f'### Hello there {message.author.mention}!\n' + f'### To store a health stats do !storehealth [type]' + f'`type = [height(in.), weight(lbs), age, gender(m/f), activity (in days)]`\n') 
    
  # Converts lbs to kg
  elif msg.startswith('!healthcalc'):
    ###### WORK IN PROGRESS
    # FIX CALCULATIONS
    # TEMPORARY VARS NEED TO MAKE FUNC TO SET USERHEALTH
    # ALSO NEED A FUNC TO MAKE SURE USERHEALTH IS FILLED OUT AND   
    message_unit = msg.split(' ')[1]
    print(message_unit)
    
    if message_unit.lower() == "bulk":
      message_unit = "Bulk"
      (protein, calories) = healthcalc.calc_daily_intake(userHealth, message_unit)
    elif message_unit.lower() == "cut":
      message_unit = "Cut"
      (protein, calories) = healthcalc.calc_daily_intake(userHealth, message_unit)
      
    await message.channel.send(f"### According to your health stats {user_id},\n You would need around {protein} g or protein and {calories} calories a day for your option of \'{message_unit}\'")
        
# Keeps Bot Up 24/7
keep_alive.keep_alive()

# Random stuff that runs the bot using token
try:
    client.run(os.getenv("TOKEN"))
except discord.HTTPException as e:
    if e.status == 429:
        print(
            "The Discord servers denied the connection for making too many requests"
        )
        print(
            "Get help from https://stackoverflow.com/questions/66724687/in-discord-py-how-to-solve-the-error-for-toomanyrequests"
        )
    else:
        raise e
