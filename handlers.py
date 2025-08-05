from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import CallbackContext, ConversationHandler
import json
import os

Admin_id = "6672753724"
COMMENT = 1

# Fayl yo‘li
FILE_PATH = "users/users.json"

def load_users():
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def save_users(users):
    with open(FILE_PATH, "w") as file:
        json.dump(users, file, indent=4)

def start(update: Update, context: CallbackContext):
    bot = context.bot
    user = update.effective_user
    users = load_users()

    update.message.reply_text(f"Assalomu alaykum {user.full_name}")

    user_dict = {
        "id": user.id,
        "name": user.full_name
    }

    if not any(u["id"] == user_dict["id"] for u in users):
        users.append(user_dict)
        save_users(users) 


    bot.send_message(
        chat_id=user.id,
        text="Menyuni tanlang:",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("🇺🇿 O'zbekcha"), KeyboardButton("🇷🇺 Ruscha")],
                [KeyboardButton("🇺🇸 English")]
            ],
            resize_keyboard=True,
            one_time_keyboard=True
        )
    )


def lang_uz(update:Update, context : CallbackContext):
    text = update.message.text
    if text == "🇺🇿 O'zbekcha":
        update.message.reply_text(
            "Iltimos telefon raqamingizni kiriting: ",
            reply_markup=ReplyKeyboardMarkup(
                keyboard=[
                    [KeyboardButton("telefon raqamni ulashish", request_contact=True)]
                ],
            
                resize_keyboard=True,
                one_time_keyboard=True
                


            ),
        )



def main_menu(update:Update, context: CallbackContext):
    contact = update.message.contact
    phone_number = contact.phone_number
    bot = context.bot
    user = update.effective_user
    update.message.reply_text(f"✅ Raqamingiz qabul qilindi: {phone_number}",
    reply_markup=ReplyKeyboardRemove()
    )

    bot.send_message(
        chat_id=user.id,
        text = "Bosh sahifaga xush kelibsiz",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("🛍 Buyurtma berish")],
                [KeyboardButton("📦 Buyurtmalarim"), KeyboardButton("⚙️ Sozlamalar")],
                [KeyboardButton("ℹ️ Biz haqimizda"), KeyboardButton("✍️ Fikr qoldirish")]
            ],
            resize_keyboard=True,
            one_time_keyboard=True
        )
    )
def comment_user(update:Update, context: CallbackContext):
    update.message.reply_text("Adminga fikr bildiring:")
    return COMMENT
    

def read_comment(update: Update, context: CallbackContext):
    text = update.message.text
    user_id = update.message.from_user.id
    user_name = update.message.from_user.full_name
    context.bot.send_message(
        chat_id = Admin_id,
        text = f" sizga {user_name} \n id {user_id} \n {text}"
    )
    update.message.reply_text("✅ Sizning xabaringiz yuborildi. Rahmat!")
    return ConversationHandler.END