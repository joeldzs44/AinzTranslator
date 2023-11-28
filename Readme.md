# AinzTranslator

Hi there!
This is a simple discord bot which translates messages to a desired language using the **googletrans** library.

The bot needs following permissions in the discord server:
- View Channel
- Send Messages
- Send Messages In Threads (Optional)
- Read Message History

## Prerequisites
You need to create a bot on discord.com/developers and get your bot access token.


## Usage instructions
The bot relies on user reactions to determine destination language.
Eg. If user reacts with a 🇫🇷 flag emoji on a message, the bot will reply back with the french translation. Follow these instructions to setup the bot:

1. Clone the git repository using following command
>`git clone https://github.com/joeldzs44/AinzTranslator.git`
2. Install all required modules using pip
> `pip install -r requirements.txt`
3. Create a **.env** file with your bot token in the same directory as rest of the files.
> `TOKEN=<YOUR TOKEN>`
4. Run the main.py file and you should see a message saying "We logged in as < Bot Name >"
> `python main.py`

Congratulations ! Your bot is now up and running. Now add it to a server and react on a message with a flag to test it. You should get a reply with the translated message.

## How to add more languages ?
To add a missing language you can modify the `languages.py` to include additional languages. The key would be discord emoji and value would be one of the language codes supported by the googletrans library.

#### References
Discord emoji codes:
> https://emojicopy.com/

List of googeltrans supported languages:
> https://py-googletrans.readthedocs.io/en/latest/#googletrans-languages
