"""
Карина Володина. Code review.
Я изучил работу: https://github.com/sacred70/lesson_21
Я обнаружил следующие моменты:
1)
строки где замечено:
https://github.com/sacred70/lesson_21/blob/master/main.py#L8
https://github.com/sacred70/lesson_21/blob/master/main.py#L19

тип запаха или проблема:
сложно читать код, при создании экземпляров классов
как бы я решила/переписала:
"""
shop = Shop()
store = Store()

shop.add('печеньки', 5)
shop.add('собачки', 2)

store.add('печеньки', 6)
store.add('собачки', 4)
store.add('коробки', 5)
store.add('носки', 3)
store.add('шапки', 5)
store.add('хлеб', 10)

places = {
    'магазин': shop,
    'магазина': shop,
    'склад': store,
    'склада': store,
}

"""
2)
строка где замечено: 
https://github.com/sacred70/lesson_21/blob/master/classes/class_Request.py#L9
тип запаха или проблема: 
можно более структорированно создать класс
как бы я решила/переписала:
"""
class Request:
    def __init__(self, request: str):
        split_request = request.split()
        self._amount = int(split_request[1])
        self._product = split_request[2]
        self._place_from = split_request[4]
        self._place_to = split_request[6]

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        self._amount = amount

    @property
    def product(self):
        return self._product

    @product.setter
    def product(self, product):
        self._product = product

    @property
    def place_from(self):
        return self._place_from

    @place_from.setter
    def place_from(self, place_from):
        self._place_from = place_from

    @property
    def place_to(self):
        return self._place_to

    @place_to.setter
    def place_to(self, place_to):
        self._place_to = place_to

"""
3)
строки где замечено: 
https://github.com/sacred70/lesson_21/blob/master/classes/class_Storage.py#L14

как бы я решил/переписал:
"""
from abc import ABC, abstractmethod


class Storage(ABC):
    @abstractmethod
    def add(self, title, amount):
        pass

    @abstractmethod
    def remove(self, title, amount):
        pass

    @abstractmethod
    def get_free_space(self):
        pass

    @abstractmethod
    def get_items(self):
        pass

    @abstractmethod
    def get_unique_items_count(self):
        pass

    @abstractmethod
    def is_item(self, title):
        pass
