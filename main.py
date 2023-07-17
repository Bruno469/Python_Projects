#DiscordBot

import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Estou online como {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startwith('!Olá'):
        await message.channel.send('Olá ')

client.run('MTA2NDYzOTQ4ODI4MzkxODM3Ng.GALGpQ.3l1ztVOcvtL_BfrAy6H7MyalmSOWbr3v5iCgB8')

#MTA2NDYzOTQ4ODI4MzkxODM3Ng.GALGpQ.3l1ztVOcvtL_BfrAy6H7MyalmSOWbr3v5iCgB8
