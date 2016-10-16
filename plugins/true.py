# -*- coding: utf-8 -*-

import random
from plugin_system import Plugin

plugin = Plugin('Правда')

# Инициализируем возможные ответы
answers = '''Абсолютно точно!
Да.
Нет.
Скорее да, чем нет.
Не уверен...
Однозначно нет!
Если ты не фанат аниме, у тебя все получится!
Можешь быть уверен в этом.
Перспективы не очень хорошие.
А как же иначе?.
Да, но если только ты не смотришь аниме.
Знаки говорят — «да».
Не знаю.
Мой ответ — «нет».
Весьма сомнительно.
Не могу дать точный ответ.
'''.splitlines()

@plugin.on_command('правда', 'предсказание', 'реши', 'шар')
async def call(vk, msg, args):
    await vk.respond(msg, {'message': "🎱" + random.choice(answers)})


@plugin.on_command('админ')
async def call(vk, msg, args):
    uid = msg.get('user_id')
    if not uid:
        return await vk.respond(msg, {'message': "Нет, ты не админ! Админ - vk.com/id170831732!"})
    await vk.respond(msg, {'message': 'Слушаю и повинуюсь!'})
