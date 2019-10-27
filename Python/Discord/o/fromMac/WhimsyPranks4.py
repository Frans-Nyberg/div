import discord
import asyncio
import MessageMaker
import random

class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # create the background task and run it in the background
        self.bg_task = self.loop.create_task(self.my_background_task())

        # store messages
        self.sendings = list()
        self.channels = list()
        self.memory = list()
        self.waits = list()
        self.maxSends = 1
        self.recents = list()

        # only read and post from the following channels
        self.allowedChannels = [
        608289492671004673, #TestChannel
        ]

    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print('------')

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return

        if message.channel.id not in self.allowedChannels:
            return

        if "stop" in message.content:
            await message.channel.send("bye!")
            await self.logout()

        await MessageMaker.updateLists(message, self.channels, self.memory, self.recents)

        if len(self.recents) <= self.maxSends:
            await MessageMaker.cue(self.sendings, self.waits, self.memory, self.recents)

    async def my_background_task(self):
        await self.wait_until_ready()
        print('Background Loop Started')
        while not self.is_closed():
            if not self.sendings:
                print("Nothing to send")
                await asyncio.sleep(60)
            else:
                sendingMessage = self.sendings.pop()
                self.recents.pop()
                messageContent = sendingMessage.content
                print('Sending message:', messageContent)

#                await channel0.send(messageContent)
#                await channel1.send(messageContent)
                # async is not called until an already running coroutine finishes

                await sendingMessage.channel.send(messageContent)

                time = self.waits.pop()
                await asyncio.sleep(time)
        print('Background Loop Ends')

client = MyClient()
client.run('NjA4MjkxNzk2NDM4NzQ1MDk4.XUnWWA.T4ILz273i3s7jiPEWCtSAELXFKQ')
