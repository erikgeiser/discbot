import discord
from discord.ext import commands
from bot import Discbot
from config import conf
import asyncio

if not discord.opus.is_loaded():
    try:
        discord.opus.load_opus('/usr/lib/x86_64-linux-gnu/libopus.so.0')
    except OSError:
        print("Could not load libopus. Exiting...")


bot = commands.Bot(command_prefix=commands.when_mentioned_or('!'),
                   description='Provider of face melting mixtapes')
discbot = Discbot(bot)
bot.add_cog(discbot)

@bot.event
async def on_ready():
    print("Connected")
    await discbot.start()


bot.run(conf.token)
