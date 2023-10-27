from src.modules.config import top_permissions
from src.data.data_base import DB

def find_channel_by_name(bot: object, source_channel: str):
    '''Поиск канала по названию канала'''

    for guild in bot.guilds:
        for channel in guild.channels:
            if channel.name == source_channel:
                return channel
    return False

def find_user_by_name_discord(bot: object, user_name: str):
    '''Поиск пользователя по имени в дискорд-сервере'''
    
    for guild in bot.guilds:
        for member in guild.members:
            if member.name == user_name:
                return member
    return False

def find_role_by_name(bot: object, role_name: str):
    '''Поиск роли по названию в дискорд-сервере'''

    for guild in bot.guilds:
        for role in guild.roles:
            if role.name == role_name:
                return role
    return False

def find_user_by_id(bot: object, user_id: int):
    '''Поиск пользователя по ID в дискорд-сервере'''

    for guild in bot.guilds:
        for member in guild.members:
            if member.id == user_id:
                return member
    return False

def find_user(user_name: str) -> bool:
    '''Поиск пользователя по имени в БД'''

    db = DB()

    if db.select_user(user_name) is None:
        return False
    return True

def get_user_money(user_name: str) -> int | None:
    '''Получаем количество монет пользователя'''

    db = DB()
    user_id = db.select_user(user_name)

    if user_id is not None:
        return db.get_user_money(user_id)
    return None

def update_duel_stats(user_win: str, user_lose: str):
    '''Обновление статистики после дуэли'''

    db = DB()

    db.update_duel_stats(user_win, 1)
    db.update_duel_stats(user_lose, -1)

def add_user_money(user_name: str, money: int):
    '''Добавляем/вычитаем у пользователя монеты'''

    db = DB()
    user_id = db.select_user(user_name)

    if user_id is not None:
        db.add_user_money(user_id, money)

def get_user_rate(user_name: str) -> int | None:
    '''Получаем рейтинг пользователя'''

    db = DB()
    user_id = db.select_user(user_name)

    if user_id is not None:
        return db.get_user_rate(user_id)
    return None

def check_permissions(author) -> bool:
    for role in author.roles:
        if role.name in top_permissions:
            return True
    return False

def update_lucky_stats(user_name: str, result: int):
    db = DB()
    user_id = db.select_user(user_name)

    if user_id is not None:
        return db.update_table_lucky_number(user_name, result)
    return None

def get_all_games_lucky(user_name: str):
    db = DB()
    user_id = db.select_user(user_name)

    if user_id is not None:
        return db.get_all_games_lucky(user_id)
    return None

def get_win_games_lucky(user_name: str):
    db = DB()
    user_id = db.select_user(user_name)

    if user_id is not None:
        return db.get_win_games_lucky(user_id)
    return None

def get_all_games_duel(user_name: str):
    db = DB()
    user_id = db.select_user(user_name)

    if user_id is not None:
        return db.get_duel_all_games(user_id)
    return None

def get_win_games_duel(user_name: str):
    db = DB()
    user_id = db.select_user(user_name)

    if user_id is not None:
        return db.get_duel_win_games(user_id)
    return None

def form_lucky_stats_dict(user_name: str):
    info_dict = {
        'all_games': get_all_games_lucky(user_name),
        'win_games': get_win_games_lucky(user_name),
    }
    info_dict['wr'] = "%.2f" % (info_dict['win_games'] / info_dict['all_games'] * 100)
    return info_dict

def form_duel_stats_dict(user_name: str):
    info_dict = {
        'all_games': get_all_games_duel(user_name),
        'win_games': get_win_games_duel(user_name),
    }
    info_dict['wr'] = "%.2f" % (info_dict['win_games'] / info_dict['all_games'] * 100)
    return info_dict
