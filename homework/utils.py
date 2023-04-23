import json


def load_data(path):
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data


def filter_sort(data):
    data = [item for item in data if item.get('state') == 'EXECUTED']
    data = sorted(data , key=lambda item: item['data'], reverse=True)
    return data


def formatted_data(item):
    item_data = formatted_data(item.get("data"))

    if item.get("from"):
        from_ = mask_card(item.get("from")) + ' -> '
    else:
        from_ = ''

        to_ = mask_card(item.get("to"))

        return f'{item_data} {item.get("description")}\n' \
               f'{from_}{to_}\n' \
               f'{item["operationAmount"]["amount"]} {item["operationAmount"]["currency"]["name"]}\n'


def format_date(srt_date):
    list_date = srt_date[:10].split('-')
    return '.'.join(reversed(list_date))


def mask_card(card):
    card = card.split(' ')
    if card[0] == 'Счет':
        return f'{card[0]} **{card[-1][-4:]}'
    return f'{" ".join(card[:-1])}{card[-1][:4]} {card[-1][4:6]}** **** {card[-1][-4:]}'



