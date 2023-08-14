###########################################################################
#                          MAIN PROGRAM FILE                              #
###########################################################################
# Functionality: This program will store your gym prs                     #
# and other gym necesities                                                #
# Contributors: Anthony Le, Aaron Mai, Andy Iliesi                        #
# Date Created: 8/11/2023                                                 #
# Last Updated: 8/12/2023 Anthony                                         #
###########################################################################
# idk what this is but it was here in the discord template.               #
# This code is based on the following example:                            #
# https://discordpy.readthedocs.io/en/stable/quickstart.html#a-minimal-bot#
###########################################################################

################# TASKS NEEDED TO BE COMPLETED ############################
#  When Tasks Are Completed Remember To Delete Them*                      #
# ----------------------------------------------------------------------- #
#  - Implement function to set userPRs_dict from database                 #
#  to make !stats work                                                    #
# - Edit code to implement in an embedded message so that it looks nicer  #
# - display proper stats when they say !stats @name, with no @ then display
#   your own stats normally
#  - Brainstorm additional ideas                                          #
###########################################################################

############################## IDEAS? ############################
# - Possibly add a database for gym schedules? 
# - Implement protein calculator per weight (could do this by using other websites)
# - Vertical calculator 
# - 

# Libraries
import discord
import os
import keep_alive
import parse_PRlist_txt as pt
import conversions as c
from discord.ext import commands

# CREATES A NEW BOT OBJECT WITH A SPECIFIED PREFIX. IT CAN BE WHATEVER YOU WANT IT TO BE.
bot = commands.Bot(command_prefix="!")

# Activates client or smth idk
intents = discord.Intents.default()
intents.messages = True
client = discord.Client(intents=intents)
  
# Dict Var for userPRs
userPRs_dict = {
  "User": None,
  "Bench": None,
  "Squat": None, 
  "Deadlift": None, 
  "Pullups": None, 
  "Pushups": None
}

# Declares Gym Schedule Vars
Mon = []
Tues = []
Wed = []
Thurs = []
Fri = []
Sat = []
Sun = []

gym_schedule = {
  "Monday": Mon,
  "Tuesday": Tues,
  "Wednesday": Wed, 
  "Thursday": Thurs, 
  "Friday": Fri, 
  "Saturday": Sat,
  "Sunday": Sun
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
  
  if msg.startswith('!storepr bench'): 
    # Once this is finished re-add the Try Except To This
    
    ################# ADDS BENCH PR ########################
    
      (temp1,temp2,userPRs_dict["Bench"]) = msg.split(" ")
    
      userPRs_dict["User"] = message.author.mention
      await message.channel.send("{} PR for bench is: {} lbs.".format(userPRs_dict["User"],userPRs_dict["Bench"]))
      pt.add_pr(userPRs_dict,"Bench")
  elif msg.startswith('!storepr squat'): 
    
   ################# ADDS SQUAT PR ########################
    
      (temp1,temp2,userPRs_dict["Squat"]) = msg.split(" ")
      userPRs_dict["User"] = message.author.mention
      await message.channel.send("{} PR for squat is: {} lbs.".format(userPRs_dict["User"],userPRs_dict["Squat"]))
      pt.add_pr(userPRs_dict,"Squat")

  elif msg.startswith('!storepr deadlift'): 
    
    ################# ADDS DEADLIFT PR ########################
    
      (temp1,temp2,userPRs_dict["Deadlift"]) = msg.split(" ")
      userPRs_dict["User"] = message.author.mention
      await message.channel.send("{} PR for deadlift is: {} lbs.".format(userPRs_dict["User"],userPRs_dict["Deadlift"]))
      pt.add_pr(userPRs_dict,"Deadlift")

  elif msg.startswith('!storepr pullups'): 
    
    ################# ADDS PULLUPS PR ########################
    
      (temp1,temp2,userPRs_dict["Pullups"]) = msg.split(" ")
      userPRs_dict["User"] = message.author.mention
      await message.channel.send("{} PR for pullups is: {} lbs.".format(userPRs_dict["User"],userPRs_dict["Pullups"]))
      pt.add_pr(userPRs_dict,"Pullups")

  elif msg.startswith('!storepr pushups'): 
    
    ################# ADDS PUSHUPS PR ########################
    
      (temp1,temp2,userPRs_dict["Pushups"]) = msg.split(" ")
      userPRs_dict["User"] = message.author.mention
      await message.channel.send("{} PR for pushups is: {} lbs.".format(userPRs_dict["User"],userPRs_dict["Pushups"]))
      pt.add_pr(userPRs_dict,"Pushups")

      return
      
  # Displays all the commands that the bot can use
  elif msg.startswith('!help'):
    help_var = pt.open_txt_file("database//help_commands.txt")
    await message.channel.send(help_var)

  elif msg.startswith('!lbstokg'):
      try:
        message_lbs = float(msg.split(' ')[1])
        await message.channel.send(f"{message_lbs} lbs -> {c.lbs_to_kg(message_lbs)} kg.")
      except:
         print("This is not a valid answer dummy.")

  elif msg.startswith('!kgtolbs'):
      try:
        message_kg = float(msg.split(' ')[1])
        await message.channel.send(f"{message_kg} kg -> {c.kg_to_lbs(message_kg)} lbs.")
      except:
         print("This is not a valid answer dummy.")

  # Converts lbs to kg or vice versa
  elif msg.startswith('!hello') or msg.startswith('!hi') or msg.startswith('!hey'):
    await message.channel.send(f'### Hello there {message.author.mention}!')
  
  # Says Hello to the user
  elif msg.startswith('!storepr'):
    await message.channel.send(f'### Hello there {message.author.mention}!\n' + f'### To store a pr do !storepr [lift]' + f'### `Lifts = [!Bench, !Squat, !Deadlift, !Pullups, !Pushups]`\nEverything is defaulted to lbs') 

  # hidden easter egg
  elif msg.startswith('!fuck you') or msg.startswith('!fuckyou'):
    await message.channel.send(f'### NO FUCK YOU {message.author.mention} BITCH!')
    # Once completed the program pls remove this lol

  # Displays stats of current user
  elif msg.startswith('!stats'):
    # userPRs_dict = setCurrent_userStats(message.author.mention, userPRs_dict)
    #no extra command line args
    user_id = message.author.mention
      #scan for the user's stats in txt
    try:
      stats = pt.display_stats(user_id)
      for item in stats:
        await message.channel.send(f"{stats[item]}: {item}")
    except Exception as e:
      await message.channel.send(e)
      
    '''if userPRs_dict['User']:
      await message.channel.send(f'Stats for {userPRs_dict["User"]}')
      
      for lift in userPRs_dict:
        if lift != 'User':
          await message.channel.send(f'{lift}: {userPRs_dict[lift]}')
    else:
      await message.channel.send("No lifts recorded")'''
      
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
