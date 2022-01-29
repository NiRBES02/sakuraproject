import asyncio
from logging import fatal
import discord
from discord.ext import commands
import os, sqlite3
import random 
from discord.utils import get
from discord import utils
from datetime import datetime, date, time
import json

###################################
# Предназначение: Исполняющий файл.
###################################

for file in os.listdir("./cogs"): # lists all the cog files inside the cog folder.
    if file.endswith(".py"): # It gets all the cogs that ends with a ".py".
        name = file[:-3] # It gets the name of the file removing the ".py"
        bot.load_extension(f"cogs.{name}") # This loads the cog.
@bot.command()
@commands.is_owner()
async def r(ctx, *, name: str):
    try:
        bot.reload_extension(f"cogs.{name}")
    except Exception as e:
        return await ctx.send(e)
    await ctx.send(f'Модуль "**{name}**" перезагружен!')

@bot.command()
@commands.is_owner()
async def u(ctx, *, name: str):
    try:
        bot.unload_extension(f"cogs.{name}")
    except Exception as e:
        return await ctx.send(e)
    await ctx.send(f'Модуль "**{name}**" выгружен!')

@bot.command()
@commands.is_owner()
async def l(ctx, *, name: str):
    try:
        bot.load_extension(f"cogs.{name}")
    except Exception as e:
        return await ctx.send(e)
    await ctx.send(f'Модуль "**{name}**" загружен!')
    
bot.run(os.getenv('TOKEN'))
