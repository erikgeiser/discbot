import discord
from discord.ext import commands
from bot import CommandBot
from config import conf
import asyncio

if not discord.opus.is_loaded():
    try:
        discord.opus.load_opus('/usr/lib/x86_64-linux-gnu/libopus.so.0')
    except OSError:
        print("Could not load libopus. Exiting...")


bot = commands.Bot(command_prefix=commands.when_mentioned_or('!'),
                   description='Provider of face melting mixtapes')
bot.add_cog(CommandBot(bot))

@bot.event
async def on_ready():
    print('Logged in')

bot.run(conf.token)
