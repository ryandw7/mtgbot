import discord
import sys
import requests

SECRET = sys.argv[1]

def scan_message(message):

    if '{' and '}' in message:
        a = message.find('{')
        b = message.find('}')
        search = message[a+1:b]
        return search

def scry_call(query_string):
    response = requests.get(f"https://api.scryfall.com/cards/search?q={query_string}")
    if response.status_code == 200:
        return response.json()
    return None

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        search = scan_message(message.content)
        if search:
            res = scry_call(search)
            if res and 'data' in res and len(res['data']) > 0:
                card_data = res['data'][0]  # Get the first card in the results
                if 'image_uris' in card_data and 'normal' in card_data['image_uris']:
                    img = card_data['image_uris']['normal']
                    await message.channel.send(img)
                else:
                    await message.channel.send("Sorry, I couldn't find an image for that card.")
            else:
                await message.channel.send("Sorry, I couldn't find that card.")

intents = discord.Intents.default()
intents.message_content = True


client = MyClient(intents=intents)
client.run(SECRET)
