from telegram.ext import Updater, CommandHandler
import os, sys
import urllib.request, json

with urllib.request.urlopen("https://xkcd.com/info.0.json") as url:
    data = json.loads(url.read().decode())
    print(data['img'])
    image = urllib.request.urlretrieve(data['img'], "xkcd.png")

TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')
if not TELEGRAM_TOKEN:
    sys.exit('Please set environment variable TELEGRAM_TOKEN')

def xkcd(bot, update):
    update.message.reply_image(        
        image,
        quote=False
    )

def hello(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))


updater = Updater(TELEGRAM_TOKEN)

updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('xkcd', xkcd))

updater.start_polling()
updater.idle()
