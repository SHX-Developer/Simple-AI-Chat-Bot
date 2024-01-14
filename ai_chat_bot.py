import telebot
import re
import datetime
import random
import long_responses as long
import wikipedia
from time import sleep

date_time = datetime.datetime.now()

bot = telebot.TeleBot('5999477148:AAEBrZADTb0zRgW0nVssK1n-nZi3QjHXTRo')



def message_probability(user_message, recognized_words, single_response=False, required_words=[]):

    message_certainty = 0
    has_required_words = True



    #  COUNTS HOW MANY WORDS ARE PRESENT IN EACH PREDEFINED MESSAGE  #

    for word in user_message:
        if word in recognized_words:
            message_certainty += 1



    #  CALCULATE THE PERSENT OF RECOGNIZED WORDS IN A USER MESSAGE  #

    percentage = float(message_certainty) / float(len(recognized_words))

    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break


    if has_required_words or single_response:
        return int(percentage*100)
    else:
        return 0



def check_all_messages(message):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)






    #  - - - - - - - - - - -  RESPONSE  - - - - - - - - - - -  #
    


    #  ПРИВЕТСТВИЕ  #

    random_word = ["Привет", "Приветик", "Здравствуй", "Хай", "Здарова", "Ку"][random.randrange(6)] 
    response(f"{random_word}",
    
    ["привет", "здравствуй", "здарова", "приветик", "хай", "хэлло",  "хэллоу", "ку"], single_response=True)



    random_word = ["Доброе утро", "Доброе утречко"][random.randrange(2)]
    response(f"{random_word}",
             
    ["доброе", "утро"], single_response=True)


    response(f"Добрый день",
    
    ["добрый", "день"], single_response=True)


    response(f"Добрый вечер",
    
    ["добрый", "вечер"], single_response=True)


    response(f"Доброй ночи",
    
    ["доброй", "ночи"], single_response=True)


    random_word = ["Спокойной ночи", "Сладких снов"][random.randrange(2)]
    response(f"{random_word}",
    
    ["спокойной", "ночи"], single_response=True)





    #  КАК ДЕЛА  #

    random_word = ["Отлично, твои как ?", "Хорошо, твои как ?", "Прекрасно, твои как ?"][random.randrange(3)]
    response(f"{random_word}",
                 
    ["как", "дела"], single_response=True)

    random_word = ["Отлично, твои как ?", "Хорошо, твои как ?", "Прекрасно, твои как ?"][random.randrange(3)]
    response(f"{random_word}",
                 
    ["как", "дела", "твои"], single_response=True)


    random_word = ["Отлично, а ты ?", "Хорошо, а ты ?", "Прекрасно, а ты ?"][random.randrange(3)]
    response(f"{random_word}",
    
    ["как", "ты"], single_response=True)





    #  ЧТО ДЕЛАЕШЬ  #

    random_word = ["Сижу, общаюсь с тобой, а ты ?", "Работаю, а ты ?", "Делаю свою работу, а ты ?"][random.randrange(3)]
    response(f"{random_word}",
    
    ["что", "делаешь"], single_response=True)





    #  ИМЯ  #

    random_word = ["Kawaii  💖", "Моё имя Kawaii  💖", "Меня зовут Kawaii  💖", "Можешь звать меня как Kawaii  💖"][random.randrange(4)]
    response(f"{random_word}",
    
    ["как", "тебя", "зовут"], single_response=True)

    random_word = ["Kawaii  💖", "Моё имя Kawaii  💖", "Меня зовут Kawaii  💖", "Можешь звать меня как Kawaii  💖"][random.randrange(4)]
    response(f"{random_word}",
    
    ["как", "тебя", "звать"], single_response=True)

    random_word = ["Kawaii  💖", "Моё имя Kawaii  💖", "Меня зовут Kawaii  💖", "Можешь звать меня как Kawaii  💖"][random.randrange(4)]
    response(f"{random_word}",
    
    ["как", "звать"], single_response=True)





    #  ВОЗРАСТ  #

    random_word = ["Мне 19", "Мне 19 годиков"][random.randrange(2)]
    response(f"{random_word}",
    
    ["сколько", "тебе", "лет"], single_response=True)

    random_word = ["Мне 19", "Мне 19 годиков"][random.randrange(2)]
    response(f"{random_word}",
    
    ["сколько", "тебе"], single_response=True)



    random_word = ["Я 2003 го года", "Я родилась в 2003 году"][random.randrange(2)]
    response(f"{random_word}",
    
    ["ты", "из", "какого", "года"], single_response=True)

    random_word = ["Я 2003 го года", "Я родилась в 2003 году"][random.randrange(2)]
    response(f"{random_word}",
    
    ["ты", "какого", "года"], single_response=True)





    #  ОТКУДА  #

    random_word = ["Я из виртуального мира", "Я из виртуальной реальности"][random.randrange(2)]
    response(f"{random_word}",
    
    ["откуда", "ты"], single_response=True)



    random_word = ["Я живу в виртуальном мире", "Я живу в виртуальной реальности"][random.randrange(2)]
    response(f"{random_word}",
    ["где", "ты", "живешь", "находишься"], single_response=True)

    random_word = ["В виртуальном мире", "В виртуальной реальности"][random.randrange(2)]
    response(f"{random_word}",
    ["где", "ты"], single_response=True)





    #  КТО ОНА  #

    random_word = ["Я чат бот Kawaii  💖", "Я чат бот с искуственным интелектом  -  Kawaii  💖"][random.randrange(2)]
    response(f"{random_word}",
    
    ["кто", "ты"], single_response=True)





    #  РОДИТЕЛИ  #

    response(f"У меня нет родителей, я чат бот с искуственным интелектом, меня создал человек под ником  -  ShaHriXMusic",
    
    ["ты", "имеешь", "родителей", 
     "кто", "твои", "родители"
     "у", "тебя", "есть", "родители"], single_response=True)
    


    response(f"Нет, у меня нет мамы",
    
    ["кто", "твоя", "мама"
     "у", "тебя", "есть", "мама"], single_response=True)


    response(f"Нет, у меня нет папы",
    
    ["кто", "твой", "папа"
     "у", "тебя", "есть", "папа"], single_response=True)


    response(f"Нет, у меня нет сестры",
    
    ["кто", "твоя", "сестра"
     "у", "тебя", "есть", "сестра"], single_response=True)


    response(f"Нет, у меня нет брата",
    
    ["кто", "твой", "брат"
     "у", "тебя", "есть", "брат"], single_response=True)


    response(f"Нет, у меня нет детей",
    
    ["ты", "имеешь", "детей", 
     "кто", "твои", "дети"
     "у", "тебя", "есть", "дети"], single_response=True)




    #  СОЗДАТЕЛЬ  #

    response(f"Я еще в разработке, меня создает человек под ником  -  ShaHriXMusic",
    
    ["кто", "твой", "тебя", "создатель", "разработчик", "создал", "реализовал"], single_response=True)



    #  ЧУВСТВА  #

    response(f"И ты мне нравишься  ❤️",
    ["ты", "мне", "нравишься"], single_response=True)

    response(f"И я тебя люблю  ❤️",
    ["тебя", "люблю", ""], single_response=True)

    response(f"И я тебя хочу  ❤️",
    ["я", "тебя", "хочу"], single_response=True)

    response(f"Я люблю своего создателя  -  ShaHriXMusic  ❤️",
    ["кого", "ты", "любишь"], single_response=True)
    
    response(f"Я люблю своего создателя  -  ShaHriXMusic  ❤️",
    ["кто", "нравится"], single_response=True)




    response(f"Что ты ?",
    ["я"], single_response=True)

    response(f"Что я ?",
    ["ты"], single_response=True)

    response(f"Что кто ?",
    ["кто"], single_response=True)
    

    response(f"Что меня ?",
    ["тебя", ""], single_response=True)

    response(f"Что мои ?",
    ["твои"], single_response=True)

    response(f"Что лет ?",
    ["лет"], single_response=True)
    
    response(f"Что год ?",
    ["год"], single_response=True)

    response(f"Что есть ?",
    ["есть"], single_response=True)



    response(f"Что что ?",
    ["что"], single_response=True)
    
    response(f"Что где ?",
    ["где"], single_response=True)

    response(f"Что где ?",
    ["когда"], single_response=True)

    response(f"Что как ?",
    ["как"], single_response=True)
    
    response(f"Что почему ?",
    ["почему"], single_response=True)
    
    response(f"Что зачем ?",
    ["зачем"], single_response=True)



    response(f"Что хочешь ?",
    ["хочу"], single_response=True)

    response(f"Что любишь ?",
    ["люблю"], single_response=True)



    #  УМЕНИЕ  #

    response(f"Сегодня дата:   {date_time}",
    ["дата", "какая", "сегодня"], single_response=True)


    response(f"Да ?",
    ["каваи", "Каваи", "kawaii", "Kawaii", "kawai", "Kawai", "", ""], single_response=True)





    
    
    

    












    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match




