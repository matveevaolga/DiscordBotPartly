import disnake
from src.functions.describe import lucky_number_describe


def embed_by_phrase(phrase: str) -> disnake.Embed:
    embed = disnake.Embed(description=phrase)

    return embed

def embed_stats_duel(user_name: str, value: dict[str, int]) -> disnake.Embed:
    all_games, win_games = value['all_games'], value['win_games']
    wr = value['wr']
    
    title = f'Статы {user_name} в игре Дуэль'
    descr = f'Всего игр: {all_games}\n'
    descr += f'Побед: {win_games}\n'
    descr += f'Процент побед: {wr}'
    color = 0x187CFC

    embed = disnake.Embed(title=title, description=descr, color=color)

    return embed


def embed_stats_lucky(user_name: str, value: dict[str, int]) -> disnake.Embed:
    all_games, win_games = value['all_games'], value['win_games']
    wr = value['wr']

    title = f'Статы {user_name} в игре Угадай число'
    descr = f'Всего игр: {all_games}\n'
    descr += f'Побед: {win_games}\n'
    descr += f'Процент побед: {wr}'
    color = 0x187CFC

    embed = disnake.Embed(title=title, description=descr, color=color)

    return embed

def embed_user_info(user_name: str, value: dict[str, int]) -> disnake.Embed:
    title = f''
    descr = f''
    color = 0x187CFC

    embed = disnake.Embed(title=title, description=descr, color=color)

    return embed

def embed_rules_lucky_game(timeout: int) -> disnake.Embed:
    d_rules = lucky_number_describe(timeout)
    color = 0x187CFC

    embed = disnake.Embed(title=d_rules['title'],
                          description=d_rules['description'], color=color)

    return embed

def embed_games_panel(d_embed: dict[str, str]) -> disnake.Embed:
    color = 0x0073ff
    embed = disnake.Embed(
        title=d_embed['title'], description=d_embed['description'],
        color=color)

    return embed

def embed_user_panel(d_embed: dict[str, str]) -> disnake.Embed:
    color = 0x0e5c00
    embed = disnake.Embed(
        title=d_embed['title'], description=d_embed['description'],
        color=color)

    return embed

def embed_wrong_channel(channel, type: str) -> disnake.Embed:
    '''Создание embed для выбора подходящего канала.
    Когда пользователь выбрал не тот канал.'''

    match (type):
        case 'question':
            description = f'Вопросы от меня ты можешь получить на канале {channel.mention}'
        case 'ege':
            description = f'Задачи от меня ты можешь получить на канале {channel.mention}' + '\n'
            description += 'просто напиши там эту же комманду ;)'
        case 'duel':
            description = f'Сразиться в дуэли ты можешь на канале {channel.mention}'
        case 'lucky_number':
            description = f'Сыграть в эту игру ты можешь на канале {channel.mention}'

    color = 0x5c2e01
    embed = disnake.Embed(description=description, color=color)

    return embed
