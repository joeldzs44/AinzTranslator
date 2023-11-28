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
async def on_reaction_add(reaction, user):
    if reaction.emoji:
        reactedEmoji = reaction.emoji
        if not(languages.get(reactedEmoji)): 
            pass
        else:
            selectedLanguage = languages.get(reactedEmoji)
            sentMessage = str(reaction.message.content)
            translator = Translator()
            sendMessage = translator.translate(sentMessage, dest=selectedLanguage)
            await reaction.message.reply(f"<@{user.id}> {reactedEmoji} Translation:\n\n"+sendMessage.text)

load_dotenv()
token = os.getenv("TOKEN")
client.run(token)