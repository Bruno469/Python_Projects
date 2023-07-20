import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!Olá'):
        await message.channel.send(f'Olá! {message.author} :smiling_face_with_3_hearts:')
client.run('MTA2NDYzOTQ4ODI4MzkxODM3Ng.GALGpQ.3l1ztVOcvtL_BfrAy6H7MyalmSOWbr3v5iCgB8')

#MTA2NDYzOTQ4ODI4MzkxODM3Ng.GALGpQ.3l1ztVOcvtL_BfrAy6H7MyalmSOWbr3v5iCgB8
