import telebot

bot = telebot.TeleBot('5116455777:AAGQMXmIX-Aa7CulygNaHdxAaQmZVKFQh_k')

keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
keyboard.row("ANIME_PICTURES", "ROCK", "DISCOUNTS", "SITE")


@bot.message_handler(commands=['start'])
def start_message(message):
    chatId = message.chat.id
    text = message.text.lower

    bot.send_message(chatId, "Привет. Хорошый рок? Может аниме? Каждый найдет что-то по вкусу)", reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def send_message(message):
    chatId = message.chat.id
    text = message.text.lower()
    if text == "rock":
        bot.send_message(chatId, "О, ты ценитель хорошей музыки! "
                                 "Чтобы избежать недопонимания, выбири степень тяжести (легкий, средний, тяжелый)")
    if text == "легкий":
        bot.send_audio(chatId, open("music/Pain - Shut Your Mouth.mp3", "rb"))
        bot.send_audio(chatId, open("music/IC3PEAK - Dead But Pretty.mp3", "rb"))
        bot.send_audio(chatId, open("music/Strike - Культ.mp3", "rb"))
    if text == "средний":
        bot.send_audio(chatId, open("music/Dope - Die MF Die.mp3", "rb"))
        bot.send_audio(chatId, open("music/Slipknot - Spit It Out.mp3", "rb"))
        bot.send_audio(chatId, open("music/Slipknot - The Devil in I.mp3", "rb"))
    if text == "тяжелый":
        bot.send_audio(chatId, open("music/GHØSTKID - ZERØ.mp3", "rb"))
        bot.send_audio(chatId, open("music/Slaughter To Prevail - Father.mp3", "rb"))
        bot.send_audio(chatId, open("music/Slaughter To Prevail - Chronic Slaughter.mp3", "rb"))
        bot.send_audio(chatId, open("music/Slaughter To Prevail - Bonebreaker.mp3", "rb"))
        bot.send_audio(chatId, open("music/Slaughter To Prevail - 666.mp3", "rb"))
        bot.send_audio(chatId, open("music/Shadow of Intent - Melancholy.mp3", "rb"))
        bot.send_audio(chatId, open("music/Shadow of Intent - Chthonic Odyssey.mp3", "rb"))
        bot.send_audio(chatId, open("music/Bury Tomorrow - Choke.mp3", "rb"))
        bot.send_audio(chatId, open(
            "music/GHØSTKID feat. Heaven Shall Burn - SUPERNØVA (feat. Marcus Bischoff of Heaven Shall Burn).mp3",
            "rb"))

    elif text == "anime_pictures":
        bot.send_message(chatId, "Героев какого аниме ты хочешь увидеть?")

    if text == "tokyo ghoul" or text == "токийский гуль":
        bot.send_photo(chatId, open("pictures/Kaneki.jpg", "rb"))
        bot.send_photo(chatId, open("pictures/Sova.jpg", "rb"))
        bot.send_photo(chatId, open("pictures/Eto.png", "rb"))
        bot.send_photo(chatId, open("pictures/Toka.jpg", "rb"))

    if text == "seven deadly sins" or text == "семь смертных грехов":
        bot.send_photo(chatId, open("pictures/meliodas.jpg", "rb"))
        bot.send_photo(chatId, open("pictures/merlin.jpg", "rb"))
        bot.send_photo(chatId, open("pictures/ban.jpg", "rb"))
        bot.send_photo(chatId, open("pictures/escanor.jpg", "rb"))
        bot.send_photo(chatId, open("pictures/king.jpg", "rb"))
    elif text == "discounts":
        bot.send_message(chatId, "Посмотри, что сейчас со скидкой: https://store.steampowered.com/specials/?l=russian")
    elif text == "site":
        bot.send_message(chatId, "Сайт с хорошей озвучкой: https://animego.org")
    elif text == "пока":
        bot.send_message(chatId, "пока")


bot.polling()
