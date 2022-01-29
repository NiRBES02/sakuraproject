import discord
from discord.ext import commands, tasks
from discord.utils import get
from datetime import datetime
import os, sqlite3
from config import settings

bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"), case_insensitive=True, intents=discord.Intents.all())

class events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()                                                             
    async def on_ready(self):
            print('* * * * * * * * * * * * * * * * *')                                                             
            print('* [SAKURA] Sakura started.	*')
            print('* [SAKURA] Module load.		*')
            print('* [SAKURA] Base connect.	*')
            print('* * * * * * * * * * * * * * * * *')
            print(f"* [Info] Author bots: {settings['Author']} 	*")
            print(f"* [Info] Version bots: {settings['Version']}	*")
            print(f"* [Info] Prefix bots: {settings['Prefix']} 	*")
            print('* * * * * * * * * * * * * * * * *')
            await self.bot.change_presence(activity=discord.Game(name=f"Version {settings['Version']}"))

def setup(bot):
    bot.add_cog(events(bot))