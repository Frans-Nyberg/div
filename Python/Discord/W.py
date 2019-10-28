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
        self.maxSends = 2

        # only read and post from the following channels
        self.allowedChannels = [
#        , #BotChannel
        , #WhimData
        , #Channeler
        ]

    async def on_ready(self):
        print('------')
        await MessageMaker.loadMemory(self.get_channel(), self.channels, self.memory)

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return

        if message.channel.id not in self.allowedChannels:
            return

        if "stop!" in message.content:
            await message.channel.send("bye!")
            await self.logout()
            
        await MessageMaker.updateLists(message, self.channels, self.memory)

        if len(self.sendings) < self.maxSends:
            await MessageMaker.cue(self.sendings, self.waits, self.memory)

    async def my_background_task(self):
        await self.wait_until_ready()
        while not self.is_closed():
            if not self.sendings:
                try:
                    sendingMessage = MessageMaker.getMessage(self.memory)
                    messageContent = sendingMessage.content

                    channeler = self.get_channel()
                    await channeler.send(messageContent)

                    time = MessageMaker.waitTime(5)
                    await asyncio.sleep(time)
                except Exception as e:
                    print(e)
                    await asyncio.sleep(10)
            else:
                try:
                    sendingMessage = self.sendings.pop()
                    messageContent = sendingMessage.content

                    channeler = self.get_channel()
                    await channeler.send(messageContent)

                    time = self.waits.pop()
                    await asyncio.sleep(time)
                except Exception as e:
                    print(e)
                    await asyncio.sleep(10)

client = MyClient()
client.run('')
