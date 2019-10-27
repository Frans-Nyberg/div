import random

# Updates messages and channels lists
async def updateLists(message, channels, memory, recents):
    memory.append(message)
    recents.append(message)
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
async def cue(sendings, waits, memory, recents):
    message = getMessage(memory)
    sendings.append(message)
    time = waitTime()
    waits.append(time)
    print('Cue new message: ', message.content, '\nwith wait time', time)
    print('Lenght of recents: ', len(recents))

# Wait time for the next message to be sent
def waitTime():
    time = random.randrange(60,120)
    sometimes = random.randrange(0, 5)
    if sometimes == 0:
        time = 300
    return time
