import telebot

bot = telebot.TeleBot('5116455777:AAGQMXmIX-Aa7CulygNaHdxAaQmZVKFQh_k')


@bot.message_handler(content_types=['text'])
def send_message(message):
    chatId = message.chat.id
    text = message.text.lower()
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
    if text == "/pain":
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
    if text == "/strike":
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
    if text == "/средний":
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
    if text == "/dope":
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
    if text == "/disturbed":
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
    if text == "/тяжелый":
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
    if text == "/shadow":
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
    if text == "/ghostkid":
        bot.send_audio(chatId, open("music/GHØSTKID - ZERØ.mp3", "rb"))
        bot.send_audio(chatId, open("music/GHØSTKID - FØØL (INHUMAN Remix).mp3", "rb"))
        bot.send_audio(chatId, open("music/Ghostkid - START A FIGHT.mp3", "rb"))
        bot.send_audio(chatId, open("music/Ghostkid - UGLY.mp3", "rb"))
        bot.send_audio(chatId, open("music/Ghostkid - YOU & I.mp3", "rb"))
        bot.send_audio(chatId, open("music/Ghostkid, Johnny 3 Tears - This Is Not Hollywood.mp3", "rb"))
        bot.send_audio(chatId, open(
            "music/GHØSTKID feat. Heaven Shall Burn - SUPERNØVA (feat. Marcus Bischoff of Heaven Shall Burn).mp3",
            "rb"))