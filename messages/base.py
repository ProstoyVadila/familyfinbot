START_MESSAGE = 'Привет! Я финансовый бот для учета личных' \
                ' или совместных финансов.\nТы можешь устанавливать' \
                ' бюджет, записывать расходы и получать актуальную' \
                ' статистику за день, неделю или месяц. А также' \
                ' выгружать ее в форматах excel таблицы или csv\n\n' \
                'Для совместного учета финансов просто добавь меня' \
                ' в чат со всеми участниками\n\nНу что, начнем?'

MENU_MESSAGE = 'Вот список операций на данный момент. \n\n' \
               'Постепенно я буду обрастать новыми возможностями,' \
               ' и буду рад вашим отзывам. Их можно отправить' \
               ' по этой команде /feedback'


# help messages
HELP_MESSAGE = 'Моей главной особенностью является совместное ведение ' \
               'учета. Иными словами каждый участник чата может вносить ' \
               'расходы или доходы, устанавливать бюджет на день,' \
               ' неделю или месяц, а также запрашивать статистику.' \
               '\nНапример: сколько возможно еще потратить, чтобы' \
               ' не выйти из бюджета (разница между бюджетом, в' \
               ' пересчете на день, к расходам за этот день,' \
               ' на что я потратился за эту неделю (вывод всех ' \
               'категорий расходов за неделю) и тд.' \
               '\n\nВсе данные хранятся в зашифрованом виде' \
               ' и абсолютно анонимно, <b><i>{user_name}</i></b>.' \
               '\n\n'

HELP_MESSAGE_COMMANDS = (
        'Команды также доступные из меню: ',
        '<b>/menu   —  Основные функции бота</b>',
        '<b>/budget —  Установить бюджет</b>',
        '<b>/income — Внести доход</b>',
        '<b>/expense — Внести расход</b>',
        '<b>/stats — Получить статистку</b>',
        '<b>/download — Выгрузить свои данные</b>',
        '',
        'Остальные команды:',
        '/help   —  Получить подсказку ',
        '/feedback — Написать админу',
        '/start  —  Начать общение с ботом',
)


# Budget messages
BUDGET_MESSAGE_START = 'Установите сколько собираетесь' \
                       ' тратить за день, неделю или месяц. ' \
                       'Выберите удобный для вас вариант ' \
                       'из представленных на месте вашей' \
                       ' клавиатуры.\n\n ' \
                       'Бюджет всегда можно потом обновить.'

BUDGET_MESSAGE_END = 'А теперь <i>дело за малым</i>  — отправьте ' \
                     'сумму бюджета. Желательно просто числом' \
                     ', а то могу не понять :)'

YOUR_BUDGET_MESSAGE = 'Вы установили себе бюджет в {value} {period}.'


# Set expanse messages
EXPANSE_MESSAGE_START = 'Вводите свой расход. ' \
                        'Желательно числом, а то могу не понять :)'

EXPANSE_MESSAGE_END = 'Предлагаю также добавить категорию' \
                      ' к расходу. Потом будет удобно ' \
                      'анализировать, на что вы тратите' \
                      ' и стоит ли это того. Просто ' \
                      'запишите ее или выберите одну ' \
                      'из существующих категорий.'

YOUR_TRANSACTION_MESSAGE = 'Вы внесли:\nСумма: {value}' \
                           '\nКатегория: {category}'


# income messages
INCOME_MESSAGE_START = 'Введите свой доход. ' \
                       'Желательно числом, а то могу не понять :)'

INCOME_MESSAGE_END = 'Предлагаю также добавить категорию дохода' \
                     '. Просто запишите категорию числом или ' \
                     'выберите из существующих. '
