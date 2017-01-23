from config import conf
import asyncio
import discord
from playlist import get_all_playlists
from functools import wraps
from discord.ext import commands

class Discbot(object):
    def __init__(self, bot):
        self.bot = bot
        self.voice = None
        self.player = None
        self.playlists = get_all_playlists()
        self.playlist = self.playlists[conf.default_playlist]

    async def start(self):
        channel = self.bot.get_channel(conf.initial_channel)
        self.voice = await self.bot.join_voice_channel(channel)
        self.player = self.voice.create_ffmpeg_player(self.playlist.next(),
            after=self.after_playback)
        self.player.start()

    def run_coroutine(self, func):
        future = asyncio.run_coroutine_threadsafe(func, self.bot.loop)
        try:
            future.result()
        except Exception as e:
            print(e)

    def after_playback(self):
        self.run_coroutine(self.voice.disconnect())

    @commands.command(pass_context=True, no_pm=True)
    async def join(self, ctx):
        if self.voice == None:
            channel = ctx.message.author.voice_channel
            self.voice = await self.bot.join_voice_channel(channel)
