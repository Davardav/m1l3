import discord
import random
from discord.ext import commands
from bot_logic import gen_pass
from bot_logic import random_number
from bot_logic import gamea
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command()
async def roll(ctx, dice: str):
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return
    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)


@bot.command(description ='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    await ctx.send(random.choice(choices))


@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def joined(ctx, member: discord.Member):
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def pasword(ctx, count_pass = 5):
    await ctx.send(gen_pass(count_pass))

@bot.command()
async def number(ctx,min_num = 1 , max_num = 1000):
    await ctx.send(random_number(min_num,max_num))

@bot.command()
async def upp(ctx,choices: str):
    await ctx.send(choices.upper())

@bot.command()
async def info(ctx):
    await ctx.send(f'roll - отправляет цифры в NDN,choose - отправляет рандомное слово из ваших варинтов,repeat - отправляет собщение несколько раз,pasword - генерирует несколько случайных символов,number - рандомное число,upp - пишет слово капсом')
    await ctx.send(f'любая команда начинается с $,между командой и значением пишится пробел')
    await ctx.send(f'примеры: $roll 2d6,$choose aaa bbb ccc,$repeat 5 snow,$pasword 10,$number 1 100,upp snow')


bot.run("TOKEN")
