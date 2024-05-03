import requests


def test_get_all_areas(url: str):
    res = requests.get(url).json()
    assert (res == [{
        'areas_id': 1,
        'name': 'Binance',
        'description': 'Одна из крупнейших криптовалютных бирж в мире.',
        'count_users': 'Cryptocurrency Exchange',
        'year': '2017'
    },
        {
            'areas_id': 2,
            'name': 'Coinbase',
            'description': 'Одна из наиболее популярных и надежных платформ для обмена криптовалют.',
            'count_users': 'Cryptocurrency Exchange',
            'year': '2012'
        },
        {
            'areas_id': 3,
            'name': 'Kraken',
            'description': 'Один из старейших криптовалютных бирж с широким спектром услуг и высоким уровнем безопасности.',
            'count_users': 'Cryptocurrency Exchange',
            'year': '2011'
        },
        {
            'areas_id': 4,
            'name': 'Bittrex',
            'description': 'Платформа для торговли криптовалютами с широким выбором монет и высокой ликвидностью.',
            'count_users': 'Cryptocurrency Exchange',
            'year': '2014'
        },
        {
            'areas_id': 5,
            'name': 'Huobi',
            'description': 'Мировая криптовалютная биржа с широким спектром услуг и активным сообществом трейдеров.',
            'count_users': 'Cryptocurrency Exchange',
            'year': '2013'
        }])


def test_get_area_by_id(url: str):
    res = requests.get(url).json()
    assert (res == {
        'areas_id': 1,
        'name': 'Binance',
        'description': 'Одна из крупнейших криптовалютных бирж в мире.',
        'count_users': 'Cryptocurrency Exchange',
        'year': '2017'
    })


if __name__ == '__main__':
    URL = 'http://127.0.0.1:80/api/v1/areas/'
    test_get_area_by_id(URL + '1')
    test_get_all_areas(URL)
