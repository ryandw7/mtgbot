import discord
import sys

from scry_call import scry_call
from scan_message import scan_message



if len(sys.argv) < 2:  # Check if at least one argument is provided
    print("Command missing application secret")
    sys.exit(1)  # Exit the program with an error status
else:
    SECRET = sys.argv[1]
    print(f"Using SECRET: {SECRET}")

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        if message.author == 'merlin1011.':
             await message.channel.send('Brendan, nobody asked you anything')

        search = scan_message(message.content)

        if search:
            res = scry_call(search)
            
            if res and len(res) > 0:
                    for i in res:
                        await message.channel.send(i)
            else:
                await message.channel.send("Sorry, I couldn't find an image for that card.")


intents = discord.Intents.default()
intents.message_content = True


client = MyClient(intents=intents)
client.run(SECRET)
