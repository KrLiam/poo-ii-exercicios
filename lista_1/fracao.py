from typing import Tuple


def mdc(a: int, b: int) -> int:
    if a == 0:
        return abs(b)

    while b != 0:
        a, b = b, a % b

    return abs(a)


def mmc(a: int, b: int) -> int:
    return a * b // mdc(a, b)


def normalize(a: float, b: float) -> Tuple[int, int]:
    while a % 1 or b % 1:
        a *= 10
        b *= 10

    m = mdc(a, b)
    return int(a / m), int(b / m)


class Fracao:
    def __init__(self, numerador, denominador=1):
        numerador, denominador = normalize(numerador, denominador)

        if denominador < 0:
            numerador *= -1
            denominador *= -1

        self.__num = numerador
        self.__den = denominador
    
    @property
    def numerador(self):
        return self.__num

    @property
    def denominador(self):
        return self.__den

    @property
    def value(self):
        return self.__num / self.__den

    def __mul__(self, value):
        if isinstance(value, Fracao):
            return Fracao(
                self.__num * value.numerador, self.__den * value.denominador
            )

        if isinstance(value, (int, float)):
            return Fracao(self.__num * value, self.__den)

        return NotImplemented

    def __rmul__(self, value):
        return self.__mul__(value)

    def __add__(self, other):
        if isinstance(other, Fracao):
            m = mmc(self.__den, other.denominador)
            numerador = (
                self.__num * m / self.__den
                + other.numerador * m / other.denominador
            )
            return Fracao(numerador, m)

        if isinstance(other, (int, float)):
            return Fracao(self.value + other)

        return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        return self.__add__(other.__neg__())

    def __rsub__(self, other):
        negated = self.__neg__()
        return negated.__add__(other)

    def __truediv__(self, other):
        if isinstance(other, Fracao):
            return Fracao(
                self.__num * other.denominador, self.__den * other.numerador
            )

        if isinstance(other, (int, float)):
            return Fracao(self.__num, self.__den * other)

        return NotImplemented

    def __rtruediv__(self, other):
        if isinstance(other, (int, float)):
            return Fracao(self.__den * other, self.__num)

        return NotImplemented

    def __neg__(self):
        return Fracao(-self.__num, self.__den)

    def __eq__(self, other):
        if isinstance(other, Fracao):
            return (
                self.__num == other.numerador
                and self.__den == other.denominador
            )

        if isinstance(other, (int, float)):
            return self.value == other

        return NotImplemented

    def __repr__(self):
        return f"Fracao({self.__num}, {self.__den})"

    def __str__(self):
        return f"{self.__num}/{self.__den}"

    def __float__(self):
        return self.value

    def __int__(self):
        return int(self.value)
    
    def __bool__(self):
        return bool(self.value)


if __name__ == "__main__":
    print(Fracao(1, 2), Fracao(1/2), Fracao(0.5))

    # métodos para soma, subtração,
    # multiplicação e divisão
    print(Fracao(1, 4) + Fracao(5, 10))
    print(Fracao(5, 3) - Fracao(1, 4))
    print(Fracao(10, 3) * Fracao(1, 5))
    print(Fracao(5, 3) / Fracao(5, 3))

    # imprimir fração
    print(repr(Fracao(3, 2)))
    print(str(Fracao(3, 2)))

    # inverter a fração
    print(1 / Fracao(4, 5))

    # retornar valor real de uma fração
    print(Fracao(3, 4).value)

    # criar fração a partir de um valor real
    print(Fracao(0.75))