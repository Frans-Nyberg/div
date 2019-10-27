import discord
import asyncio
from MessageMaker import getMessage

class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # create the background task and run it in the background
        self.bg_task = self.loop.create_task(self.my_background_task())

        # store messages
        self.messages = list()

    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
#        print(self.user.id)
        print('------')

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return

        self.messages.append(message)

    async def my_background_task(self):
        await self.wait_until_ready()
        try:
            sendingMessage = getMessage(self.messages)
            await message.channel.send(sendingMessage.content)
        except Exception as e:
            print(Exception)

client = MyClient()
client.run('NjA4MjkxNzk2NDM4NzQ1MDk4.XUnWWA.T4ILz273i3s7jiPEWCtSAELXFKQ')
