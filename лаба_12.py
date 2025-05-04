class RationalError(ZeroDivisionError):  # власний клас обробки помилки
    def __init__(self, message):
        ZeroDivisionError.__init__(self)
        super().__init__(message)
        self._message = message

    def __str__(self):
        return "RationalError" + str(self._message)


class Rational:
    def __init__(self, n, d):
        self._n = n
        if d == 0:
            self._d = None
            raise RationalError("Знаменник рівний нулю.")
        else:
            self._d = d

    def __str__(self):
        return str(self._n) + '/' + str(self._d)

    def __call__(self):
        return self._n / self._d
    # def __add__(self, other):


num = Rational(2, 4)
print(num)