from itertools import zip_longest
from typing import Any, Iterable, Tuple


class Polinomio:
    def __init__(self, *coefs: Tuple[float]):
        if isinstance(coefs[0],  Iterable):
            coefs = coefs[0]

        self.__coefs = tuple(coefs)

    @property
    def coefs(self):
        return self.__coefs

    @property
    def grau(self):
        return len(self.__coefs) - 1

    def evaluate(self, x: float):
        return sum(coef * x**i for i, coef in enumerate(self.__coefs))
    
    def plot(self, start: float, end: float, num: int):
        step = (end - start) / num

        return tuple(self.evaluate(start + step * i) for i in range(num))

    def __getitem__(self, potencia: int):
        return self.__coefs[potencia]
    
    def __call__(self, x: float):
        return self.evaluate(x)

    def __add__(self, value: Any):
        if isinstance(value, Polinomio):
            return Polinomio(
                a + b for a, b in zip_longest(self.coefs, value.coefs, fillvalue=0)
            )
        
        return NotImplemented
    
    def __mul__(self, value: Any):
        if isinstance(value, Polinomio):
            size = len(self.coefs) + len(value.coefs) - 1
            coefs = [0] * size

            for i, a in enumerate(self.coefs):
                for j, b in enumerate(value.coefs):
                    coefs[i + j] += a * b
            
            return Polinomio(coefs)

        if isinstance(value, (int, float)):
            return Polinomio(
                coef * value for coef in self.__coefs
            )

        return NotImplemented
    
    def __rmul__(self, value: Any):
        return self.__mul__(value)
    
    def __eq__(self, value: Any):
        if isinstance(value, Polinomio):
            return self.coefs == value.coefs
        
        return NotImplemented
    
    def __repr__(self):
        return f"Polinomio(coefs={self.coefs})"


if __name__ == "__main__":
    quad = Polinomio(10, 5, 2)  # 2x^2 + 5x + 10

    print(quad)

    print(quad.coefs)
    print(quad.grau)

    print(quad[2], quad[1], quad[0])

    print(quad.evaluate(0))
    print(quad(0))

    cubic = Polinomio(4, 2, 1, 0.5) # (1/2)x^3 + x^2 + 2x + 4
    print(cubic)

    print(cubic(0))
    print(cubic(2))

    print(quad + cubic)

    t = Polinomio(1, 1) * Polinomio(1, -1) # (1 + x)(1 - x)
    print(t)
    print(t == Polinomio(1, 0, -1)) # (1 + x)(1 - x) = 1 - x²
    
    print(cubic.plot(-10, 10, 20))