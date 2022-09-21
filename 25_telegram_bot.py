from asyncore import dispatcher
from lib2to3.pgen2 import token
#import the dependecies
from telegram.ext import Updater, CommandHandler
updater = Updater(token="5792255580:AAFrjJjuJaW5NAK4KmzfNYnOuLcyw6PTu8I",use_context=True)
daspatcher = updater.dispatcher
def Hello_User(update, context):
    try:
        context.bot.send_message(chat_id = update.effective_chat.id, text = "Hello Welcome to ML Family & DSA")
    except Exception as Ex:
        return Ex
hell_handler = CommandHandler('Hi',Hello_User) #if I send /Hi messgage to my chatbot so the Chat will return Hello Welcome to ML Family & DSA
daspatcher.add_handler(hell_handler)

#covid dayly status send 
import requests, json
def summary_covid(up,con):
    try:
        response = requests.get('https://api.covid19api.com/summary')
        if(response.status_code==200): #Everything went okay, we have the data
            data = response.json()
            print(data['Global'])
            con.bot.send_message(chat_id = up.effective_chat.id, text = data['Global'])
        else:
            con.bot.send_message(chat_id = up.effective_chat.id, text = "Something Went Wrong! Plaese Tray Again Later")
    except Exception as Ex:
        return Ex
hell_handler_2 = CommandHandler("Covid",summary_covid)
daspatcher.add_handler(hell_handler)
daspatcher.add_handler(hell_handler_2)
updater.start_polling()