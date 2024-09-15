#Импортируемые библиотеки и млодули
import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor, VkKeyboardButton
from vk_api.longpoll import VkLongPoll, VkEventType

#Токен, сесии и longpoll
vk_session = vk_api.VkApi(token="vk1.a.jVe9ajsUIoiGaEB3fpad8t-wKDwT2VkHgrZsIiGTLgrp8zoRMpsqY0x4z1zXkKQm7Tzil-6saWltOq3Hidy_C70CgXoUtKCFVFiOo0oC-Nzr9_CMO1_IjJpiqktGBTLYINM4ZXL6Cxtl4chiKhzyS5cqTwXEqHzDFRTh9CGAxe6tq_OOGfK6AvbIePdgk9X4V2ccN9iSWSkQqFfVTUysww")
session_api = vk_session.get_api()
longpool = VkLongPoll(vk_session)



#Методы использующиеся в работе бота
def send_some_msg(id, some_text, keyboard=None):
    post = {
        "user_id":id,
        "message":some_text,
        "random_id":0,
    }
    #вывод клавы 
    if keyboard != None:
        post["keyboard"] = keyboard.get_keyboard()
    else:
        post = post
    
    
    vk_session.method("messages.send", post)

# Слушаем longpoll и отправляем/обробатываем сообщения
for event in longpool.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            msg = event.text.lower()
            id = event.user_id
            #меню
            if msg == "начать":
                keyboard = VkKeyboard(one_time=True)
                keyboard.add_button("1", VkKeyboardColor.PRIMARY )
                keyboard.add_button("2", VkKeyboardColor.SECONDARY)
                keyboard.add_button("3", VkKeyboardColor.NEGATIVE )
                keyboard.add_button("4", VkKeyboardColor.POSITIVE )
                send_some_msg(id, "Здарово, я Олег и я хочу продать тебе свои ЭКСТРАОРДИНАРНЫЕ услуги. Я предлагаю барохло номер 1, номер 2, номер 3, номер 4", keyboard)
            if msg == "назад в меню":
                keyboard = VkKeyboard(one_time=True)
                keyboard.add_button("1", VkKeyboardColor.PRIMARY )
                keyboard.add_button("2", VkKeyboardColor.SECONDARY)
                keyboard.add_button("3", VkKeyboardColor.NEGATIVE )
                keyboard.add_button("4", VkKeyboardColor.POSITIVE )
                send_some_msg(id, "Здарово, я Олег и я хочу продать тебе свои ЭКСТРАОРДИНАРНЫЕ услуги. Я предлагаю барохло номер 1, номер 2, номер 3, номер 4", keyboard)
            #Католог о товаре 1
            if msg == "1":
                keyboard = VkKeyboard(one_time=True)
                keyboard.add_button("купить товар №1", VkKeyboardColor.PRIMARY )
                keyboard.add_button("подробнее о товаре 1", VkKeyboardColor.SECONDARY)
                keyboard.add_button("назад в меню", VkKeyboardColor.NEGATIVE )
                send_some_msg(id, "Очень рад что тебя заинтересовала, я предлпгпю тебе то сё и пятое десятое всего 100 рублей!", keyboard)
                
            if msg == "подробнее о товаре 1":
                keyboard = VkKeyboard(one_time=True)                
                keyboard.add_button("купить товар №1", VkKeyboardColor.PRIMARY )
                keyboard.add_button("назад в меню", VkKeyboardColor.NEGATIVE )
                send_some_msg(id, "Это лучшее предложение в МИРЕ!", keyboard)
            
            if msg == "купить товар №1":
                keyboard = VkKeyboard(one_time=True)                
                keyboard.add_button("назад в меню", VkKeyboardColor.NEGATIVE )
                send_some_msg(id, "Цена товара 1 состовляет 100 руб, для покупке пишете ВСТАВТЕ_ИМЯ", keyboard)
            
            #Каталог товара 2 
            if msg == "2":
                keyboard = VkKeyboard(one_time=True)
                keyboard.add_button("купить товар №2", VkKeyboardColor.PRIMARY )
                keyboard.add_button("подробнее о товаре 2", VkKeyboardColor.SECONDARY)
                keyboard.add_button("назад в меню", VkKeyboardColor.NEGATIVE )
                send_some_msg(id, "Очень рад что тебя заинтересовала, я предлпгпю тебе то сё и пятое десятое всего 1000 рублей!", keyboard)

            if msg == "подробнее о товаре 2":
                keyboard = VkKeyboard(one_time=True)                
                keyboard.add_button("купить товар №1", VkKeyboardColor.PRIMARY )
                keyboard.add_button("назад в меню", VkKeyboardColor.NEGATIVE )
                send_some_msg(id, "Это уникеальный продукт, который ты не найдёшь на вайлдбериз или озон!", keyboard)
            
            if msg == "купить товар №2":
                keyboard = VkKeyboard(one_time=True)                
                keyboard.add_button("назад в меню", VkKeyboardColor.NEGATIVE )
                send_some_msg(id, "Цена товара 2 состовляет 1000 руб, для покупке пишете ВСТАВТЕ_ИМЯ", keyboard)
                
            # Каталог товара 3    
            if msg == "3":
                keyboard = VkKeyboard(one_time=True)
                keyboard.add_button("купить товар №3", VkKeyboardColor.PRIMARY )
                keyboard.add_button("подробнее о товаре 3", VkKeyboardColor.SECONDARY)
                keyboard.add_button("назад в меню", VkKeyboardColor.NEGATIVE )
                send_some_msg(id, "Очень рад что тебя заинтересовала, я предлпгпю тебе то сё и пятое десятое всего 100000 рублей!", keyboard)
                
            if msg == "подробнее о товаре 3":
                keyboard = VkKeyboard(one_time=True)                
                keyboard.add_button("купить товар №3", VkKeyboardColor.PRIMARY )
                keyboard.add_button("назад в меню", VkKeyboardColor.NEGATIVE )
                send_some_msg(id, "Сделано из золота 99 пробы!", keyboard)
            
            if msg == "купить товар №3":
                keyboard = VkKeyboard(one_time=True)                
                keyboard.add_button("назад в меню", VkKeyboardColor.NEGATIVE )
                send_some_msg(id, "Цена товара 3 состовляет 100000 руб, для покупке пишете ВСТАВТЕ_ИМЯ", keyboard)
                
            #Каталог 4    
            if msg == "4":
                keyboard = VkKeyboard(one_time=True)
                keyboard.add_button("купить товар №4", VkKeyboardColor.PRIMARY )
                keyboard.add_button("подробнее о товаре 4", VkKeyboardColor.SECONDARY)
                keyboard.add_button("назад в меню", VkKeyboardColor.NEGATIVE )
                
                send_some_msg(id, "Очень рад что тебя заинтересовала, я предлпгпю тебе то сё и пятое десятое всего 10000000000 рублей!", keyboard)
            
            if msg == "подробнее о товаре 4":
                keyboard = VkKeyboard(one_time=True)                
                keyboard.add_button("купить товар №4", VkKeyboardColor.PRIMARY )
                keyboard.add_button("назад в меню", VkKeyboardColor.NEGATIVE )
                send_some_msg(id, "Эта хенлогия украдина с самой Лубянки!!!!", keyboard)
            
            if msg == "купить товар №4":
                keyboard = VkKeyboard(one_time=True)                
                keyboard.add_button("назад в меню", VkKeyboardColor.NEGATIVE )
                send_some_msg(id, "Цена товара 4 состовляет 10000000000 руб, для покупке пишете ВСТАВТЕ_ИМЯ", keyboard)
                
                
