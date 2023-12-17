from telebot import TeleBot
import biography

bot = TeleBot('6827623190:AAGmU9pWf2lslop65xIeksizfYaKQgxnItk')

help_message = \
    """Я умею:
/help или /помощь - узнать, что я умею
/bio или /биография - расскажу биографию, которая известна всему миру о Фрэнке Абигнейле
/publ или /публикации - покажу известнейшие книги и фильмы о Фрэнке Абигнейле
/facts или /факты - игра, в которой тебе нужно угадать реальные факты 
/true_video или /разоблачающее_видео - расследование о Фрэнке Абигнейле
     """


@bot.message_handler(commands=['start'])
def bot_start(message):
    bot.send_message(message.chat.id,
                     text=f"Привет, {message.from_user.first_name} " + help_message)


@bot.message_handler(commands=['help', 'помощь'])
def bot_help(message):
    bot.send_message(message.chat.id, text=help_message)


@bot.message_handler(commands=['bio', 'биография'])
def bot_biography(message):
    bot.send_message(message.chat.id, text=biography.about_person)
    bot.send_photo(message.chat.id, photo="https://ibb.org.ru/images/2023/12/16/scale_1200.jpg",
                   caption="Фрэнк Абигнейл")


@bot.message_handler(commands=['publ', 'публикации'])
def bot_publ(message):
    bot.send_message(message.chat.id,
                     text="<a href='https://www.youtube.com/watch?v=vsMydMDi3rI '>Видео</a>, где Фрэнк Абигнейл выстапает на ежегодной конференции Google Talk",
                     parse_mode='HTML')
    bot.send_message(message.chat.id,
                     text="<a href='https://www.kinopoisk.ru/film/324/?utm_referrer=www.google.com'>Фильм</a> про Фрэнка Абигнейла с Леонардо Ди Каприо",
                     parse_mode='HTML')
    bot.send_message(message.chat.id,
                     text="<a href='https://www.litres.ru/book/frenk-abigneyl/poymay-menya-esli-smozhesh-realnaya-istoriya-samogo-neulovi-23214488/'>Автобиография</a> Фрэнка Абигнейла",
                     parse_mode='HTML')


@bot.message_handler(commands=['facts', 'факты'])
def bot_publ(message):
    bot.send_message(message.chat.id,
                     text="""Введи номера тех фактов (по одному в сообщении) из нижепреведенного списка, которые кажутся тебе верными. А когда захочешь остановиться вводить номера фактов, отправь 0 отдельным сообщением""")
    bot.send_message(message.chat.id, text=biography.print_facts(), parse_mode='HTML')


def is_in_facts(message):
    if message.text.isdigit() and 1 <= int(message.text) <= 6:
        return True
    return False


@bot.message_handler(func=is_in_facts)
def bot_publ(message):
    bot.send_message(message.chat.id, text=biography.print_com(int(message.text)))
    print(biography.input_facts)


def is_end(message):
    if message.text.isdigit() and int(message.text) == 0:
        return True
    return False


@bot.message_handler(func=is_end)
def bot_publ(message):
    # print(biography.forgot)
    bot.send_message(message.chat.id, text=biography.print_forgotten())


@bot.message_handler(commands=['true_video', 'разоблачающее_видео'])
def bot_publ(message):
    bot.send_message(message.chat.id,
                     text="Как ты наверное уже понял, совершенно не все, что известно о Фрэнке Абигнейле является правдной. Если хочешь ее узнать, то можешь посмотреть видео по <a href='https://www.youtube.com/watch?v=Dan-jPgWGqM'>ссылке</a>",
                     parse_mode='HTML')


bot.polling()
