# -*- coding: utf-8 -*-

import random
from plugin_system import Plugin
from settings import ADMINS
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
async def tell_truth(msg, args):
    await msg.answer("🎱" + random.choice(answers))


@plugin.on_command('админ')
async def im_admin(msg, args):
    uid = msg.id
    if uid not in ADMINS:
        return await msg.answer("Нет, ты не админ!")
    await msg.answer('Слушаю и повинуюсь!')
