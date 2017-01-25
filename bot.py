from telegram.ext import Updater, CommandHandler
import random
def start(bot, update):
    update.message.reply_text('Hello World!')

def hello(bot, update):
    update.message.reply_text('Hello {}'.format(update.message.from_user.first_name))
def hi(bot,update):
    update.message.reply_text('hi {} what can i do for you'.format(update.message.from_user.first_name))
def shut_up(bot,update):
    update.message.reply_text("Okay no need to be rude :(")  
def quote(bot,update):
    y=random.randrange(0,10)
    if y <= 3:
       update.message.reply_text("Peace is its own reward-Mahatma Gandhi")       
    elif y <= 4:
       update.message.reply_text("Art is a collaboration between God and the artist, and the less the artist does the better-Andre Gide")       
    elif y<=5:        
        update.message.reply_text("Every man has a sane spot somewhere. Robert Louis Stevenson") 
updater = Updater('272518965:AAFAkV1kTJ17fCWbc2iDbqsshb95b2ShGtI')

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('hi', hi))
updater.dispatcher.add_handler(CommandHandler('shut_up',shut_up))
updater.dispatcher.add_handler(CommandHandler('quote',quote))
updater.start_polling()
updater.idle()

