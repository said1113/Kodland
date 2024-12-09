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

@bot.command()
async def mem(ctx):
    with open('images/mem1.jpg', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)

@bot.command()
async def random_meme(ctx):
    ImageName = random.choice(os.listdir("C:\Users\Said Abbasov\Desktop\Kodland Python Pro\images"))
    with open(f"Images\{ImageName}" , "rb") as f:
        Resim = discord.file{f}
    await ctx.send(file = Resim)
bot.run("sdgfhgfxgcbhfxfdfddffdcx")