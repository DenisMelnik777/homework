import utils


def test_load_data():
    list_ = [
 {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  }
  ]
    assert utils.load_data('test.json') == list_


def test_filer_sort():
    list_ = [
        {
            'id': 1,
            'state': 'EXECUTED',
            'date': '2018-11-29T07:18:23.941293'
        },
        {'id': 2,
            'state': 'OPEN',
            'date': '2018-11-29T07:18:23.941293'
        },
        {'id': 3,
            'state': 'EXECUTED',
            'date': '2019-06-14T19:37:49.044089'
        }

    ]
    sorted_list = [
        {'id': 3,
         'state': 'EXECUTED',
         'date': '2019-06-14T19:37:49.044089'
         },

        {
            'id': 1,
            'state': 'EXECUTED',
            'date': '2018-11-29T07:18:23.941293'
        }

    ]
    assert utils.filter_sort(list_) == sorted_list


def test_format_date():
    assert utils.format_date('2019-03-23T01:09:46.296404') == '23.03.2019'
    assert utils.format_date('2018-12-20T16:43:26.929246') == '20.12.2018'


def test_mask_card():
    assert utils.mask_card("Maestro 3928549031574026") == 'Maestro 3928 54** **** 4026'
    assert utils.mask_card("Счет 27248529432547658655") == 'Счет **8655'
    assert utils.mask_card("Visa Platinum 2256483756542539") == 'Visa Platinum 2256 48** **** 2539'


def test_formatted_data():
    dict_ = {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  }
    str_ = '26.08.2019 Перевод организации\n' \
           'Maestro 1596 83** **** 5199 -> Счет **9589\n' \
           '31957.58 руб\n'
    assert utils.format_date(dict_) == str_


