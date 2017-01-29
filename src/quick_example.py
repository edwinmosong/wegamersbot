"""
From https://github.com/Rapptz/discord.py
Created 10/29/2016
"""
import logging

import discord
import asyncio


logger = logging.getLogger('wegamersbot')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

client = discord.Client()

@client.event
@asyncio.coroutine
def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
@asyncio.coroutine
def on_message(message):
    if message.content.startswith('!test'):
        # counter = 0
        # tmp = yield from client.send_message(message.channel, 'Calculating messages...')
        logs = yield from client.logs_from(message.channel)
        for past_messages in logs:
            logger.debug({"client.user": client.user, "message.author": message.author})
            if message.author == client.user:
                yield from client.edit_message(message, ':)')
            else:
                yield from client.send_message(message.channel, 'testing back :)')
        # for log in client.logs_from(message.channel, limit=100):
        #     if log.author == message.author:
        #         counter += 1
        # yield from client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('!sleep'):
        yield from asyncio.sleep(5)
        yield from client.send_message(message.channel, 'Done sleeping')

client.run('MjQyMDUwNTE1MTQyMzExOTM3.Cvay0A.OhZwoFXG3c_mUq9EezZDwotsxZ8')
