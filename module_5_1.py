class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print("Такого этажа не существует")
        else:
            for i in range(1, new_floor + 1):
                print(i)


h_1 = House('ЖК Эльбрус', 30)
h_2 = House('Домик в деревне', 2)
# print(dom.name, dom.number_of_floors)
h_1.go_to(5)
h_2.go_to(3)