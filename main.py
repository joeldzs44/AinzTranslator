import discord
import os
from googletrans import Translator
from dotenv.main import load_dotenv
from languages import languages

# Intents
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# Connecting to Client
@client.event
async def on_ready():
    print(f"We logged in as {client.user}")

@client.event
async def on_raw_reaction_add(reaction):
    channel = await client.fetch_channel(reaction.channel_id)
    message = await channel.fetch_message(reaction.message_id)
    userid = reaction.user_id

    if reaction.emoji:
        reactedEmoji = reaction.emoji.name
        if not(languages.get(reactedEmoji)):
            print(f"{reactedEmoji} Language not found")
            pass
        else:
            selectedLanguage = languages.get(reactedEmoji)
            sentMessage = str(message.content)
            translator = Translator()
            sendMessage = translator.translate(sentMessage, dest=selectedLanguage)
            await channel.send(f"<@{userid}> {reactedEmoji} Translation:\n\n"+sendMessage.text)

load_dotenv()
token = os.getenv("TOKEN")
client.run(token)