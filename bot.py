import json
import telebot
from forecast import get_weather
from boltalkaAPI import create_request, send_request

bot = telebot.TeleBot('5793077914:AAEHODd2Mhrbb4J77FPHqLNUIMjIBEAmzGk')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if "погода" in message.text.split():
        weather = get_weather()
        bot.send_message(message.from_user.id, "Погода на завтра в Москве " + str(weather.temperature('celsius')["temp"]))
    else:
        request = create_request(message.text)
        response = send_request(request)
        answer = json.loads(response.text)["responses"][2:-2]
        bot.send_message(message.from_user.id, answer)
        print(message.text + " --> " + answer)


@bot.message_handler(
    content_types=['audio', 'document', 'photo', 'sticker', 'video', 'video_note', 'voice', 'location', 'contact'])
def get_other_messages(message):
    bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEHARZjqLFE3BqMLzHpEZXsT9eqZ1CLvgAClRIAAvXQth0heMlv4jKVKywE")


bot.polling(none_stop=True, interval=0)
