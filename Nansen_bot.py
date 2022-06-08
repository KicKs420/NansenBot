import requests
import os
import json
import discord
import certifi
from webdriver_manager.chrome import ChromeDriverManager
import selenium_bot


TOKEN = ''
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

            if len(full_request) == 1:
                if command == 'help':
                    await message.reply('To request a Nansen report, specify one of the supported commands (!godmode, !breakdown, !hodlers, !trades, and !rarity) and then the contract address.')
                    return
            else:
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
                await message.reply(f'Unknown command entered. Currently supported commands are !godmode, !breakdown, !hodlers, !trades, and !rarity. Please try again.')
                return


            #await message.reply(f'Pulling ' + command + ' report for: ' + contract)
            website_title = selenium_bot.nansen_request(url, contract)

            if website_title == None or website_title == "NFT God Mode":
                await message.reply(f'No contract found for ' + contract + '. Please try again.')
                return
            else:
                embed = discord.Embed(title=website_title, description="Report requested: " + command, color=0x00ff00)  # creates embed
                file = discord.File(contract + ".png", filename=contract + ".png")
                embed.set_image(url="attachment://image.png")
                await message.reply(file=file, embed=embed)
                return

    guilds = await client.fetch_guilds(limit=150).flatten()

client.run(TOKEN)