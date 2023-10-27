import src.data.data_base as db


def create_user(user):
    '''Создание пользователя в БД'''
    
    data_base = db.DB()
    users, stats, duel, lucky = divide_values(user)
    new_id = data_base.get_last_user_id() + 1

    print(users, new_id)

    data_base.insert_stats([new_id] + stats, new_id)
    data_base.insert_users(users, new_id)
    data_base.insert_duel([new_id] + duel, new_id)
    data_base.insert_table_lucky_number([new_id] + lucky)


def divide_values(values: list) -> tuple:
    '''Разделение значений для записи в БД'''

    users = [values.name, values.money, values.live_server]
    stats = [values.count_messages, values.count_req_help,
             values.count_done_help, values.count_projects,
             values.bonus_rate, values.rate]
    duels = [values.duel_all_games, values.duel_win_games]
    lucky = [0, 0]

    return (users, stats, duels, lucky)