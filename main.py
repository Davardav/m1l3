import discord
from bot_logic import gen_pass
from bot_logic import random_number
from bot_logic import gamea
# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send('\\U0001f642')
    elif message.content.startswith('$pasword'):
        await message.channel.send(gen_pass(10))
    elif message.content.startswith('$number'):
        await message.channel.send(random_number(1,1000))
    elif message.content.startswith('$stone') or message.content.startswith('$scissors') or message.content.startswith('$paper'):
        await message.channel.send(gamea(message.content))
    else:
        await message.channel.send(message.content)

client.run('token')
