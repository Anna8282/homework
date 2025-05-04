from math import gcd


class Rational:
    def __init__(self, n, d):
        self._n = n
        self._d = d

    def __str__(self):
        return str(self._n) + '/' + str(self._d)

    def __call__(self):  # круглі дужки
        return self._n / self._d

    def __add__(self, other):
        result = Rational(0, 1)
        if isinstance(other, int):
            other = Rational(other, 1)
        elif not isinstance(other, Rational):
            raise TypeError

        zn = self._d * other.d // gcd(self._d, other.d)
        num = self._n * (zn // self._d) + other * (zn // other.d)

        return Rational(num, zn)

        # визначити знаменник нсд, зведення до нескоротного дробу

    def __setitem__(self, key, value):
        if not isinstance(key, int):  # перевіряє чи key лежить в інт
            raise KeyError
        if key in self.__dict:  # якщо таке значення в словнику вже є
            raise PermissionError  # помилка заповнення
        self.__dict[key] = value

def __getitem__(self, item):
    if item == 'n':
        return self._n
    elif item == 'd'
        return self.__dict
    else:
        raise KeyError


num = Rational(3, 4)
print(num())