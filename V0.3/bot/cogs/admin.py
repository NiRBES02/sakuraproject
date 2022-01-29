import discord
from discord.ext import commands, tasks
from discord.utils import get
from datetime import datetime
import os, sqlite3
from config import settings

bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"), case_insensitive=True, intents=discord.Intents.all())

class admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def say(self, ctx,*,message=None):
    	if message == None:
    		await ctx.send(f"Enter a message!")
    	else:
        	await ctx.send(message)
        	await ctx.message.delete()

    @commands.command()
    @commands.is_owner()
    async def purge(self, ctx, amount=None):
    	if amount == None:
    		await ctx.channel.send("Enter the number of deleted messages!")
    	else:
        	await ctx.channel.purge(limit=int(amount)+1)

def setup(bot):
    bot.add_cog(admin(bot))