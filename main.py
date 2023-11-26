import telebot
from config import token

from logic import Pokemon

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Здравствуйте! 🔥\nЭто бот для создания своего собственного покемона! ✍️\nСписок доступных команд Вы можете увидеть рядом с кнопкой отправки сообщения! 💻')


@bot.message_handler(commands=['create'])
def create(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        pokemon = Pokemon(message.from_user.username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
    else:
        bot.reply_to(
            message, 'Вы уже создали себе покемона! Посмотреть его можете по команде /pokemon 💻')


@bot.message_handler(commands=['pokemon'])
def pokemon(message):
    if message.from_user.username in Pokemon.pokemons.keys():
        pokemon = Pokemon.pokemons[message.from_user.username]
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
    else:
        bot.reply_to(
            message, 'Вы еще не создали покемона! Используйте /create для создания 💁')


bot.infinity_polling(none_stop=True)
