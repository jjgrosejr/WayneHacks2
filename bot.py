#Using Library Discord.py to communicate with the discord API
#Must be ran in replit unless you want to go through the pain of getting the discord.py library on VS code
import discord
from discord.ext import commands
from noncommandfunctions import superrandint
import time
#all pre-connection code
bot_token = 'OTczMTg0MTA0NDU3NzExNjE2.GQ03ok.U4GwHaYqAgr3AwUsLv3MODatxuDmdWAdedJhQg'
intents = discord.Intents.all()
intents.members = True

activity = discord.Activity(type=discord.ActivityType.playing, name="VS Code")
bot = commands.Bot(command_prefix='?', activity=activity, intents=intents)
bot.announcement_channel_set = ""



@bot.command()
async def spampm(ctx, user: discord.User, numberofmessages, *message):
    for i in range(int(numberofmessages)):
        await user.send(message)


@bot.command()
async def spam(ctx, numberofmessages, message):
    for i in range(int(numberofmessages)):
        await ctx.send(message)


#For command errors
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please pass in all requirements :rolling_eyes:.')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You dont have all the requirements :angry:")
    else:
        raise error


bot.run(bot_token)
