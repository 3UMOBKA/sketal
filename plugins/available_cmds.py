from plugin_system import Plugin
from settings import PREFIXES

import asyncio

plugin = Plugin('Помощь',
                usage='команды - узнать список доступных команд')


@plugin.on_command('команды', 'помоги', 'помощь')
async def call(msg, args):
    usages = "🔘Доступные команды:🔘\n"

    for plugin in msg.vk.get_plugins():
        if not plugin.usage:
            continue

        temp = "🔷" + plugin.name + ":🔷" + "\n"

        for usage in plugin.usage:
            temp += "🔶" + PREFIXES[0] + usage + "\n"

        temp += "\n"

        if len(usages) + len(temp) >= 550:
            await msg.answer(usages)
            await asyncio.sleep(0.34)
            usages = ""

        usages += temp

    await msg.answer(usages)
