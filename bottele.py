import requests
import telebot

# Cấu hình bot Telegram
TOKEN = '6481990162:AAFEeTWSIPrjiQ1x3fDoOSYQRUxhWQ8YIXQ'
bot = telebot.TeleBot(TOKEN)

def print_separator():
    return "-" * 26

def get_xu(api_url):
    data = requests.get(api_url).json()
    user = data['data']['user']
    xu = data['data']['xu']
    xudie = data['data']['xudie']
    user = user[:-2] + "**"
    result = f"User: {user}\nXu: {xu}\nXudie: {xudie}"
    return result, int(xu)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Xin chào! Gõ /xu để check Xu.")

@bot.message_handler(commands=['xu'])
def get_total_xu(message):
    access_tokens = [
        'TDS0nIwEjclZXZzJiOiIXZ2V2ciwiI5gDOxIXZsRXaIZGbvRWQiojIyV2c1Jye',
        'TDSQfiETMyVmdlNnI6IiclZXZzJCLiMjc4IDMjVHawdmbh9GaiojIyV2c1Jye',
        'TDSQfiQjclZXZzJiOiIXZ2V2ciwiI6lHejVHawdmbh9GaiojIyV2c1Jye',
        'TDS9JCMxIXZ2V2ciojIyVmdlNnIsISM6lHejVHawdmbh9GaiojIyV2c1Jye',
        'TDS0nIzIXZ2V2ciojIyVmdlNnIsIiM6lHejVHawdmbh9GaiojIyV2c1Jye',
        'TDSQfiUjclZXZzJiOiIXZ2V2ciwiI1JnctpXaiojIyV2c1Jye'
    ]

    total_xu = 0
    response = ""

    for token in access_tokens:
        api_url = f"https://traodoisub.com/api/?fields=profile&access_token={token}"
        result, xu = get_xu(api_url)
        total_xu += xu
        response += result + "\n" + print_separator() + "\n"

    response += f"Total Xu: {total_xu}"
    bot.reply_to(message, response)

bot.polling()