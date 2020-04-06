from telethon import TelegramClient,events, client
from telethon.errors import FloodWaitError, ChannelsTooMuchError, UsernameNotOccupiedError, ChannelPrivateError, ChatWriteForbiddenError, StartParamInvalidError
from telethon.tl.types import UpdateShortMessage,ReplyInlineMarkup,KeyboardButtonUrl
from telethon.tl.functions.messages import GetBotCallbackAnswerRequest, StartBotRequest
from telethon.tl.functions.account import DeleteAccountRequest
from telethon.tl.functions.channels import UpdateUsernameRequest as chusername
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors.rpcerrorlist import UsernameNotOccupiedError,UsernameOccupiedError
from colorama import Fore,init as COLO
from telethon.tl.types import PeerUser, PeerChat, PeerChannel, InputPeerChannel
import re
from telethon.tl.functions.contacts import ResolveUsernameRequest
from telethon.tl.functions.channels import LeaveChannelRequest
import logging
logging.basicConfig(level=logging.WARNING)
COLO(autoreset=True)
from datetime import datetime
from bs4 import BeautifulSoup
import os
import re
import time
import requests
import sys
import asyncio
import datetime
import pytz



ID=64179
PHPSESSID="dd60bb74bb03d8aa368aa37ec7b35d42"

try:
    def SESSION(phone_number=None):
        return TelegramClient("session/"+phone_number,ID,PHPSESSID)
    async def UravxBuCwNMpYWTzKhPF():
        if not os.path.exists("session"):
            os.mkdir("session")
  
        PROFILER=SESSION(sys.argv[1])
        try:
            await PROFILER.start(sys.argv[1])
        except FloodWaitError as b:
            print('you need to wait %s secconds'%(b.seconds))
             
        exit(1)
        me=await PROFILER.get_me()
        await PROFILER.run_until_disconnected()
    asyncio.get_event_loop().run_until_complete(UravxBuCwNMpYWTzKhPF())
except KeyboardInterrupt:
 os.system('cls' if os.name=='nt' else 'clear')