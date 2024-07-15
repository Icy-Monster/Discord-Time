import requests
import time
from datetime import datetime
import pytz

Token = "" # Set this to your Discord account token- https://www.geeksforgeeks.org/how-to-get-discord-token/
TimeZone = pytz.timezone('CET')

def ChangeTime(Token):
    Request = requests.patch(
        "https://discord.com/api/v9/users/%40me/profile",

         headers = {
             "Authorization": f"{Token}"
         },

        # You should change this if you want to include anything else in your BIO
         json = {
             "bio": "**Time `" + datetime.now(pytz.utc).astimezone(TimeZone).strftime('%I:%M %p').lstrip('0') + "`**"
         },
    )


    # This is just to be safe, so that Discord doesn't think you're a bot
    if Request.status_code != 200:
        time.sleep(300)
        print(" !!! DISCORD RETURNED ERROR CODE OF " + str(Request.status_code) +", FOR SAFETY APP WILL BE TIMED OUT FOR 5 MINUTES !!!")

# Immediately set the bio once this is ran, then every minute
ChangeTime()

while True:
    ChangeTime()
    time.sleep(60 - (time.time() % 60))