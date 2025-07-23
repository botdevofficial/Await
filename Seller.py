from flask import Flask
from telegram import Bot
import threading
import time

# === Configuration ===
BOT_TOKEN = '7786407965:AAHlLwNr8x_Q-2SFhHoTKaPSth9hQgdJ6rM'
MY_CHAT_ID = -123456789  # Replace with your Telegram user ID
SEND_INTERVAL = 300    # 1 hour = 3600 seconds
msg = '''
📢

Free 15 🌟 in just a few clicks and tasks

https://t.me/StarsFarmRobot?start=1795489177
'''
bot = Bot(token=BOT_TOKEN)
app = Flask(__name__)

# === Fake endpoint for UptimeRobot ===
@app.route('/health')
def health():
    return "Bot is alive ✅", 200

# === Bot background task ===
def send_alive_messages():
    while True:
        try:
            bot.send_message(chat_id=MY_CHAT_ID, text=msg)
            print("Message sent.")
        except Exception as e:
            print(f"Error sending message: {e}")
        time.sleep(SEND_INTERVAL)

# === Start bot in background ===
threading.Thread(target=send_alive_messages, daemon=True).start()

# === Start Flask app ===
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
    
