import asyncio
from flask import Flask
from telegram import Bot
from telegram.constants import ParseMode

# === Configuration ===
BOT_TOKEN = '7786407965:AAHlLwNr8x_Q-2SFhHoTKaPSth9hQgdJ6rM'
MY_CHAT_ID = -1002613165023  # your group chat ID
SEND_INTERVAL = 300  # in seconds (5 mins)

msg = '''
hello 🤗 
nice to meet you
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

# === Run asyncio task in background ===
def start_loop():
    loop = asyncio.get_event_loop()
    loop.create_task(send_alive_messages())
    app.run(host="0.0.0.0", port=8080)

# === Entry point ===
if __name__ == '__main__':
    start_loop()
