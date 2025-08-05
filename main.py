from handlers import start, lang_uz, main_menu
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler 
from telegram import update
from config import TOKEN

def main()->None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler(['start', 'boshlash'], start))
    dispatcher.add_handler(MessageHandler(Filters.text("🇺🇿 O'zbekcha"),lang_uz ))
    dispatcher.add_handler(MessageHandler(Filters.contact, main_menu ))


    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main() 
