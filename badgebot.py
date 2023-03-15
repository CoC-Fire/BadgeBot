import os # This is meant to make sure everything is installed and ready to go.
os.system('pip install discord requests')
# Importing the required modules
import discord
import requests
from discord.ext import commands

# Text brick to walk you through the process
print("Hello! I'm here to help you get Discord's active developer badge!\n")
print("First of all, you'll need to go to https://discord.com/developers in your browser and make a new application\n")
print("Once you have created the bot, scroll down until you see the application id and click on the blue button that says copy.")
app_id = input("Now, paste the application id here: ")
print("\n\n")
print(f"Now, you'll need to create the bot account by going to https://discord.com/developers/applications/{app_id}/bot and clicking on the blue add bot button.")
token = input("Underneath the bot's username, you'll see two buttons. You're going to need to click the blue button which says copy, then paste that into here: ")
print("Alright, now that all of that's out of the way, I would recommend creating a new server for this bot.")
print(f"Once you've done that, you can click here to add the new bot to your server: https://discord.com/api/oauth2/authorize?client_id={app_id}&permissions=2048&scope=bot%20applications.commands")
print("\n\n\n")
print("After you add the bot to your server, just use the '/hi' command to get the active developer badge!")
print("It is a good idea to keep in mind that you may need to open discord from your browser for the commands to update.\nAlso, it will usually take around 24 hours for you to get your badge, but be patient! it will happen!")
print("24 hours after you use '/hi' and I respond, check the discord developer portal, and you should be able to claim your badge.\n")
print("WARNING: MAKE SURE THAT YOU RUN THIS AT LEAST ONCE A MONTH, OR YOU WILL LOSE YOUR BADGE!\n")
print("Anyway, please remember to subscribe to my YouTube channel at https://youtube.com/c/CoCFire and share it with your friends!")
print("Have fun with your badge!")

# Setting the URL to add the command to
url = f"https://discord.com/api/v10/applications/{app_id}/commands"

try:
    # Creating the custom command
    json = {
        "name": "hi",
        "type": 1,
        "description": "hi",
    }
    # Telling discord that it's really you
    headers = {
        "Authorization": f"Bot {token}",
        "Content-Type": "application/json",
    }

    requests.post(url, headers=headers, json=json)
# Giving a description of an error in case one occurs
except Exception as e:
    print(f"Well, something happened. Here's an explaination if you want it:\nError: {e}\nIt's probably fine, but if it isn't, please contact me on discord CoCFire#1111 for help.")
# Setting up the bot's intents
intents = discord.Intents.default()
bot = commands.Bot(intents=intents,command_prefix="/")
@bot.tree.command()
async def hi(interaction: discord.Interaction):
    await interaction.response.send_message("Hi! Great work!")
bot.run(token)
