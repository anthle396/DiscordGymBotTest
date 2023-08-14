###########################################################################
#                          KEEP_ALIVE PROGRAM FILE                        #
###########################################################################
# Functionality: # This File Basically calls this website called          #
# https://uptimerobot.com/dashboard#mainDashboard                         #
# And It Will Run 24/7                                                    #         
# Contributors: Anthony Le                                                #
# Date Created: 8/11/2023                                                 #
# Last Updated: 8/11/2023                                                 #
###########################################################################

# Libraries
from flask import Flask
from threading import Thread

# Dont know exactly what these do but keeps the program running
app = Flask('')

@app.route('/')
def main():
  return "Your bot is alive!"

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    server = Thread(target=run)
    server.start()