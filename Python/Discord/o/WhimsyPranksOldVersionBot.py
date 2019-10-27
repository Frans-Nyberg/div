import random
from discord.ext.commands import Bot

BOT_PREFIX = ("?", "!")
TOKEN = "NjA4MjkxNzk2NDM4NzQ1MDk4.XUmERQ.5IMd43F7opi7QjVHnW05Q6VnPVI"

client = Bot(command_prefix=BOT_PREFIX)

@client.command(name='8ball',
                description='123 writer',
                brief='123')
async def eight_ball():
    possible_responses = [
    '1',
    '2',
    '3',
    ]
    await client.say(random.coice(possible_responses))

client.run(TOKEN)
