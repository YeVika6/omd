import json  # https://python-scripts.com/json
from keyword import iskeyword

test_1_json = '''{
    "title": "iPhone X",
    "price": 100
}'''

test_2_json = '''{
    "title":"iPhone X",
    "price": 100,
    "location": {
        "address":"город Самара, улица Мориса Тореза, 50",
        "metro_stations": ["Спортивная","Гагаринская"]
    }
}'''

test_3_json = '''{
    "title": "Вельш-корги",
    "price": 1000,
    "class": "dogs",
    "location": {
        "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
    }
}'''

test_4_json = '''{
    "title": "iPhone X",
    "price": -100
}'''

test_5_json = '''{
    "title": "iPhone X"
}'''


class DictToAttr:
    def __init__(self, mapping: dict):  # Он уже видит, что test - это словарик https://translated.turbopages.org/proxy_u/en-ru.ru.1b466611-6356dd06-b59a91c2-74722d776562/https/www.geeksforgeeks.org/convert-json-to-dictionary-in-python/
        for key, value in mapping.items():
            if iskeyword(key):  # iskeyword производит проверку указанного слова на предмет его наличия в перечне ключевых слов языка
                key = str(key) + '_'
            if isinstance(value, dict):  # isinstance(value, dict) - проверяет, что value является экземпляром класса или кортежем классов (на случай вложенности)
                self.__dict__[key] = DictToAttr(value)
            else:
                self.__dict__[key] = value  # добавляем атрибут в словарь атрибутов


class ColorizeMixin:
    def __repr__(self) -> str:
        text = super().__repr__()  # идем в BaseAdvert за __repr__()
        return f'\033[{self.repr_color_code}m{text}\033[0m'  # https://ozzmaker.com/add-colour-to-text-in-python/


class BaseAdvert(DictToAttr):
    def __init__(self, mapping: dict):
        super().__init__(mapping)

        if 'price' not in self.__dict__:
            self.__dict__['price'] = 0
        elif self.price < 0:
            raise ValueError('must be >= 0')  # создали исключение https://stackoverflow.com/questions/2052390/manually-raising-throwing-an-exception-in-python

    def __repr__(self) -> str:
        return f'{self.title} | {self.price}₽'


class Advert(ColorizeMixin, BaseAdvert):
    repr_color_code = 33  # 36 - blue, 33 - yellow


def main():
    test_1 = json.loads(test_1_json)  # loads читает json и возвращает dict
    test_2 = json.loads(test_2_json)
    test_3 = json.loads(test_3_json)
    test_4 = json.loads(test_4_json)
    test_5 = json.loads(test_5_json)
    ad_1 = Advert(test_1)  # инициализируем объект класса
    print(ad_1)
    print('title =', ad_1.title)
    print('price =', ad_1.price)
    ad_2 = Advert(test_2)
    print(ad_2)
    print('title =', ad_2.title)
    print('price =', ad_2.price)
    print('location =', ad_2.location)
    print('address =', ad_2.location.address)
    print('metro_stations =', ad_2.location.metro_stations)
    ad_3 = Advert(test_3)
    print('title =', ad_3.title)
    print('price =', ad_3.price)
    print('class =', ad_3.class_)
    print('location =', ad_3.location)
    print('address =', ad_3.location.address)
    ad_4 = Advert(test_4)    # Для теста ValueError: price < 0
    print(ad_4)
    print('title =', ad_4.title)
    print('price =', ad_4.price)
    ad_5 = Advert(test_5)
    print(ad_5)
    print('title =', ad_5.title)
    print('price =', ad_5.price)


if __name__ == '__main__':
    main()