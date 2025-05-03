from copy import copy
from random import randint


class ProtectedDictInt:
    def __init__(self):
        self.__dict = {}  # Словник

    def __setitem__(self, key, value):
        if not isinstance(key, int):
            raise KeyError("Ключ має бути цілим числом")

        if key in self.__dict:
            raise PermissionError("Зміна значення існуючого ключа заборонена")

        self.__dict[key] = value

    def __getitem__(self, key):
        return self.__dict[key]

    def __add__(self, other):
        result_dict = ProtectedDictInt()
        for key, val in self.__dict.items():
            result_dict[key] = val

        if isinstance(other, ProtectedDictInt):
            for key, val in other.__dict.items():
                result_dict[key] = val
        elif isinstance(other, tuple) and len(other) == 2:
            result_dict[other[0]] = other[1]
        else:
            raise ValueError("Неприпустимий тип операнду")

        return result_dict

    def __sub__(self, other):
        if isinstance(other, int) and other in self:
            result_dict = ProtectedDictInt()
            for key, val in self.__dict.items():
                if key != other:
                    result_dict[key] = val
            return result_dict
        else:
            raise ValueError("Ключ для видалення некоректний")

    def __contains__(self, key):
        return key in self.__dict

    def __len__(self):
        return len(self.__dict)

    def __str__(self):
        return str(self.__dict)

    def __iter__(self):
        return ProtectedDictIntIterator(self.__dict)


class ProtectedDictIntIterator:
    def __init__(self, collection):
        self._sorted_keys = copy(sorted(list(collection)))
        self._collection = collection
        self._cursor = 0

    def __next__(self):
        if self._cursor >= len(self._sorted_keys):
            raise StopIteration
        key = self._sorted_keys[self._cursor]
        self._cursor += 1
        return (key, self._collection[key])

    def __iter__(self):
        return self


def construct():
    object_list = []
    d = ProtectedDictInt()
    for i in range(20):
        try:
            key = randint(0, 1000)
            d[key] = key
        except:
            pass

    object_list.append(d)
    object_list.append(10)
    object_list.append("1234")
    object_list.append([1, 3, 4])
    object_list.append(ProtectedDictIntIterator({1: 3}))
    object_list.append(5.3)
    object_list.append({5: 5, 23: 23, 12: 12})
    return object_list


##########################################
############### МОЇ ЗМІНИ ################
##########################################


def decor(f):
    def _decor(*arg, **kw):
        print(f'Function: {f.__name__}')
        return f(*arg, **kw)
    return _decor


def log_instance_creation(cls):
    original_init = cls.__init__

    def new_init(self, *args, **kwargs):
        print(f"Створено екземпляр класу: {cls.__name__}")
        original_init(self, *args, **kwargs)

    cls.__init__ = new_init
    return cls


@decor
def isIterable(obj):
    return hasattr(obj, '__iter__') and callable(obj.__iter__)


@log_instance_creation
class MyClass:
    def __init__(self, value):
        self.value = value

    def print(self):
        print(self.value)


if __name__ == "__main__":
    lst = construct()
    for obj in lst:
        if isIterable(obj):
            print(f"Об'єкт {type(obj)} підтримує ітерацію: {obj}")
            try:
                for it in obj:
                    print(it)
            except Exception as e:
                print(f"Помилка під час ітерації: {e}")
            print()