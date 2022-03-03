import discord
from discord.ext import commands
import wordle
# Import the client id of the bot
from id import client_id

bot = commands.Bot(command_prefix="+")

@bot.event
async def on_ready():
    print("The bot is launched")

def help(ctx):
    pass

def start(ctx):
    pass


@bot.command(name="w")
async def wordle(ctx, arg=''):
    if arg=="help":
        await help(ctx)
    elif arg=="start":
        await start(ctx)


if __name__ == '__main__':
    bot.run(client_id)