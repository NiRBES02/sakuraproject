import discord
from discord.ext import commands
import os, sqlite3

bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"), case_insensitive=True, intents=discord.Intents.all())
bot.remove_command('help')
base = sqlite3.connect('cogs/sakura.db')
cur = base.cursor()

@bot.event
async def on_ready():
    cur.execute("""CREATE TABLE IF NOT EXISTS users (id INT,name TEXT,nick TEXT,lvl INT,exp INT,server_id INT)""")
    for guild in bot.guilds:
        for member in guild.members:
            if cur.execute(f"SELECT id FROM users WHERE id = {member.id}").fetchone() is None:
                cur.execute(f"INSERT INTO users VALUES ('{member.id}', '{member.name}', '{member.nick}', 0, 0, {guild.id})")
    base.commit()


for file in os.listdir("./cogs"): # lists all the cog files inside the cog folder.
    if file.endswith(".py"): # It gets all the cogs that ends with a ".py".
        name = file[:-3] # It gets the name of the file removing the ".py"
        bot.load_extension(f"cogs.{name}") # This loads the cog.

@bot.command()
@commands.is_owner()
async def reload(ctx, *, name: str):
    try:
        bot.reload_extension(f"cogs.{name}")
    except Exception as e:
        return await ctx.send(e)
    await ctx.send(f'The module "**{name}**" has been reloaded!')

@bot.command()
@commands.is_owner()
async def unload(ctx, *, name: str):
    try:
        bot.unload_extension(f"cogs.{name}")
    except Exception as e:
        return await ctx.send(e)
    await ctx.send(f'The module "**{name}**" has been unloaded!')

@bot.command()
@commands.is_owner()
async def l(ctx, *, name: str):
    try:
        bot.load_extension(f"cogs.{name}")
    except Exception as e:
        return await ctx.send(e)
    await ctx.send(f'The module "**{name}**" has been loaded!')

bot.run(os.getenv('TOKEN'))