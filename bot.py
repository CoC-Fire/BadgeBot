# Importing the required modules
import discord
import requests
from discord.ext import commands

# Text brick to walk you through the process
print("Hello! You're on your way to getting Discord's Active Developer Badge!")
print("I'll walk you through how to do this.")
print("")
print("First of all, you'll need to go to https://discord.com/developers in your browser")
print("and make a new application.")
print("")
print("Next, after you name it and everything (you can use whatever you want for the name), you'll")
print("want to go to the tab on the left menu that says bot and click that one thing to add a bot")
print("")
print("After this, you'll want to make a separate server just for this bot, then create an invite link for your bot.")
print("You can create the link by going to OAuth2 and clicking on URL Generator.")
print("Now, after you do this, in scopes, check the boxes for bot and applications.commands")
print("Then scroll down and check the box for Send Messages under text permissions and copy the generated url")
print("")
print("After you do that, just go to that link, add the bot to your server, then go back to the developer portal")
print("")
print("")
# Collection the Application ID and the bot token
print("Now, here comes the tricky part...")
app_id = input("I need you to go to the General Information tab, copy the Application ID, then paste it here: ")
bot_token = input("When you got that done, go to the Bot tab, click on reset token, then copy the token and paste it here: ")
print("")
print("")
print("")
print("After you got that done, just go to your server, type '/hi', then cick enter. I'll respond by saying Hi, and after")
print("a while, check back in the discord developer portal, and you'll be able to claim your badge.")
print("")
print("")
print("WARNING: MAKE SURE THAT YOU RUN THIS AT LEAST ONCE A MONTH, OR YOU WILL LOSE YOUR BADGE!")
print("")
print("Anyway, please remember to subscribe to my YouTube channel at https://youtube.com/c/CoCFire and share it with your friends!")
print("Have fun with your badge!")

# Setting the URL to add the command to
url = "https://discord.com/api/v10/applications/{app_id}/commands"

# Creating the custom command
json = {
    "name": "hi",
    "type": 1,
    "description": "hi",
}
# Telling discord that it's really you and not some random hacker
headers = {
    "Authorization": f"Bot {bot_token}",
    "Content-Type": "application/json",
}

response = requests.post(url, headers=headers, json=json)
# Basically tells you whether or not the command was added successfully
if response.status_code == 201:
    print("Custom command created successfully")
else:
    print(f"Error creating custom command: {response.status_code}")
# Setting up the bot
intents = discord.Intents.default()
bot = commands.Bot(intents=intents,command_prefix="/")
# Making it into a chatbot with a very limited vocabulary
@bot.tree.command()
async def hi(interaction: discord.Interaction):
    await interaction.response.send_message("hi")
# Making the bot RUUUUUUUUUUUN
bot.run(bot_token)
