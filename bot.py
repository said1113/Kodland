import discord
from bot_logic_1 import nickname_maker
from bot_logic_1 import gen_pass
from bot_logic_1 import help
# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)
@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$merhaba'):
        await message.channel.send("Selam!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('$password'):
        await message.channel.send(gen_pass)
    elif message.content.startswith('$nickname'):
        await message.channel.send(nickname_maker)
    elif message.content.startswith('$help'):
        await message.channel.send(help)
    else:
        await message.channel.send("Böyle bir komut bulunmamakta. Eğer botu kullanmakta zorlanıyorsanız" ,"help"," komutunu kullanarak botun tüm komutlarını öğrene bilirsiniz!")



client.run("REMOVED FOR SECURITY PURPOSES")
