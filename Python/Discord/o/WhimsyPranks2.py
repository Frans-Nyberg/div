import discord
import asyncio
import MessageMaker

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
        print('------')

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return

        self.messages.append(message)
        print('Appended message: ', message.content)

    async def my_background_task(self):
        await self.wait_until_ready()
        print('Background Loop Started')
        while not self.is_closed():
            try:
                sendingMessage = MessageMaker.getMessage(self.messages)
                messageContent = sendingMessage.content
                print('Sending message:', messageContent, 'in channel', sendingMessage.channel)
                await sendingMessage.channel.send(messageContent)
                await asyncio.sleep(60)
            except Exception as e:
                print('Exception in background task:', e)
                await asyncio.sleep(300)
        print('Background Loop Ends')

client = MyClient()
client.run('NjA4MjkxNzk2NDM4NzQ1MDk4.XUnWWA.T4ILz273i3s7jiPEWCtSAELXFKQ')
