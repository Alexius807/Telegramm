import sqlite3
import telebot

# считываем токен бота
f = open("Token.txt", encoding="utf-8")
token = f.readline()

bot = telebot.TeleBot(token)

# создаем кнопки, отражающие возможности бота
keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
keyboard.row("ANIME_PICTURES", "ROCK", "DISCOUNTS", "SITE", "METALL_FACTS", "SUPPORTED_ANIME")


# функция для старта работы бота /start. Добавляем новое ID в базу данных или приветствуем старого пользователя
@bot.message_handler(commands=['start'])
def start_message(message):
    connect = sqlite3.connect('users.db')
    cursor = connect.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS name_id(
            id INTEGER
        )""")

    connect.commit()

    people_id = message.chat.id
    cursor.execute(f"SELECT id FROM name_id WHERE id = {people_id}")
    data = cursor.fetchone()
    if data is None:
        user_id = [message.chat.id]
        cursor.execute("INSERT INTO name_id VALUES(?);", user_id)
        connect.commit()
    else:
        bot.send_message(message.chat.id, 'С возвращением!')

    chatId = message.chat.id
    text = message.text.lower()

    # стартовое сообщение
    bot.send_message(chatId,
                     "Привет. Хорошый рок музыка? Может новая аниме - аватарка? Каждый найдет что-то по вкусу) "
                     "ВНИМАНИЕ: все команды и ответы нужно вводить через слешь (/)",
                     reply_markup=keyboard)


# функция для обработки пользовательского ввода
@bot.message_handler(content_types=['text'])
def send_message(message):
    chatId = message.chat.id
    text = message.text.lower()

    # обрабатываем запросы в музыке
    if text == "rock":
        bot.send_message(chatId, "О, ты ценитель хорошей музыки! "
                                 "Чтобы избежать недопонимания, выбири степень тяжести (легкий, средний, тяжелый)")

    if text == "/легкий":
        bot.send_message(chatId, "Icepeak, Pain или Strike?")

    if text == "/icepeak":
        bot.send_audio(chatId, open("music/IC3PEAK - Dead But Pretty.mp3", "rb"))
        bot.send_audio(chatId, open("music/IC3PEAK - Красота И Сила.mp3", "rb"))
        bot.send_audio(chatId, open("music/IC3PEAK - Сказка.mp3", "rb"))
        bot.send_audio(chatId, open("music/IC3PEAK - Смерти Больше Нет.mp3", "rb"))
        bot.send_audio(chatId, open("music/IC3PEAK - Таблетки.mp3", "rb"))
        bot.send_audio(chatId, open("music/IC3PEAK feat. Ghostemane - Яма.mp3", "rb"))
        bot.send_audio(chatId, open("music/IC3PEAK feat. ZillaKami - TRRST.mp3", "rb"))
        bot.send_audio(chatId, open("music/IC3PEAK, Kim Dracula - Червь Worm.mp3", "rb"))
        bot.send_audio(chatId, open("music/IC3PEAK - Привет.mp3", "rb"))
        bot.send_audio(chatId, open(
            "music/IC3PEAK, Oli Sykes, Bring Me The Horizon - VAMPIR (feat. Oli Sykes of Bring Me The Horizon).mp3",
            "rb"))

    elif text == "/pain":
        bot.send_audio(chatId, open("music/Pain - Shut Your Mouth.mp3", "rb"))
        bot.send_audio(chatId, open("music/Pain - Bye Die.mp3", "rb"))
        bot.send_audio(chatId, open("music/Pain - Dancing With The Dead.mp3", "rb"))
        bot.send_audio(chatId, open("music/Pain - Dirty Woman.mp3", "rb"))
        bot.send_audio(chatId, open("music/Pain - Monster.mp3", "rb"))
        bot.send_audio(chatId, open("music/Pain - Nothing.mp3", "rb"))
        bot.send_audio(chatId, open("music/Pain - Same Old Song.mp3", "rb"))
        bot.send_audio(chatId, open("music/Pain - Stay Away.mp3", "rb"))
        bot.send_audio(chatId, open("music/Pain - The Great Pretender.mp3", "rb"))
        bot.send_audio(chatId, open("music/Pain - The Third Wave.mp3", "rb"))

    elif text == "/strike":
        bot.send_audio(chatId, open("music/Strike - Культ.mp3", "rb"))
        bot.send_audio(chatId, open("music/Strike - Беги.mp3", "rb"))
        bot.send_audio(chatId, open("music/Strike - Вниз Головой.mp3", "rb"))
        bot.send_audio(chatId, open("music/Strike - Время-Песок.mp3", "rb"))
        bot.send_audio(chatId, open("music/Strike - Глаза в глаза.mp3", "rb"))
        bot.send_audio(chatId, open("music/Strike - Кто.mp3", "rb"))
        bot.send_audio(chatId, open("music/Strike - Мы мир перевернём.mp3", "rb"))
        bot.send_audio(chatId, open("music/Strike - На одной волне.mp3", "rb"))
        bot.send_audio(chatId, open("music/Strike - Паранойя.mp3", "rb"))
        bot.send_audio(chatId, open("music/Strike - Плачь.mp3", "rb"))
        bot.send_audio(chatId, open("music/Strike - Это не грех.mp3", "rb"))

    elif text == "/средний":
        bot.send_message(chatId, "Disturbed, Slipknot или Dope?")

    if text == "/slipknot":
        bot.send_audio(chatId, open("music/Slipknot - Spit It Out.mp3", "rb"))
        bot.send_audio(chatId, open("music/Slipknot - The Devil in I.mp3", "rb"))
        bot.send_audio(chatId, open("music/Slipknot - All Out Life.mp3", "rb"))
        bot.send_audio(chatId, open("music/Slipknot - Before I Forget.mp3", "rb"))
        bot.send_audio(chatId, open("music/Slipknot - Duality.mp3", "rb"))
        bot.send_audio(chatId, open("music/Slipknot - I Am Hated.mp3", "rb"))
        bot.send_audio(chatId, open("music/Slipknot - Nero Forte.mp3", "rb"))
        bot.send_audio(chatId, open("music/Slipknot - Psychosocial.mp3", "rb"))
        bot.send_audio(chatId, open("music/Slipknot - Wait and Bleed.mp3", "rb"))
        bot.send_audio(chatId, open("music/Slipknot - Scream.mp3", "rb"))

    elif text == "/dope":
        bot.send_audio(chatId, open("music/Dope - Die MF Die.mp3", "rb"))
        bot.send_audio(chatId, open("music/Dope - Bitch.mp3", "rb"))
        bot.send_audio(chatId, open("music/Dope - Burn.mp3", "rb"))
        bot.send_audio(chatId, open("music/Dope - Debonaire.mp3", "rb"))
        bot.send_audio(chatId, open("music/Dope - I'm Back.mp3", "rb"))
        bot.send_audio(chatId, open("music/Dope - Now Or Never.mp3", "rb"))
        bot.send_audio(chatId, open("music/Dope - Slipping Away.mp3", "rb"))
        bot.send_audio(chatId, open("music/Dope - Take Your Best Shot.mp3", "rb"))
        bot.send_audio(chatId, open("music/Dope - Thanks For Nothing.mp3", "rb"))
        bot.send_audio(chatId, open("music/Dope - What About....mp3", "rb"))

    elif text == "/disturbed":
        bot.send_audio(chatId, open("music/Disturbed - Are You Ready.mp3", "rb"))
        bot.send_audio(chatId, open("music/Disturbed - Decadence.mp3", "rb"))
        bot.send_audio(chatId, open("music/Disturbed - Down with the Sickness.mp3", "rb"))
        bot.send_audio(chatId, open("music/Disturbed - Immortalized.mp3", "rb"))
        bot.send_audio(chatId, open("music/Disturbed - Legion of Monsters.mp3", "rb"))
        bot.send_audio(chatId, open("music/Disturbed - Never Wrong.mp3", "rb"))
        bot.send_audio(chatId, open("music/Disturbed - No More.mp3", "rb"))
        bot.send_audio(chatId, open("music/Disturbed - Pain Redefined.mp3", "rb"))
        bot.send_audio(chatId, open("music/Disturbed - Ten Thousand Fists.mp3", "rb"))
        bot.send_audio(chatId, open("music/Nita Strauss, David Draiman, Disturbed - Dead Inside.mp3", "rb"))

    elif text == "/тяжелый":
        bot.send_message(chatId, "Slaughter, Shadow или Ghostkid?")

    if text == "/slaughter":
        bot.send_audio(chatId, open("music/Slaughter To Prevail - Father.mp3", "rb"))
        bot.send_audio(chatId, open("music/Slaughter To Prevail - Chronic Slaughter.mp3", "rb"))
        bot.send_audio(chatId, open("music/Slaughter To Prevail - Bonebreaker.mp3", "rb"))
        bot.send_audio(chatId, open("music/Slaughter To Prevail - 666.mp3", "rb"))
        bot.send_audio(chatId, open("music/Slaughter To Prevail - Agony.mp3", "rb"))
        bot.send_audio(chatId, open("music/Slaughter To Prevail - Baba Yaga.mp3", "rb"))
        bot.send_audio(chatId, open("music/Slaughter To Prevail - Demolisher.mp3", "rb"))
        bot.send_audio(chatId, open("music/Slaughter To Prevail - Head On A Plate.mp3", "rb"))
        bot.send_audio(chatId, open("music/Slaughter To Prevail - King.mp3", "rb"))
        bot.send_audio(chatId, open("music/Slaughter To Prevail - Made In Russia.mp3", "rb"))

    elif text == "/shadow":
        bot.send_audio(chatId, open("music/Shadow of Intent - Melancholy.mp3", "rb"))
        bot.send_audio(chatId, open("music/Shadow of Intent - Chthonic Odyssey.mp3", "rb"))
        bot.send_audio(chatId, open("music/Shadow of Intent - Farewell.mp3", "rb"))
        bot.send_audio(chatId, open("music/Shadow of Intent - From Ruin... We Rise.mp3", "rb"))
        bot.send_audio(chatId, open("music/Shadow of Intent - Gravesinger.mp3", "rb"))
        bot.send_audio(chatId, open("music/Shadow of Intent - Of Fury.mp3", "rb"))
        bot.send_audio(chatId, open("music/Shadow of Intent - Saurian King.mp3", "rb"))
        bot.send_audio(chatId, open("music/Shadow of Intent - The Coming Fire.mp3", "rb"))
        bot.send_audio(chatId, open("music/Shadow of Intent - The Heretic Prevails.mp3", "rb"))
        bot.send_audio(chatId, open(
            "music/Shadow of Intent feat. Trevor Strnad - Barren and Breathless Macrocosm (feat. Trevor Strnad).mp3",
            "rb"))

    elif text == "/ghostkid":
        bot.send_audio(chatId, open("music/GHØSTKID - ZERØ.mp3", "rb"))
        bot.send_audio(chatId, open("music/GHØSTKID - FØØL (INHUMAN Remix).mp3", "rb"))
        bot.send_audio(chatId, open("music/Ghostkid - START A FIGHT.mp3", "rb"))
        bot.send_audio(chatId, open("music/Ghostkid - UGLY.mp3", "rb"))
        bot.send_audio(chatId, open("music/Ghostkid - YOU & I.mp3", "rb"))
        bot.send_audio(chatId, open("music/Ghostkid, Johnny 3 Tears - This Is Not Hollywood.mp3", "rb"))
        bot.send_audio(chatId, open(
            "music/GHØSTKID feat. Heaven Shall Burn - SUPERNØVA (feat. Marcus Bischoff of Heaven Shall Burn).mp3",
            "rb"))

    # обрабатываем запросы картинок
    if text == "anime_pictures":
        bot.send_message(chatId, "Героев какого аниме ты хочешь увидеть?")

    if text == "/tokyo ghoul" or text == "/токийский гуль":
        bot.send_photo(chatId, open("pictures/Kaneki.jpg", "rb"))
        bot.send_photo(chatId, open("pictures/Sova.jpg", "rb"))
        bot.send_photo(chatId, open("pictures/Eto.png", "rb"))
        bot.send_photo(chatId, open("pictures/Toka.jpg", "rb"))
        bot.send_photo(chatId, open("pictures/juzo.jpg", "rb"))
        bot.send_photo(chatId, open("pictures/kanekiblack.jpg", "rb"))
        bot.send_photo(chatId, open("pictures/Rize.jpg", "rb"))
        bot.send_photo(chatId, open("pictures/taki.png", "rb"))
        bot.send_photo(chatId, open("pictures/ayto.jpg", "rb"))
        bot.send_photo(chatId, open("pictures/tatara.png", "rb"))

    elif text == "/seven deadly sins" or text == "/семь смертных грехов":
        bot.send_photo(chatId, open("pictures/meliodas.jpg", "rb"))
        bot.send_photo(chatId, open("pictures/merlin.jpg", "rb"))
        bot.send_photo(chatId, open("pictures/ban.jpg", "rb"))
        bot.send_photo(chatId, open("pictures/escanor.jpg", "rb"))
        bot.send_photo(chatId, open("pictures/5.jpg", "rb"))
        bot.send_photo(chatId, open("pictures/astarosa.jpg", "rb"))
        bot.send_photo(chatId, open("pictures/zel.jpg", "rb"))

    elif text == "/magic battle" or text == "/магическая битва":
        bot.send_photo(chatId, open("pictures/satoru.jpg", "rb"))
        bot.send_photo(chatId, open("pictures/sucuna.jpg", "rb"))
        bot.send_photo(chatId, open("pictures/fusiguro.jpg", "rb"))
        bot.send_photo(chatId, open("pictures/nobara.jpg", "rb"))
        bot.send_photo(chatId, open("pictures/brat.jpg", "rb"))
        bot.send_photo(chatId, open("pictures/druid.png", "rb"))
        bot.send_photo(chatId, open("pictures/ucitel.png", "rb"))

    elif text == "/vinland saga" or text == "/сага о винланде":
        bot.send_photo(chatId, open("pictures/troe.jpg", "rb"))
        bot.send_photo(chatId, open("pictures/torkil.png", "rb"))
        bot.send_photo(chatId, open("pictures/torfin.jpg", "rb"))
        bot.send_photo(chatId, open("pictures/yoms-vikings.jpg", "rb"))
        bot.send_photo(chatId, open("pictures/Торфинн-суров.jpg", "rb"))
        bot.send_photo(chatId, open("pictures/battle.png", "rb"))
        bot.send_photo(chatId, open("pictures/ASKELAT.jpg", "rb"))

    elif text == "/berserk" or text == "/берсерк":
        bot.send_photo(chatId, open("pictures/bers1.jpg", "rb"))
        bot.send_photo(chatId, open("pictures/bers2.jpg", "rb"))
        bot.send_photo(chatId, open("pictures/bers3.jpg", "rb"))
        bot.send_photo(chatId, open("pictures/bers4.jpg", "rb"))

    elif text == "/black lagoon" or text == "/пираты черной лагуны":
        bot.send_photo(chatId, open("pictures/pirates1.jpg", "rb"))
        bot.send_photo(chatId, open("pictures/pirates2.png", "rb"))
        bot.send_photo(chatId, open("pictures/pirates3.jpg", "rb"))
        bot.send_photo(chatId, open("pictures/pirates4.jpg", "rb"))
        bot.send_photo(chatId, open("pictures/pirates5.jpg", "rb"))
        bot.send_photo(chatId, open("pictures/pirates6.jpg", "rb"))
        bot.send_photo(chatId, open("pictures/pirates7.jpg", "rb"))

    elif text == "/sword art online" or text == "/мастера меча онлайн":
        bot.send_photo(chatId, open("pictures/sao1.jpg", "rb"))
        bot.send_photo(chatId, open("pictures/sao2.jpg", "rb"))
        bot.send_photo(chatId, open("pictures/sao3.jpg", "rb"))
        bot.send_photo(chatId, open("pictures/sao4.jpg", "rb"))
        bot.send_photo(chatId, open("pictures/sao5.jpg", "rb"))
        bot.send_photo(chatId, open("pictures/sao6.jpg", "rb"))
        bot.send_photo(chatId, open("pictures/sao7.jpg", "rb"))

    elif text == "/akame ga kill" or text == "/убийца акаме":
        bot.send_photo(chatId, open("pictures/akame1.jpg", "rb"))
        bot.send_photo(chatId, open("pictures/akame2.jpg", "rb"))
        bot.send_photo(chatId, open("pictures/akame3.jpg", "rb"))
        bot.send_photo(chatId, open("pictures/akame4.jpg", "rb"))
        bot.send_photo(chatId, open("pictures/akame5.jpg", "rb"))
        bot.send_photo(chatId, open("pictures/akame6.jpg", "rb"))
        bot.send_photo(chatId, open("pictures/akame7.jpg", "rb"))
        bot.send_photo(chatId, open("pictures/akame8.jpg", "rb"))
        bot.send_photo(chatId, open("pictures/akame9.jpg", "rb"))
        bot.send_photo(chatId, open("pictures/akame10.png", "rb"))

    elif text == "/war 12" or text == "/война 12":
        bot.send_photo(chatId, open("pictures/war12.jpg", "rb"))
        bot.send_photo(chatId, open("pictures/war121.jpg", "rb"))
        bot.send_photo(chatId, open("pictures/122.jpg", "rb"))
        bot.send_photo(chatId, open("pictures/123.png", "rb"))
        bot.send_photo(chatId, open("pictures/124.jpg", "rb"))
        bot.send_photo(chatId, open("pictures/125.jpg", "rb"))
        bot.send_photo(chatId, open("pictures/126.jpg", "rb"))

    elif text == "/demon slayer" or text == "/клинок рассекающий демонов":
        bot.send_photo(chatId, open("pictures/krd1.jpg", "rb"))
        bot.send_photo(chatId, open("pictures/krd2.jpg", "rb"))
        bot.send_photo(chatId, open("pictures/krd3.jpg", "rb"))
        bot.send_photo(chatId, open("pictures/krd4.jpg", "rb"))
        bot.send_photo(chatId, open("pictures/krd5.jpg", "rb"))
        bot.send_photo(chatId, open("pictures/krd6.jpg", "rb"))
        bot.send_photo(chatId, open("pictures/krd7.jpg", "rb"))
        bot.send_photo(chatId, open("pictures/krd8.jpg", "rb"))
        bot.send_photo(chatId, open("pictures/krd9.jpg", "rb"))
        bot.send_photo(chatId, open("pictures/krd10.jpg", "rb"))

    elif text == "/naruto" or text == "/наруто":
        bot.send_photo(chatId, open("pictures/nar1.jpg", "rb"))
        bot.send_photo(chatId, open("pictures/nar2.jpg", "rb"))
        bot.send_photo(chatId, open("pictures/nar3.png", "rb"))
        bot.send_photo(chatId, open("pictures/nar4.png", "rb"))
        bot.send_photo(chatId, open("pictures/nar5.png", "rb"))
        bot.send_photo(chatId, open("pictures/nar6.jpg", "rb"))
        bot.send_photo(chatId, open("pictures/nar7.jpg", "rb"))
        bot.send_photo(chatId, open("pictures/nar8.png", "rb"))
        bot.send_photo(chatId, open("pictures/nar9.jpg", "rb"))
        bot.send_photo(chatId, open("pictures/nar10.jpg", "rb"))
    # вывод сайта стим с скидками
    elif text == "discounts":
        bot.send_message(chatId, "Посмотри, что сейчас со скидкой: https://store.steampowered.com/specials/?l=russian")
    # сайт для онлайн просмотра аниме
    elif text == "site":
        bot.send_message(chatId, "Сайт для комфортного просмотра с хорошей озвучкой: https://animego.org")
    # Кому - то может быть интересно
    elif text == "metall_facts":
        bot.send_message(chatId, "Вот несколько интересных фактов о тяжелой музыке:")
        bot.send_message(chatId, "- Тяжелый металл снижает давление и выравнивает сердцебиение")
        bot.send_message(chatId, "- Агрессивная музыка помогает бороться с депрессиями, злостью и раздражением")
        bot.send_message(chatId, "- Классика успокаевает и уменьшает тревогу в организме человека хуже чем металл")
        bot.send_message(chatId,
                         " - 80 % Людей - металлистов чувствуют себя намного более счастливыми при прослушивании своей любимой музыки чем слушатели реп или поп музыки")
        bot.send_message(chatId,
                         "- Со временем сами исполнители тяжелой музыки начинают слушать классику и более спокойную музыку")
    elif text == "supported_anime":
        bot.send_message(chatId, "Доступны картинки:")
        bot.send_message(chatId, "/tokyo ghoul или /токийский гуль")
        bot.send_message(chatId, "/magic battle или /магическая битва")
        bot.send_message(chatId, "/vinland saga или /сага о винланде")
        bot.send_message(chatId, "/seven deadly sins или /семь смертных грехов")
        bot.send_message(chatId, "/akame ga kill или /убийца акаме")
        bot.send_message(chatId, "/sword art online или /мастера меча")
        bot.send_message(chatId, "/berserk или /берсерк")
        bot.send_message(chatId, "/war 12 или /война 12")
        bot.send_message(chatId, "/naruto или /наруто")
        bot.send_message(chatId, "/demon slayer или /клинок рассекающий демонов")
        bot.send_message(chatId, "/black lagoon или /пираты черной лагуны")


    elif text == "пока":
        bot.send_message(chatId, "До свидания!")


bot.polling()
