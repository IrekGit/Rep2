class House:
    houses_history = []

    def __new__(cls, *args):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self, *args):
        self.houses_history.remove(self.name)   # удаление снесенного дома из списка
        print(f'{self.name} снесён ({self.number_of_floors} этажей), но он останется в истории')


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 30)
print(House.houses_history)
print()
del h2
print(House.houses_history)
del h3
print(House.houses_history)