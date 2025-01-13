import discord
import sys

from scry_call import scry_call
from scan_message import scan_message

SECRET = sys.argv[1]

print(scry_call(scan_message('my nafe g erg {dark ritual} fewEF wef fefw {damnation}')))


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        if message.author == 'merlin1011.':
             await message.channel.send('Brendan, nobody asked for your opinion')
        search = scan_message(message.content)
        if search:
            res = await scry_call(search)
            if res and res.length > 0:
                    for i in res:
                        await message.channel.send(i)
            else:
                await message.channel.send("Sorry, I couldn't find an image for that card.")


intents = discord.Intents.default()
intents.message_content = True


client = MyClient(intents=intents)
client.run(SECRET)
