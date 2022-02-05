from http import client
import os
import discord
import mysql.connector
from dotenv import load_dotenv



client = discord.client

load_dotenv()
TOKEN = os.getenv('TOKEN')







lmiibot_db = mysql.connector.connect(
    host="discordbotdatabase...com",
    user="doadmin",
    passwd="password",
    database="lmiibot",
    auth_plugin="mysql_native_password",
)



client.run(TOKEN)
