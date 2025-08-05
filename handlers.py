from telegram import Update, ParseMode, KeyboardButton, ReplyKeyboardMarkup,ReplyKeyboardRemove
from telegram.ext import CallbackContext

def start(update: Update, context: CallbackContext):
    bot = context.bot
    user = update.effective_user

    update.message.reply_text(f"Assalomu alaykum {update.message.from_user.full_name}")

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