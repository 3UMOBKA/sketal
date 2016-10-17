import random
from plugin_system import Plugin

answers = ['🌚', '🌚🌚']

plugin = Plugin('Луна')


@plugin.on_command('луна', '🌚')
async def get_moon(msg, args):
    await msg.answer(random.choice(answers))
