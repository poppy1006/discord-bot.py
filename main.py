from email import message
import discord
from dotenv import load_dotenv
import os


 
load_dotenv()
TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)




@client.event # Bot status #
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name = 'bot.py'))


@client.event
async def on_member_join(member):
    guild = client.get_guild(890866780946464808) #guils id #
    channel = guild.get_channel(890866780946464811) #Channel id#
    await channel.send(f'Welcome to the server {member.mention} ! :partying_face:')  ## Welcome the member to the  server ##
    await member.send(f'Welcome to the {guild.name} server,{member.name}!!') ##Welcomes the user via dm ##


@client.event
async def on_message(message):
    if message.content == 'hi':
        await message.channel.send('Hello!!')
    if message.content == 'Hi':
        await message.channel.send('Hello!!')





## connection success message in terminal ##
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')






client.run(TOKEN)