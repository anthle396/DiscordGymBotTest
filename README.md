# Gym Discord Bot
![Bot Display](GymBotTesting/Bot_Profile2.png)

---

## Table of Contents
- [Section 1: Introduction](#section-1-introduction)
- [Section 2: How It Works](#section-2-how-it-works)
  - [Database](#database)
- [Section 3: Usage](#section-3-usage)
  - [Commands](#commands)
    - [Help](#help)
    - [Hello](#hello)
    - [Storepr](#storepr)
    - [Stats](#stats)
    - [Conversions](#conversions)
    - [Leaderboard](#leaderboard)

---

## Section 1: Introduction

### Introduction/Inspiration
The idea for this bot came from me and my friend constantly wondering why there wasn’t a Discord bot to track gym statistics. As gym enthusiasts and coders, we decided it was time to change that. I didn’t want to host the bot on my own computer, so I found a site called Repl.it, which acts as a cloud-based IDE that can compile, run, and store my code. After doing some research, I discovered I could keep the bot running 24/7 by using another service called Uptime.com to monitor the website.

Since I wasn’t familiar with storing databases, I reached out to a friend who had experience in this area. He suggested using simple .txt file as a start, as he’d used them in a class before. While this project isn’t for professional use and might have some bugs or lack polished visuals, it’s been a great learning experience and a fun way to bring our idea to life.

### Section 2: How It Works

### Description
This bot utilizes python to store gym personal records and displays them on discord for you to track and see eachother on the leaderboard. So far the leaderboard is on all servers that the bot is on since the database is not on a per server basis.

![Bot Display](GymBotTesting/Bot_Profile.png)

`Figure 1: This is what the display would like like if the user clicked on the bot's profile.`


### Database
The database works by using a .txt file which has dictionaries stored into it and has a '|' delimiter that separates between users to know that you have reached a new user.
All this data is stored on one line so the algorithm uses function that searches the one line until it reaches the delimiter to find specified data and ',' for the data personal record type.

![Bot Display](GymBotTesting/userpr_database.png)

`Figure 2: Shows the user's personal record database.`

Note* PR - Personal Record
### Order Of Database

| User ID    | PR Type | data (in lbs/reps) | Delimiter | Delimiter |
|------------| --------| -------------------|---------------|---------|
| The discord's user id | Type of PR | The data in lbs or reps | The delimtier ',' to separate pr data types | Depending on how many pr types there are it will keep repeating pr type, data, and delimiter ',' until eventuall reaching the line which separates different user data |

### Section 3: Usage

### Commands
The commands are listed as followed from [help_commands.txt](database/help_commands.txt)

| Command          | Description                                         |
|------------------|-----------------------------------------------------|
| `!`              | All commands are started with a !                   |
| `!help`          | Displays the commands that can be used.             |
| `!hello`         | Displays hello to you.                              |
| `!storepr`       | Displays all options to store for Personal Records (pr).|
| `!stats`         | Displays user's PR's.                               |
| `!conversions`   | Displays all possible conversions.                  |
| `!leaderboard`   | Displays the leaderboard of PRs of everyone. Note that this takes a little longer to load. |

### Here are some outputs of how the commands would be displayed to for the user:

---

#### Help
![Bot Help](GymBotTesting/Help.png)

`Figure 3: This will display all commands the bot has to offer from !help.`

---

#### Hello
![Bot Hello](GymBotTesting/Hello.png)

`Figure 4: This will greet the user if they say !hello/hi/hey.`

---

#### Storepr
![Bot Storepr](GymBotTesting/storepr.png)
![Bot Storepr](GymBotTesting/storeprbench.png)

`Figure 5: !Storepr [lift] will store your pr stats into the database.`

---

#### Stats
![Bot Stats](GymBotTesting/stats.png)

`Figure 6: This will show your individual stats from the database if !stats is called.`

---

#### Conversions
![Bot conversions](GymBotTesting/conversions.png)

`Figure 7: !Storepr [lift] will store your pr stats into the database.`

---

#### Leaderboard
![Bot Storepr](GymBotTesting/leaderboard.png)

`Figure 8: !Leaderboard displays the ranking based on everyone in the database on who is the strongest/best`

---
