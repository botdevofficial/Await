import asyncio
from flask import Flask
from telegram import Bot
from telegram.constants import ParseMode
import threading

# === Configuration ===
BOT_TOKEN = '7786407965:AAHlLwNr8x_Q-2SFhHoTKaPSth9hQgdJ6rM'
MY_CHAT_ID = -1002613165023
SEND_INTERVAL = 600  # 5 minutes

msg = '''
<b>please join</b>

<a href="https://t.me/share/url?url=https://t.me/+K8pQ_KJ4tF9mMjM1">SHARE</a>

https://t.me/+K8pQ_KJ4tF9mMjM1
'''

bot = Bot(token=BOT_TOKEN)
app = Flask(__name__)

# === Fake endpoint for uptime robot ===
@app.route('/health')
def health():
    return "Bot is alive ✅", 200

# === Async background task ===
async def send_alive_messages():
    while True:
        try:
            print("Trying to send message...")
            await bot.send_message(chat_id=MY_CHAT_ID, text=msg, parse_mode=ParseMode.HTML)
            print("Message sent.")
        except Exception as e:
            print(f"Error sending message: {e}")
        await asyncio.sleep(SEND_INTERVAL)

# === Start async task in separate thread ===
def start_async_loop():
    asyncio.run(send_alive_messages())

if __name__ == '__main__':
    # Start bot loop in background thread
    threading.Thread(target=start_async_loop, daemon=True).start()
    # Start Flask app
    app.run(host="0.0.0.0", port=8080)
