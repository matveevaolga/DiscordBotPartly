from random import randint
import datetime as DT

def load_phrases(type='social', game='', action='not_exist') -> str:
    '''Подгрузка фраз для общения

    type: games, social
    game: duel
    '''

    path = f'./data/phrases/{type}/'

    match (type):
        case 'games':
            match (game):
                case 'duel':
                    match (action):
                        case 'bot':
                            f = open(f'{path}{game}/{action}.txt',
                                     encoding='UTF-8')
                        case 'self':
                            f = open(f'{path}{game}/{action}.txt',
                                     encoding='UTF-8')
                        case 'none':
                            f = open(f'{path}{game}/{action}.txt',
                                     encoding='UTF-8')
                        case 'money_self':
                            f = open(f'{path}{game}/{action}.txt',
                                     encoding='UTF-8')
                        case 'money_enemy':
                            f = open(f'{path}{game}/{action}.txt',
                                     encoding='UTF-8')
        case 'social':
            match (action):
                case 'not_exist':
                    f = open(f'{path}/{action}.txt', encoding='UTF-8')
                case 'transfer_money_hero':
                    f = open(f'{path}/{action}.txt', encoding='UTF-8')
                case 'transfer_money_self':
                    f = open(f'{path}/{action}.txt', encoding='UTF-8')

    strings_actions = f.readlines()
    num_string = randint(0, len(strings_actions) - 1)
    f.close()

    return strings_actions[num_string]

def to_two_digits(num: float) -> float:
    '''Преобразовываем к 2ум знакам после запятой'''

    return int(num * 100) / 100

def date_to_days(user_date: str) -> int:
    '''Количество дней от даты до текущего дня'''

    # datetime.date
    date = str(user_date).split('-')
    date = DT.date(int(date[0]), int(date[1]), int(date[2]))
    days = abs(int((date - DT.date.today()).days))

    return days

def delete_reverse_slash(s: str) -> str:
    if s.find('\\') == -1:
        return s
    return s[:s.find('\\'):] + s[s.find('\\') + 1::]