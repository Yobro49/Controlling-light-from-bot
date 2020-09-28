import os

x = "Mjolniemaxmuff" #ADAFRUIT_IO_USERNAME
y = "aio_CRNm16OPH1PdNIuR3J4J75YmVKWP" #ADAFRUIT_IO_KEY

from Adafruit_IO import Client, Feed
aio = Client(x,y)

from telegram.ext import Updater, CommandHandler 
import requests # Getting data from cloud
from Adafruit_IO import Data


def on(bot,update):
    value = Data(value=1)
    value_send = aio.create_data('light',value)

def off(bot,update):
    value = Data(value=0)
    value_send = aio.create_data('light',value)

u = Updater(os.getenv(u))
dp = u.dispatcher
dp.add_handler(CommandHandler('on',on))
dp.add_handler(CommandHandler('off',off)) 
u.start_polling()
u.idle()
 
