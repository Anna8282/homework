class RationalError(ZeroDivisionError):  # власний клас обробки помилки
    def __init__(self, message):
        ZeroDivisionError.__init__(self)
        super().__init__(message)
        self._message = message

    def __str__(self):
        return "RationalError" + str(self._message)


class RationalValueError(ValueError):
    def __init__(self, message):
        ValueError.__init__(self)
        super().__init__(message)
        self._message = message

    def __str__(self):
        return "RationalValueError: " + str(self._message)



class Rational:
    def __init__(self, n, d):
        if d == 0:
            raise RationalError("Знаменник рівний нулю.")
        self._n = n
        self._d = d
        self._reduce()

    def _reduce(self):
        g = gcd(self._n, self._d)
        self._n //= g
        self._d //= g
        if self._d < 0:
            self._n *= -1
            self._d *= -1

    def __str__(self):
        return f"{self._n}/{self._d}"

    def __call__(self):
        return self._n / self._d


from math import gcd


class Rational:
    def __init__(self, n, d):
        self._n = n
        self._d = d
        self._reduce()

    def __str__(self):
        return str(self._n) + '/' + str(self._d)

    def __call__(self):  # круглі дужки
        return self._n / self._d

    def _reduce(self):
        g = gcd(self._n, self._d)
        self._n //= g
        self._d //= g
        if self._d < 0:
            self._n *= -1
            self._d *= -1

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
        if not isinstance(value, int):
            raise TypeError
        if key == "n":
            self.n = value
        elif key == "d":
            if value == 0:
                raise ValueError
            self.d = value
        else:
            raise KeyError
        self._reduce()

def __getitem__(self, item):
    if item == 'n':
        return self._n
    elif item == 'd':
        return self.__dict
    else:
        raise KeyError


def parse_token(token):
    if '/' in token:
        a, b = map(int, token.split('/'))
        return Rational(a, b)
    else:
        return Rational(int(token), 1)

def evaluate_expression(line):
    tokens = line.strip().split()
    if not tokens:
        return None

    result = parse_token(tokens[0])
    i = 1
    while i < len(tokens):
        op = tokens[i]
        right = parse_token(tokens[i + 1])

        if op == '+':
            result = result + right
        elif op == '-':
            result = result - right
        elif op == '*':
            result = result * right
        elif op == '/':
            result = result / right
        else:
            raise ValueError(f"{op}")
        i += 2
    return result


with open('input01.txt', 'r') as infile, open('output01.txt', 'w') as outfile:
    for line in infile:
        try:
            res = evaluate_expression(line)
            outfile.write(f"{res} = {res()}\n")
        except Exception as e:
            outfile.write(f"{e}\n")


num = Rational(3, 4)
print(num())


num = Rational(2, 4)
print(num)