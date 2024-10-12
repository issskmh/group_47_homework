class Computer:
    def init(self, cpu=0, memory=0):  # Добавлены параметры по умолчанию
        self.__cpu = cpu  # Приватный атрибут cpu
        self.__memory = memory  # Приватный атрибут memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def make_computations(self):
        # Пример вычислений: сумма памяти и количества ядер процессора
        return self.cpu * self.memory  # Пример вычисления

    def str(self):
        return f'Computer(cpu={self.cpu}, memory={self.memory})'

    def eq(self, other):
        return self.memory == other.memory

    def ne(self, other):
        return self.memory != other.memory

    def lt(self, other):
        return self.memory < other.memory

    def le(self, other):
        return self.memory <= other.memory

    def gt(self, other):
        return self.memory > other.memory

    def ge(self, other):
        return self.memory >= other.memory


class Phone:
    def init(self, sim_cards_list=None):
        if sim_cards_list is None:  # Проверка на None для избежания ошибки
            sim_cards_list = []
        self.__sim_cards_list = sim_cards_list  # Приватный атрибут списка сим-карт

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    def call(self, sim_card_number, call_to_number):
        try:
            sim_card_info = self.__sim_cards_list[sim_card_number]
            print(f"Идет звонок на номер {call_to_number} с сим-карты-{sim_card_number + 1} - {sim_card_info}")
        except IndexError:
            print("Неверный номер сим-карты")

    def str(self):
        return f'Phone(sim_cards_list={self.__sim_cards_list})'


class SmartPhone(Computer, Phone):
    def init(self, cpu=0, memory=0, sim_cards_list=None):
        Computer.init(self, cpu, memory)
        Phone.init(self, sim_cards_list)

    def use_gps(self, location):
        print(f"Построение маршрута до {location}")

    def str(self):
        return f'SmartPhone(cpu={self.cpu}, memory={self.memory}, sim_cards_list={self.sim_cards_list})'


# Создание объектов
computer1 = Computer(cpu=4, memory=16)
phone1 = Phone(sim_cards_list=["Beeline", "MegaCom", "O!"])
smartphone1 = SmartPhone(cpu=8, memory=32, sim_cards_list=["Beeline", "MegaCom"])
smartphone2 = SmartPhone(cpu=6, memory=64, sim_cards_list=["O!", "Beeline"])

# Печать информации о созданных объектах
print(computer1)
print(phone1)
print(smartphone1)
print(smartphone2)

# Применение методов
print("Результат вычислений на компьютере:", computer1.make_computations())
phone1.call(0, "+996 777 99 88 11")  # Звонок с первой сим-карты
smartphone1.use_gps("Ала-Арча")
smartphone2.use_gps("Ош")  # Пример вызова метода use_gps

# Применение магических методов сравнения
print(f"Сравнение памяти smartphone1 и smartphone2: {smartphone1.memory == smartphone2.memory}")
print(f"Сравнение smartphone1 < smartphone2: {smartphone1 < smartphone2}")