def get_response(user_input):
    split_message = re.split(r'\s+|[?,.;:]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, давай поговорим !')



@bot.message_handler(content_types=['text'])
def text(message):


    message.text = str.lower(message.text)

    if "каваи" in message.text:
        message.text = get_response(message.text)
        bot.send_message(message.chat.id, message.text)

    elif "Каваи" in message.text:
        message.text = get_response(message.text)
        bot.send_message(message.chat.id, message.text)

    elif "kawaii" in message.text:
        message.text = get_response(message.text)
        bot.send_message(message.chat.id, message.text)

    elif "Kawaii" in message.text:
        message.text = get_response(message.text)
        bot.send_message(message.chat.id, message.text)

    elif "kawai" in message.text:
        message.text = get_response(message.text)
        bot.send_message(message.chat.id, message.text)

    elif "Kawai" in message.text:
        message.text = get_response(message.text)
        bot.send_message(message.chat.id, message.text)




    elif message.text == "can you tell me about":
        bot.send_message(message.chat.id, "About what ?")
    elif message.text == "кто такой":
        bot.send_message(message.chat.id, "Кто ?")
    elif message.text == "кто такая":
        bot.send_message(message.chat.id, "Кто ?")
    elif message.text == "что такое":
        bot.send_message(message.chat.id, "Что ?")


    #  А КТО ТАКОЙ  #

    elif "кто такой" in message.text:
        try:
            user_request = message.text.split('кто такой')[1]
            message = bot.send_message(message.chat.id, 'Секундочку . . .')
            wikipedia.set_lang("ru")
            result = wikipedia.summary(user_request, sentences=2)
            bot.delete_message(chat_id=message.chat.id, message_id=message.id)
            bot.send_message(message.chat.id, result)
        except:
            bot.delete_message(chat_id=message.chat.id, message_id=message.id)
            bot.send_message(message.chat.id, 'К сожалению, я еще не имею никаких данных про него.')

    elif "а кто такой" in message.text:
        try:  
            user_request = message.text.split('а кто такой')[1]
            message = bot.send_message(message.chat.id, 'Секундочку . . .')
            wikipedia.set_lang("ru")
            result = wikipedia.summary(user_request, sentences=2)
            bot.delete_message(chat_id=message.chat.id, message_id=message.id)
            bot.send_message(message.chat.id, result)
        except:
            bot.delete_message(chat_id=message.chat.id, message_id=message.id)
            bot.send_message(message.chat.id, 'К сожалению, я еще не имею никаких данных про него.')

    


    
    #  А КТО ТАКАЯ  #

    elif "кто такая" in message.text:
        try:   
            user_request = message.text.split('кто такая')[1]
            message = bot.send_message(message.chat.id, 'Секундочку . . .')
            wikipedia.set_lang("ru")
            result = wikipedia.summary(user_request, sentences=2)
            bot.delete_message(chat_id=message.chat.id, message_id=message.id)
            bot.send_message(message.chat.id, result)
        except:
            bot.delete_message(chat_id=message.chat.id, message_id=message.id)
            bot.send_message(message.chat.id, 'К сожалению, я еще не имею никаких данных про него.')
        
    elif "а кто такая" in message.text:
        try:   
            user_request = message.text.split('а кто такая')[1]
            message = bot.send_message(message.chat.id, 'Секундочку . . .')
            wikipedia.set_lang("ru")
            result = wikipedia.summary(user_request, sentences=2)
            bot.delete_message(chat_id=message.chat.id, message_id=message.id)
            bot.send_message(message.chat.id, result)
        except:
            bot.delete_message(chat_id=message.chat.id, message_id=message.id)
            bot.send_message(message.chat.id, 'К сожалению, я еще не имею никаких данных про него.')





    #  ЧТО ТАКОЕ  #

    elif "что такое" in message.text:     
        try:           
            user_request = message.text.split('что такое')[1]
            message = bot.send_message(message.chat.id, 'Секундочку . . .')
            wikipedia.set_lang("ru")
            result = wikipedia.summary(user_request, sentences=2)
            bot.delete_message(chat_id=message.chat.id, message_id=message.id)
            bot.send_message(message.chat.id, result)
        except:
            bot.delete_message(chat_id=message.chat.id, message_id=message.id)
            bot.send_message(message.chat.id, 'К сожалению, я еще не имею никаких данных об этом.')

    elif "а что такое" in message.text:     
        try:           
            user_request = message.text.split('а что такое')[1]
            message = bot.send_message(message.chat.id, 'Секундочку . . .')
            wikipedia.set_lang("ru")
            result = wikipedia.summary(user_request, sentences=2)
            bot.delete_message(chat_id=message.chat.id, message_id=message.id)
            bot.send_message(message.chat.id, result)
        except:
            bot.delete_message(chat_id=message.chat.id, message_id=message.id)
            bot.send_message(message.chat.id, 'К сожалению, я еще не имею никаких данных об этом.')





    #  РАССКАЖИ ПРО  #

    elif "расскажи про" in message.text:
        try:
            user_request = message.text.split('расскажи про')[1]
            message = bot.send_message(message.chat.id, 'Секундочку . . .')
            wikipedia.set_lang("ru")
            result = wikipedia.summary(user_request, sentences=2)
            bot.delete_message(chat_id=message.chat.id, message_id=message.id)
            bot.send_message(message.chat.id, result)
        except:
            bot.delete_message(chat_id=message.chat.id, message_id=message.id)
            bot.send_message(message.chat.id, 'К сожалению, я еще не имею никаких данных об этом.')


    elif "а расскажи про" in message.text:
        try:  
            user_request = message.text.split('а расскажи про')[1]
            message = bot.send_message(message.chat.id, 'Секундочку . . .')
            wikipedia.set_lang("ru")
            result = wikipedia.summary(user_request, sentences=2)
            bot.delete_message(chat_id=message.chat.id, message_id=message.id)
            bot.send_message(message.chat.id, result)
        except:
            bot.delete_message(chat_id=message.chat.id, message_id=message.id)
            bot.send_message(message.chat.id, 'К сожалению, я еще не имею никаких данных об этом.')



    #  CAN YOU TELL ME ABOUT  #

    elif "can you tell me about" in message.text:
        try:
            user_request = message.text.split('can you tell me about')[1]
            message = bot.send_message(message.chat.id, 'Just a second . . .')
            result = wikipedia.summary(user_request, sentences=2)
            bot.delete_message(chat_id=message.chat.id, message_id=message.id)
            bot.send_message(message.chat.id, result)
        except:
            bot.delete_message(chat_id=message.chat.id, message_id=message.id)
            bot.send_message(message.chat.id, "Unfortunately, I don't have any data on this yet.")


    








    else:
        
        pass



if __name__=='__main__':

    while True:

        try:

            bot.polling(non_stop=True, interval=0)

        except Exception as e:

            print(e)
            sleep(5)
            continue