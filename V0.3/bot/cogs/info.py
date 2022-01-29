import discord
from discord.ext import commands, tasks
from discord.utils import get
from datetime import datetime
import os, sqlite3
from config import settings

bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"), case_insensitive=True, intents=discord.Intents.all())

class info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def help(self, ctx, point = None):
    	if point == None:
    		embed=discord.Embed(title="Bot Commands", color=0x96fa00)
    		embed.add_field(name=f"{settings['Prefix']}help mod", value="Help by commands mod", inline=False)
    		embed.add_field(name=f"{settings['Prefix']}help own", value="Help by commands mod", inline=False)
    		embed.add_field(name=f"{settings['Prefix']}help bot", value="Help by commands mod", inline=False)
    		await ctx.send(embed=embed)
    	elif point == "mod":
    		embed=discord.Embed(title="Bot Commands - mod -", color=0x96fa00)
    		embed.add_field(name=f"{settings['Prefix']}purge [amount]", value="Clear the chat from the message.", inline=False)
    		embed.add_field(name=f"{settings['Prefix']}say [text]", value="Write a message on behalf of the bot.", inline=False)
    		await ctx.send(embed=embed)
    	elif point == "own":
    		embed=discord.Embed(title="Bot Commands - own -", color=0x96fa00)
    		embed.add_field(name=f"{settings['Prefix']}reload [module]", value="Reload modules.", inline=False)
    		embed.add_field(name=f"{settings['Prefix']}load [module]", value="Load modules.", inline=False)
    		embed.add_field(name=f"{settings['Prefix']}unload [module]", value="Unload modules.", inline=False)
    		await ctx.send(embed=embed)
    	elif point == "bot":
    		embed=discord.Embed(title="Bot info", color=0x96fa00)
    		embed.set_author(name="GitHub - Project Sakura", url="https://github.com/NiRBES02/sakuraproject",
    			icon_url="https://gitlab.com/uploads/-/system/group/avatar/10532272/github.png")
    		embed.add_field(name="Author:", value=f"{settings['Author']}", inline=False)
    		embed.add_field(name="Version", value=f"{settings['Version']}", inline=False)
    		embed.add_field(name="Prefix", value=f"{settings['Prefix']}", inline=False)
    		embed.set_footer(text="GitHub - https://github.com/NiRBES02/sakuraproject")
    		await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(info(bot))