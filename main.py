from handlers import start, lang_uz, main_menu, comment_user, read_comment
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, ConversationHandler
from telegram import update
from config import TOKEN

COMMENT = 1

def main()->None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher
    

    dispatcher.add_handler(CommandHandler(['start', 'boshlash'], start))
    dispatcher.add_handler(MessageHandler(Filters.text("🇺🇿 O'zbekcha"),lang_uz ))
    dispatcher.add_handler(MessageHandler(Filters.contact, main_menu ))

    
    conv_handler = ConversationHandler(
        entry_points=[MessageHandler(Filters.text("✍️ Fikr qoldirish"), comment_user)],
        states={
            COMMENT: [MessageHandler(Filters.text & ~Filters.command, read_comment)]
        },
        fallbacks=[])
    dispatcher.add_handler(conv_handler)



    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main() 
