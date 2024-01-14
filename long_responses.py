import random

def unknown():
    
    response = ["Я вас не поняла, можете перефразировать ваше сообщение ?",
                "А ?",
                "Я не поняла вас",
                "Извините, но я еще не знаю таких слов"][random.randrange(4)]
    
    return response