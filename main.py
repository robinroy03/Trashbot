import discord
import asyncio

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("Bot is online!")

@client.event
async def on_message(message):
    if message.author != client.user:
        if message.content == "!help":
            await message.channel.send(
                "Use prefix `!say ` and bot will speak that back to you"
                "\nType `Hello` and bot replies with an emoji\n"
                "Edit a message and the bot will highlight that to everyone :)"
            )
        elif message.content[:5] == "!say ":
            await message.channel.send(f"{message.content[5:]}")
        elif message.content == "Hello":
            await message.add_reaction("\U0001F60E")

@client.event
async def on_message_edit(before, after):
    await before.channel.send(f"Before : {before.content}\nAfter : {after.content}")

client.run('Your token goes here')
