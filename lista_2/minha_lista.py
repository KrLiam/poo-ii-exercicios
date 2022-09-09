class MinhaLista:
    def __init__(self, tupla = ()):
        self.__valores = tupla
    
    def append(self, valor):
        self.__valores = (*self.__valores, valor)

    def remove(self, valor):
        r = []
        removeu = False

        for x in self.__valores:
            if x == valor and not removeu:
                removeu = True
                continue

            r.append(x)

        self.__valores = tuple(r)

    def sort(self):
        self.__valores = sorted(self.__valores)

    def reverse(self):
        self.__valores = self.__valores[::-1]

    def pop(self, index=-1):
        r = []

        if index < 0:
            index = len(self.__valores) + index

        for i, x in enumerate(self.__valores):
            if i != index:
                r.append(x)

        self.__valores = tuple(r)
    
    def __str__(self):
        return str(self.__valores)
    
    def __setitem__(self, index, valor):
        r = []

        if index < 0:
            index = len(self.__valores) + index

        for i, x in enumerate(self.__valores):
            r.append(valor if i == index else x)

        self.__valores = tuple(r)
    
    def __getitem__(self, key):
        return self.__valores[key]

l = MinhaLista()

l.append(9)
l.append(10)
l.append(-5)
l.append(10)

print(l)

l.remove(10)

print(l)

[].reverse

l.sort()

print(l)

l.pop(-1)
l.pop(0)

l.append(8)
l.append(8)
l.append(8)

print(l)

l[2] = 7
l[-1] = 6

print(l)

print(l[0])
print(l[2:])
