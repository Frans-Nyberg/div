import discord
import asyncio
import MessageMaker

class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # create the background task and run it in the background
        self.bg_task = self.loop.create_task(self.my_background_task())

        # store messages
        self.sendings = list()
        self.channels = list()
        self.memory = list()

    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print('------')

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return

        await MessageMaker.updateLists(message, self.channels, self.memory)
        await MessageMaker.cue(self.sendings, self.memory)

    async def my_background_task(self):
        await self.wait_until_ready()
        print('Background Loop Started')
        while not self.is_closed():
            try:
                sendingMessage = self.sendings.pop()
                messageContent = sendingMessage.content
                print('Sending message:', messageContent)
                await sendingMessage.channel.send(messageContent)
                await asyncio.sleep(3)
            except Exception as e:
                print('Not sending:', e)
                await asyncio.sleep(10)
        print('Background Loop Ends')

client = MyClient()
client.run('NjA4MjkxNzk2NDM4NzQ1MDk4.XUnWWA.T4ILz273i3s7jiPEWCtSAELXFKQ')
