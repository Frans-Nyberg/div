import random

# Updates messages and channels lists
async def updateLists(message, channels, memory):
    memory.append(message)
    print('Appended message: ', message.content)

    if message.channel not in channels:
        channels.append(message.channel)
        print('Appended channel: ', message.channel)
        await appendHistory(message.channel, memory)
        print('Appended channel history in :', message.channel)

# Pops a message
def getMessage(messageList):
    size = len(messageList)
    index = random.randrange(0,size)

    returnMessage = messageList.pop(index)
    return returnMessage

# Append channel history
async def appendHistory(channel, memory):
    record = channel.history(limit=5000)
    async for message in record:
        memory.append(message)

# Cue messages to be sent
async def cue(sendings, memory):
    sendings.append(getMessage(memory))
    print('Cue new message')
