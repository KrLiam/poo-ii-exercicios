
class Math:
    def __init__(self):
        self.__fib_cache = {}
        self.__fact_cache = {}

    def fibonacci(self, n: int):
        if n <= 1:
            return 1

        if n not in self.__fib_cache:
            self.__fib_cache[n] = self.fibonacci(n-1) + self.fibonacci(n-2)
            
        return self.__fib_cache[n]
    
    def fatorial(self, n: int):
        if n <= 1:
            return 1
        
        if n not in self.__fact_cache:
            self.__fact_cache[n] = n * self.fatorial(n-1)
        
        return self.__fact_cache[n]

    def primos(self, n: int = float("inf")):
        """Gera os n primeiros números primos."""

        seq = [2]
        i = 3

        yield 2

        while True:
            if not any(i % p == 0 for p in seq):
                seq.append(i)
                yield i

                if len(seq) >= n:
                    break

            i += 2


if __name__ == "__main__":
    math = Math()

    print(math.fibonacci(20))

    print([math.fibonacci(i) for i in range(20)])

    print([math.fatorial(i) for i in range(10)])

    print(*math.primos(40), sep=" ")