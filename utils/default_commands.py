from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("menu", "Меню"),
        types.BotCommand("balance", "Узнать баланс"),
        types.BotCommand("expense", "Внести расход"),
        types.BotCommand("income", "Внести доход"),
        types.BotCommand("stats", "Получить аналитику"),
        types.BotCommand("budget", "Установить бюджет"),
        types.BotCommand("download", "Выгрузить свои операции"),
        types.BotCommand("feedback", "Оставить фидбек"),
        types.BotCommand("help", "Помощь"),
        types.BotCommand('donate', 'На развитие бота')
    ])
