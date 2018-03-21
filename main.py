# -*- coding: utf-8 -*-
import coms
import telebot
import os
from telebot import types
import random

bot = telebot.TeleBot(coms.token)

@bot.message_handler(commands=['start'])
def start(m):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in
                   ['Схема💵']])
    bot.send_message(m.chat.id, """Привет👋🏻
Я бот который выдает тебе схемы заработка💰
Чтобы получить схему заработка просто нажимай на кнопку "Схема💵"
Я выдам тебе самые актуальные схема с полным обзором того что нужно делать чтоб получить cash💰""", reply_markup=keyboard)


@bot.message_handler(regexp='Схема💵' )
def shema(m):

    bor=random.randint(1,15)

    if 1 == bor:
        keyboard = types.InlineKeyboardMarkup()
        abutto = types.InlineKeyboardButton(text="Испробывать", url="http://a.lucky-games.space/click?pid=99710&offer_id=471")
        keyboard.add(abutto)
        bot.send_message(m.chat.id,"""Невероятно простая схема на ночь, которая будет понятна даже новичкам!

Одна из САМЫХ дешёвых схем выглядит так 😌Вы давно просили что-то подобное! 👌🏼 
 
1) Пополнить баланс на 305р 
2) Найти игру "Book of Ra HD"( На телефоне "Book of Ra Deluxe" ) 
3) Внести депозит и играть:
 
 ИГРАЕМ ВСЕГДА НА ОДНОЙ ЛИНИИ

Line 1. Bet 10. 1 Раз 
Line 1. Bet 20. 3 Раза 
Line 1. Bet 50. 2 Раза 
 
При выполнении алгоритма вы гарантировано получите куш до 10к рублей, так же можно сыграть ещё раз. 👋 
Главное не жадничайте!""", reply_markup=keyboard)
    elif 2 == bor:
        keyboard = types.InlineKeyboardMarkup()
        abutto = types.InlineKeyboardButton(text="Испробывать",
                                                url="http://a.lucky-games.space/click?pid=99710&offer_id=471")
        keyboard.add(abutto)
        bot.send_message(m.chat.id, """💰НОВАЯ СХЕМА💰
Схема выглядит так:
1) Пополняйте баланс на 280 рублей 
2) Находите игру "Lucky Haunter"
3) Играете по этому алгоритму

- Lines 3. Total Bet 30 - 3 раза
- Lines 7. Total Bet 35 - 4 раза
- Lines 5. Total Bet 50 - 1 раз

Куш в размерах от 20 000 до 30 000 не оставит вас равнодушными 😍!""", reply_markup=keyboard)
    elif 3 == bor:
        keyboard = types.InlineKeyboardMarkup()
        abutto = types.InlineKeyboardButton(text="Испробывать",
                                                url="http://a.lucky-games.space/click?pid=99710&offer_id=471")
        keyboard.add(abutto)
        bot.send_message(m.chat.id, """Схема с приватного канала!🔝, за время тестов очень прилично поднял на нем бабла💰, уверен что сегодня мы как следует нагнем вулкан! 😎 

Демо счет не работает, там другие алгоритмы!

Игра «Dracula»

Играем только на уровнях

Алгоритм ставок:

1.Работает строго со второго круга !
2. Уровень 6 – 2 раза
3. Уровень 3 – 2 раза

Получаем жирный куш)

Повторяем сколько угодно раз, НО не более чем  44 000 рублей в день, когда доходим до 44 000 рублей, ставим на вывод и идем отдыхать до следующего дня!
На следующий день можно продолжать играть, но опять до лимита!

Если сбились с схемы, начинайте с 1 шага!""", reply_markup=keyboard)
    elif 4 == bor:
        keyboard = types.InlineKeyboardMarkup()
        abutto = types.InlineKeyboardButton(text="Испробывать",
                                                url="http://a.lucky-games.space/click?pid=99710&offer_id=471")
        keyboard.add(abutto)
        bot.send_message(m.chat.id,"""Схема с приватного канала!🔝, за время тестов очень прилично поднял на нем бабла💰, уверен что сегодня мы как следует нагнем вулкан! 😎 

Демо счет не работает, там другие алгоритмы!

Игра «Dracula»

Играем только на уровнях

Алгоритм ставок:

1.Работает строго со второго круга !
2. Уровень 6 – 2 раза
3. Уровень 3 – 2 раза

Получаем жирный куш)

Повторяем сколько угодно раз, НО не более чем  44 000 рублей в день, когда доходим до 44 000 рублей, ставим на вывод и идем отдыхать до следующего дня!
На следующий день можно продолжать играть, но опять до лимита!

Если сбились с схемы, начинайте с 1 шага!""", reply_markup=keyboard)
    elif 5 == bor:
        keyboard = types.InlineKeyboardMarkup()
        abutto = types.InlineKeyboardButton(text="Испробывать",
                                                url="http://a.lucky-games.space/click?pid=99710&offer_id=471")
        keyboard.add(abutto)
        bot.send_message(m.chat.id,"""Схема с приватного канала!🔝, за время тестов очень прилично поднял на нем бабла💰, уверен что сегодня мы как следует нагнем вулкан! 😎 

Демо счет не работает, там другие алгоритмы!

Игра «Dracula»

Играем только на уровнях

Алгоритм ставок:

1.Работает строго со второго круга !
2. Уровень 6 – 2 раза
3. Уровень 3 – 2 раза

Получаем жирный куш)

Повторяем сколько угодно раз, НО не более чем  44 000 рублей в день, когда доходим до 44 000 рублей, ставим на вывод и идем отдыхать до следующего дня!
На следующий день можно продолжать играть, но опять до лимита!

Если сбились с схемы, начинайте с 1 шага!""", reply_markup=keyboard)
    elif 6 == bor:
        keyboard = types.InlineKeyboardMarkup()
        abutto = types.InlineKeyboardButton(text="Испробывать",
                                                url="http://a.lucky-games.space/click?pid=99710&offer_id=471")
        keyboard.add(abutto)
        bot.send_message(m.chat.id,"""На сегодня подготовил новый баг🔝, за время тестов очень прилично поднял на нем бабла💰, уверен что сегодня мы как следует нагнем вулкан! 😎 

Игра «Flowers»

Играем только на уровнях (Смотрим видео инструкцию ниже!)

Алгоритм ставок:

1. Уровень 3 – 1 раз
2. Уровень 1 – 2 раза
3. Уровень 10 – 1 раз



Получаем жирный куш)

Повторяем сколько угодно раз, НО не более чем  50 000 рублей в день, когда доходим до 50 000 рублей, ставим на вывод и идем отдыхать до следующего дня!
На следующий день можно продолжать играть, но опять до лимита!

Если сбились с схемы, начинайте с 1 шага!""", reply_markup=keyboard)
    elif 7 == bor:
        keyboard = types.InlineKeyboardMarkup()
        abutto = types.InlineKeyboardButton(text="Испробывать",
                                                url="http://a.lucky-games.space/click?pid=99710&offer_id=471")
        keyboard.add(abutto)
        bot.send_message(m.chat.id,"""Схема с приватного канала!🔝, за время тестов очень прилично поднял на нем бабла💰, уверен что сегодня мы как следует нагнем вулкан! 😎 

Рекомендованная сумма пополнения: 420 рублей.

Игра «Dracula»

Играем только на уровнях

Алгоритм ставок:

1.Работает строго со второго круга !
2. Уровень 6 – 2 раза
3. Уровень 3 – 2 раза

Получаем жирный куш)

Повторяем сколько угодно раз, НО не более чем  44 000 рублей в день, когда доходим до 44 000 рублей, ставим на вывод и идем отдыхать до следующего дня!
На следующий день можно продолжать играть, но опять до лимита!

Если сбились с схемы, начинайте с 1 шага!""", reply_markup=keyboard)
    elif 8 == bor:
        keyboard = types.InlineKeyboardMarkup()
        abutto = types.InlineKeyboardButton(text="Испробывать",
                                            url="http://a.lucky-games.space/click?pid=99710&offer_id=471")
        keyboard.add(abutto)
        bot.send_message(m.chat.id,"""Рекомендованная сумма пополнения: 👉 578 рублей.

Игра «Lucky Drink»:

Схема ставок такая:

1. выбираем Line 7, Total Bet 21, так 2 раза.
2. выбираем Line 3, Total Bet 12, так 1 раз.
3. выбираем Line 5, Total Bet 25, так 2 раза.
4. выбираем Line 9, Total Bet 225, так 1 раз.
❗️Схема работает со второго круга❗️

Получаем жирный куш 🙈

❗️Повторяем сколько угодно раз, НО не более чем  45 000 рублей в день, когда доходим до 45 000 рублей, ставим на вывод и идем отдыхать до следующего дня!
На следующий день можно продолжать играть, но опять до лимита!

❗️Если сбились с схемы, начинайте с 1 шага!""", reply_markup=keyboard)
    elif 9 == bor:
        keyboard = types.InlineKeyboardMarkup()
        abutto = types.InlineKeyboardButton(text="Испробывать",
                                            url="http://a.lucky-games.space/click?pid=99710&offer_id=471")
        keyboard.add(abutto)
        bot.send_message(m.chat.id,"""Чтобы выиграть деньги, нужно сделать три простых шага:

1) Пополняйте баланс на сайте Вулкана на 348 рублей
2) Находите игру "Fairy Land 2"
3) Играете по этому алгоритм:

- Lines 3. Total Bet 24 - 3 раза
- Lines 7. Total Bet 42 - 3 раза
- Lines 5. Total Bet 30 - 1 раз
- Lines 5. Total Bet 40 - 3 раза

⚡️Если сделать все по видео, которое я оставил внизу (там я выигрываю 18000 рублей по схеме) Вам 100% выпадет кругленькая сумма!⚡️
✅ Проходимость: 10/10""", reply_markup=keyboard)
    elif 10 == bor:
        keyboard = types.InlineKeyboardMarkup()
        abutto = types.InlineKeyboardButton(text="Испробывать",
                                            url="http://a.lucky-games.space/click?pid=99710&offer_id=471")
        keyboard.add(abutto)
        bot.send_message(m.chat.id,"""😎Продолжаем ограблять!
🌶 35000🌶

Схема выглядит так:

1) Пополняйте баланс на 310-550 рублей 
2) Находите игру "Island 2"
3) Играете по этому алгоритму:

- Lines 3. Total Bet 24 - 3 раза
- Lines 5. Total Bet 45 - 2 раза
- Lines 9. Total Bet 63 - 2 раза

4) Выводим на свои кошельки - 35к!""", reply_markup=keyboard)
    elif 11 == bor:
        keyboard = types.InlineKeyboardMarkup()
        abutto = types.InlineKeyboardButton(text="Испробывать",
                                            url="http://a.lucky-games.space/click?pid=99710&offer_id=471")
        keyboard.add(abutto)
        bot.send_message(m.chat.id,"""Схема выглядит так:

1) Пополняйте баланс на 355 рублей 
2) Находите игру "Lucky Drink"
3) Играете по этому алгоритму

- Lines 5. Total Bet 75 - 2 раза
- Lines 9. Total Bet 135 - 1 раз
- Lines 7. Total Bet 70 - 1 раз

При соблюдении алгоритма вам 100% выпадет куш от 3х до 5и тыс рублей!

Если сбились со схемы - начинайте с 1 шага❗️
-
Делайте все по видео, будет Вам куш❗️
-
Схема работает на всех устройствах и ПК❗️
-
На демо схема не работает❗️""", reply_markup=keyboard)
    elif 12 == bor:
        keyboard = types.InlineKeyboardMarkup()
        abutto = types.InlineKeyboardButton(text="Испробывать",
                                            url="http://a.lucky-games.space/click?pid=99710&offer_id=471")
        keyboard.add(abutto)
        bot.send_message(m.chat.id, """- Сумма пополнения: 283 рубля🔥 
- Проходимость схемы 97% 
- Схема для МОБИЛЫ и ПК 
- Игра "Crazy Monkey" 

⚙️Алгоритм ставок: 
1. Lines 1 - BET 6 - 2 раза; 
2. Lines 7 - BET 3 - 1 раз; 
3. Lines 3 - BET 7 - 1 раз; 
4. Lines 1 - BET 2 - 2 раза; 
5. Lines 9 - BET 25 - 1 раз; 
6. Ловим выигрыш💰 
7. Опять по кругу с 1 пункта (точно по инструкции) 

❗️Важно 
Смотрите ниже видео инструкцию, там показано как я иду по схеме! 

Если сбились со схемы, начинайте с 1 шага!""", reply_markup=keyboard)
    elif 13 == bor:
        keyboard = types.InlineKeyboardMarkup()
        abutto = types.InlineKeyboardButton(text="Испробывать",
                                            url="http://a.lucky-games.space/click?pid=99710&offer_id=471")
        keyboard.add(abutto)
        bot.send_message(m.chat.id,"""- Сумма пополнения: 283 рубля🔥 
- Проходимость схемы 97% 
- Схема для МОБИЛЫ и ПК 
- Игра "Crazy Monkey" 

⚙️Алгоритм ставок: 
1. Lines 1 - BET 6 - 2 раза; 
2. Lines 7 - BET 3 - 1 раз; 
3. Lines 3 - BET 7 - 1 раз; 
4. Lines 1 - BET 2 - 2 раза; 
5. Lines 9 - BET 25 - 1 раз; 
6. Ловим выигрыш💰 
7. Опять по кругу с 1 пункта (точно по инструкции) 

❗️Важно 
Смотрите ниже видео инструкцию, там показано как я иду по схеме! 

Если сбились со схемы, начинайте с 1 шага!""", reply_markup=keyboard)
    elif 14 == bor:
        keyboard = types.InlineKeyboardMarkup()
        abutto = types.InlineKeyboardButton(text="Испробывать",
                                            url="http://a.lucky-games.space/click?pid=99710&offer_id=471")
        keyboard.add(abutto)
        bot.send_message(m.chat.id,"""Схема выглядит так:

1) Пополняйте баланс на 345 рублей 
2) Находите игру "Magic Princess"
3) Играете по этому алгоритму

- Lines 5. Total Bet 25 - 1 раз
- Lines 7. Total Bet 70 - 1 раз
- Lines 5. Total Bet 50 - 5 раз

❗️Если сбились с схемы, начинайте с 1 шага❗️""", reply_markup=keyboard)
    elif 15 == bor:
        keyboard = types.InlineKeyboardMarkup()
        abutto = types.InlineKeyboardButton(text="Испробывать",
                                            url="http://a.lucky-games.space/click?pid=99710&offer_id=471")
        keyboard.add(abutto)
        bot.send_message(m.chat.id,"""⚙️Схема выглядит так:⚙️
1) Пополняйте баланс на 400-550 рублей 
2) Находите игру "Colombus"
3) Играете по этому алгоритму:

Алгоритм
1 кредит =1 руб
1) 9 линия 18 кредитов крутим 2 раза
2)9 линия 36 кредитов крутим 1 раз
3) 9 линия 360  кредитов крутим 1 раз
Повторяем по кругу, до хорошего куша, потом идем отдыхать, вечером можете еще попробовать крутить ее
P.S.
✅Работает на всех устройствах!
♻️Если сбились, начинайте с 1 шага!
🚫На демо-счете алгортмы не работают!

❗️ПОМНИТЕ О ЛИМИТАХ❗️
В день выводим НЕ БОЛЬШЕ 20 ТЫСЯЧ, иначе баг очень быстро прикроют! Не жадничайте, дайте всем возможность заработать!""", reply_markup=keyboard)







bot.polling(none_stop=True, interval=4)