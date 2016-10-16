import random
from plugin_system import Plugin

# Инициализируем возможные ответы
greetings = ['Слава Украине!', '🌚 Кекеке', 'Запущен и готов служить!', 'У контакта ужасный флуд-контроль, %username%',
             'Хуяк-хуяк и в продакшн']

plugin = Plugin('Приветствие')


@plugin.on_command('привет', 'приветствие', 'голос', 'ку', 'как дела?')
async def call(vk, msg, args):
    await vk.respond(msg, {'message': random.choice(greetings)})
