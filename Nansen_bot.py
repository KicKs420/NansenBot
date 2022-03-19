import requests
import os
import json
import discord
import certifi
from webdriver_manager.chrome import ChromeDriverManager
import selenium_bot


TOKEN = 'OTUxMTM2MjcyOTY4MjE2NjA2.YijErg.09ttinRDFf1IkMGiWKTJfg9cqYM'
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    message_user = str(message.author).split('#')[0]
    message_fulluser = message.author
    message_str = str(message.content)
    channel_name = str(message.channel.name)
    godmode_baseurl = 'https://pro.nansen.ai/nft-god-mode'

    if message.author == client.user:
        return
    else:
        print(f'{message_user}: {message_str} ({channel_name})')

    if channel_name == 'nansen-requests':
        message_str = message_str.lower()

        if message_str[:1] == '!':
            full_request = str.split(message_str, " ")
            command = full_request[0][1:].lower()
            contract = full_request[1].lower()

            if command == 'godmode':
                url = godmode_baseurl + '?nft_address=' + contract

            elif command == 'breakdown':
                url = godmode_baseurl + '/breakdown?nft_address=' + contract

            elif command == 'hodlers':
                url = godmode_baseurl + '/segments?nft_address=' + contract

            elif command == 'trades':
                url = godmode_baseurl + '/transactions?nft_address=' + contract

            elif command == 'rarity':
                url = godmode_baseurl + '/rarity?nft_address=' + contract

            else:
                await message.channel.send(f'{message_user}, unknown command entered. Currently supported commands are !godmode, !breakdown, !hodlers, !trades, and !rarity. Please try again.')
                return

            await message.channel.send(f'{message_user}, pulling ' + command + ' for: ' + url)
            selenium_bot.nansen_request(url)
            return

    guilds = await client.fetch_guilds(limit=150).flatten()


client.run(TOKEN)