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
        phone_number = sys.argv[2]
        adress = sys.argv[1]
        if not os.path.exists("session"):
            os.mkdir("session")
       
        # Connect to client
        client = TelegramClient('session/' + phone_number, api_id, api_hash)
        await client.start(phone_number)
        me = await client.get_me()
        
        #Start withdraw command
        
        await client.send_message(url_channel, '/withdraw')
        
        
        @client.on(events.NewMessage(chats=url_channel, incoming=True))
        async def withdraw_balance(event):
            withdraw = event.raw_text
            if 'Your balance' in withdraw:
                cama = float(event.raw_text[15:24])
                #print(cama)
                await client.send_message(me.id, str(cama))
                
                await client.send_message(url_channel, adress)
                #print(event.raw_text)
            if 'Enter the amount' in withdraw:
                #print(me.id)
                am = await client.get_messages(me.id, limit=1)
                for message in am:
                    await client.send_message(url_channel, message.message)
            if 'Are you sure you want to send' in withdraw:
                await event.message.click(0)            
                #print_msg_time(Fore.YELLOW + f'{withdraw}\n' + Fore.RESET)
            if 'Your withdrawal has been requested!' in withdraw: 
                    action = ["0", "0", "0"]
                    ask_action = int(input ("" ))
                    answer = (action[ask_action]) 
                    if answer == '0':
                        print('good')
                        exit(1)
                
                
        await client.run_until_disconnected()
    
asyncio.get_event_loop().run_until_complete(main())