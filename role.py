
import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from discord.utils import get



load_dotenv()
TOKEN = os.getenv('TOKEN')




# CREATES A NEW BOT OBJECT WITH A SPECIFIED PREFIX. IT CAN BE WHATEVER YOU WANT IT TO BE.
bot = commands.Bot(command_prefix="!")




@bot.command()
async def ping(ctx):
	await ctx.channel.send("pong")




@bot.event
async def on_message(message):
    if message.author == bot.user :
        return
    await bot.process_commands(message)
     




     
## role assigning ##
@bot.command(pass_context=True)
async def role(ctx,role):
    author = ctx.message.author 
    print(role)
    guild = ctx.guild
    if get(guild.roles, name=role):
        await ctx.send(f"Hi {author.mention},Role already exists")
    else:      
        role_obj = await guild.create_role(name=role)
        await author.add_roles(role_obj)
        await ctx.send(f"hey {author.mention} has assigned a role called: {role}")





        
# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. TOKEN HAS BEEN REMOVED AND USED JUST AS AN EXAMPLE.
bot.run(TOKEN)