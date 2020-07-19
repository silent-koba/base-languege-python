from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, r):
        self.r = r

    @abstractmethod
    def method1(self):
        pass

class Palto(Clothes):
    def __init__(self, r):
        self.r = r
    @property
    def method1(self):
        result = self.r / 6.5 + 0.5
        return result

class Costum(Clothes):
    def __init__(self, r):
        self.r = r
    @property
    def method1(self):
        result = 2 * self.r + 0.3
        return result

palto = Palto(float(input('Введите размер для пальто: ')))
costum = Costum(float(input('Введите рост для костюма: ')))
print(palto.method1)
print(costum.method1)
summ = palto.method1+costum.method1
print(f'Всего ткани на пальто и костюм нужно {summ}')

