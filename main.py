import discord
from discord.ext import commands

from bot_logic import gen_pass
from bot_logic import random_number
from bot_logic import gamea

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def pasword(ctx, count_pass = 5):
    await ctx.send(gen_pass(count_pass))

@bot.command()
async def number(ctx,min_num = 1 , max_num = 1000):
    await ctx.send(random_number(min_num,max_num))

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

bot.run('TOKEN')
