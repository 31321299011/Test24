import telebot
import time

# আপনার দেওয়া টোকেন
TOKEN = "8264679566:AAFpbMd_g6Tbv3GfShREtCM0CW078ujPixY"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "আসসালামু আলাইকুম! আপনার বটটি এখন GitHub-এ হোস্ট করা অবস্থায় সচল আছে।")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"আপনি বলেছেন: {message.text}")

while True:
    try:
        print("Bot is running...")
        bot.polling(none_stop=True)
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(15)
