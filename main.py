# This code is based on the following example:
# https://discordpy.readthedocs.io/en/stable/quickstart.html#a-minimal-bot
#test
# Libraries
import discord
import os
import keep_alive

# Initializes Vars
name_list = []

# Initializes dict vars
bench_PR = "" 
squat_PR = ""
deadlift_PR = ""
pullup_PR = ""
pushup_PR = ""
name = ""

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

user_states = {}
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
  
  if message.author.id in user_states:
    state = user_states[message.author.id]
    if state == 'bench' and msg.startswith('!pr'):
      userPRs_dict["Bench"] = msg.split(' ')[1]
      userPRs_dict["User"] = message.author.mention
      
      await message.channel.send("{} PR for bench is:{}".format(userPRs_dict["User"],userPRs_dict["Bench"]))
      del user_states[message.author.id]
      return
      
  # Displays all the commands that the bot can use
  if msg.startswith('!help'):
    help_var = '### "!help" - Displays the commands that can be used.' + '\n### "!hello" - Displays hello to the you.' + '\n### "storepr" - Stores your workout PRs. # Note work in progress' + '\n ### "displaypr [user]" - Displays user\'s PR\'s. # Note work in progress`'
    await message.channel.send(help_var)

  # Says Hello to the user
  elif msg.startswith('!hello') or msg.startswith('!hi') or msg.startswith('!hey'):
    await message.channel.send(f'### Hello there {message.author.mention}!')
  
  # Says Hello to the user
  elif msg.startswith('!storepr'):
    await message.channel.send(f'### Hello there {message.author.mention}! what PR would you like to store:')
    await message.channel.send(f'### `[!Bench, !Squat, !Deadlift, !Pullups, !Pushups]`')
    
    msg = (message.content).lower()
      
      #if msg == "!bench" or msg == "!squat" or msg == "!deadlift" or msg == "!pullups" or msg == "!pushups":
  elif msg == '!bench':
      user_states[message.author.id] = 'bench'
      await message.channel.send('### You have chosen bench. Enter your PR (!pr "num"):')

      '''# Supposedly stops infinite loop
      @client.event
      async def on_message(message):
        if message.author == client.user:
          return

        # lowercases user command cause bot is dumb as fuck
        msg = (message.content).lower()
        
        input_text = msg
        keyword = "!pr"
        index = input_text.find(keyword)
        
        if index != -1:
            pr_var = keyword
            remaining_text = input_text[index + len(keyword):].strip()
            bench_PR = remaining_text
        else:
            pr_var = None
            bench_PR = None

        if pr_var == "!pr":
          userPRs_dict["Bench"] = bench_PR
          userPRs_dict["User"] = message.author.mention
          
        await message.channel.send("{} PR for bench is: {}".format(userPRs_dict["User"],userPRs_dict["Bench"]))'''
            

  # hidden easter egg
  elif msg.startswith('!fuck you') or msg.startswith('!fuckyou'):
    await message.channel.send(f'### NO FUCK YOU {message.author.mention} BITCH!')

  elif msg.startswith('!stats'):
    if userPRs_dict['User']:
      await message.channel.send(f'Stats for {userPRs_dict["User"]}')
      
      for lift in userPRs_dict:
        if lift != 'User':
          await message.channel.send(f'{lift}: {userPRs_dict[lift]}')
    else:
      await message.channel.send("No lifts recorded")
      
      
# Keeps Bot Up 24/7
keep_alive.keep_alive()

# Random shit that runs the bot using token
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
