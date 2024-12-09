import discord
from discord.ext import commands
import os
import random

intents = discord.intents.default()
intents.message_content  = True

bot = commands.Bot(command_prefix = "$", intents = intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yapıldı')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba ben {bot.user}, bir sohbet discord botuyum')

@bot.command
async def merhaba(ctx):
    await ctx.send("Merhaba ben bir Çerve dotu asistanınızım... Atık yönütimi hakkında bilgi almaya ne dersiniz??")

@bot.command
async def geri_donusum(ctx):
    tips = [
        "Plastik şişeleri yıkamadan geri dönüşüm kutusuna atmayınız?"
        "Atıkları geri dönüşüm kısımalarına dikkat ederek atalım"
        "Cam şişeleri kırmadan geri dönüşüm kutusuna atınız."
    ]
    await ctx.send("İşte bazı geri dönüşüm tavsiyeleri")


bot.run("removed for security purposes")