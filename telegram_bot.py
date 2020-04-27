import pyowm
import telebot

owm = pyowm.OWM('3171d33eb8ec7865bab3cac0af96ee01', language = "ru")
bot = telebot.TeleBot("1216763831:AAHOPWVNTPB93NtOJYn68kZrEpdSUIp8qPA")

@bot.message_handler(content_types=['text'])
def send_echo(message):
	observation = owm.weather_at_place(message.text)
	weather = observation.get_weather()
	temp = weather.get_temperature('celsius')["temp"]

	answer = "В городе " + message.text + " сейчас " + weather.get_detailed_status() + "." + "\n"
	answer += "Текущая температура " + str(temp) + "°." + "\n\n"

	if temp < 10:
		answer += "Надень пальто и погладь кота!"
	elif temp > 20:
		answer += "Одевайся потеплее и погладь кота два раза!" 
	else:
		answer += "Надевай, что хочешь, но кота погладь! Без кота и жизнь не та."

	bot.send_message(message.chat.id, answer) 

bot.polling(none_stop = True)
