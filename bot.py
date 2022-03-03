import discord
import wordle
# Import the client id of the bot
from id import client_id

client = discord.Client()

if __name__ == '__main__':
    client.run(client_id)