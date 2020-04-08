import asyncio
import logging
import re
import time
import os
import sys
import requests

logging.basicConfig(level=logging.ERROR)

from telethon.tl.types import UpdateShortMessage,ReplyInlineMarkup,KeyboardButtonUrl
from telethon import TelegramClient, events
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import GetBotCallbackAnswerRequest
from telethon.tl.functions.messages import StartBotRequest
from datetime import datetime
from colorama import Fore, init as color_ama
from bs4 import BeautifulSoup

color_ama(autoreset=True)

#os.system('cls' if os.name=='nt' else 'clear')

# Get your own values from my.telegram.org
api_id = 800812
api_hash = 'db55ad67a98df35667ca788b97f771f5'

url_channel = 'BCH_clickbot'

def print_msg_time(message):
    print('[' + Fore.CYAN + f'{datetime.now().strftime("%H:%M:%S")}' + Fore.RESET + f'] {message}')
        
async def main():
        phone_number = sys.argv[1]
        
        if not os.path.exists("session"):
            os.mkdir("session")
       
        # Connect to client
        client = TelegramClient('session/' + phone_number, api_id, api_hash)
        await client.start(phone_number)
        me = await client.get_me()
        await client(StartBotRequest(bot='BitcoinClick_bot',peer='BitcoinClick_bot',start_param='7ya3 '))
        await client(StartBotRequest(bot='Dogecoin_click_bot',peer='Dogecoin_click_bot',start_param='ty4f'))
        await client(StartBotRequest(bot='Litecoin_click_bot',peer='Litecoin_click_bot',start_param='FmvT'))
        await client(StartBotRequest(bot='BCH_clickbot',peer='BCH_clickbot',start_param='6pE3'))
        await client(StartBotRequest(bot='Zcash_click_bot',peer='Zcash_click_bot',start_param='60h0'))
        
        
        #Start balance command
        
        await client.send_message(url_channel, '/balance')
        
        
        @client.on(events.NewMessage(chats=url_channel, incoming=True))
        async def account_balance(event):
            message = event.raw_text
            #print(message)
            if 'Available balance' in message:
                cama = float(event.raw_text[19:29])
                balance = cama                
                action = ["0", "0", "0"]
                ask_action = int(input ("" ))
                answer = (action[ask_action]) 
                if answer == '0':
                    if cama>0.00001:
                        print(1 ,event.raw_text[19:29])
                    else:
                        print(0 ,event.raw_text[19:29])
                exit(1)
        await client.run_until_disconnected()
    
asyncio.get_event_loop().run_until_complete(main())