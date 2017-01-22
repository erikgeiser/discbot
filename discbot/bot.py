from config import conf
import discord
from discord.ext import commands

class CommandBot(object):
    def __init__(self, bot):
        print("in init")
        self.bot = bot
        self.voice = self.bot.join_voice_channel(conf.channel)
        print(self.voice)
        print("end of init")

    @commands.command(pass_context=True)
    async def join(self, ctx):
        if self.voice == None:
            self.voice = await self.bot.join_voice_channel(ctx.channel)
