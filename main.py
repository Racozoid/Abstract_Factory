from abc import ABC, abstractmethod
import random


# Три функции генерации случайных чисел в диапазоне от 1 до 100
def generate_high():
    return random.randint(67, 100)


def generate_medium():
    return random.randint(34, 66)


def generate_low():
    return random.randint(1, 33)


class FantasyFactory(ABC):
    """Сама абстрактная фабрика"""
    @abstractmethod
    def create_sword(self):
        pass

    @abstractmethod
    def create_spear(self):
        pass

    @abstractmethod
    def create_crossbow(self):
        pass


class PoisonFactory(FantasyFactory):
    """Конкретная фабрика номер 1
    Создает ядовитые вещи"""
    def create_sword(self):
        return PoisonSword()

    def create_spear(self):
        return PoisonSpear()

    def create_crossbow(self):
        return PoisonCrossbow()


class FireFactory(FantasyFactory):
    """Конкретная фабрика номер 2
    Создает огненные вещи"""
    def create_sword(self):
        return FireSword()

    def create_spear(self):
        return FireSpear()

    def create_crossbow(self):
        return FireCrossbow()


class FrostFactory(FantasyFactory):
    """Конкретная фабрика номер 3
    Создает морозные вещи"""
    def create_sword(self):
        return FrostSword()

    def create_spear(self):
        return FrostSpear()

    def create_crossbow(self):
        return FrostCrossbow()


class AbstractSword(ABC):
    """Абстрактный меч
    Должен уметь менять свои характеристики"""
    @abstractmethod
    def change_characteristics(self):
        pass


class FireSword(AbstractSword):
    """Огненный меч, при создании ему присваиваются случайные характеристики
    (Конкретный продукт A1)"""
    def __init__(self):
        self.parameters = dict()
        self.parameters['mod'] = 'fire'
        self.parameters['type_of_damage'] = 'melee'
        self.parameters['damage'] = generate_high()
        self.parameters['range'] = generate_low()
        self.parameters['speed'] = generate_low()
        print('You created fire sword')

    def change_characteristics(self):
        self.parameters['damage'] = generate_high()
        self.parameters['range'] = generate_low()
        self.parameters['speed'] = generate_low()
        print('Characteristics changed')

    def __repr__(self):
        damage = self.parameters['damage']
        mod = self.parameters['mod']
        range_of = self.parameters['range']
        speed = self.parameters['speed']
        type_of = self.parameters['type_of_damage']
        return f'This is a sword. It deals {damage} {mod} {type_of} damage. ' \
               f'His speed equal {speed} and his range equal {range_of} meters'


class PoisonSword(AbstractSword):
    """Ядовитый меч, при создании ему присваиваются случайные характеристики
    (Конкретный продукт A2)"""
    def __init__(self):
        self.parameters = dict()
        self.parameters['mod'] = 'poison'
        self.parameters['type_of_damage'] = 'melee'
        self.parameters['damage'] = generate_low()
        self.parameters['range'] = generate_low()
        self.parameters['speed'] = generate_high()
        print('You created poison sword')

    def change_characteristics(self):
        self.parameters['damage'] = generate_low()
        self.parameters['range'] = generate_low()
        self.parameters['speed'] = generate_high()
        print('Characteristics changed')

    def __repr__(self):
        damage = self.parameters['damage']
        mod = self.parameters['mod']
        range_of = self.parameters['range']
        speed = self.parameters['speed']
        type_of = self.parameters['type_of_damage']
        return f'This is a sword. It deals {damage} {mod} {type_of} damage. ' \
               f'His speed equal {speed} and his range equal {range_of} meters'


class FrostSword(AbstractSword):
    """Морозный меч, при создании ему присваиваются случайные характеристики
    (Конкретный продукт A3  )"""
    def __init__(self):
        self.parameters = dict()
        self.parameters['mod'] = 'frost'
        self.parameters['type_of_damage'] = 'melee'
        self.parameters['damage'] = generate_medium()
        self.parameters['range'] = generate_low()
        self.parameters['speed'] = generate_low()
        print('You created frost sword')

    def change_characteristics(self):
        self.parameters['damage'] = generate_medium()
        self.parameters['range'] = generate_low()
        self.parameters['speed'] = generate_low()
        print('Characteristics changed')

    def __repr__(self):
        damage = self.parameters['damage']
        mod = self.parameters['mod']
        range_of = self.parameters['range']
        speed = self.parameters['speed']
        type_of = self.parameters['type_of_damage']
        return f'This is a sword. It deals {damage} {mod} {type_of} damage. ' \
               f'His speed equal {speed} and his range equal {range_of} meters'


class AbstractSpear(ABC):
    """Абстрактное копье
    Должно уметь менять свои характеристики"""
    @abstractmethod
    def change_characteristics(self):
        pass


class PoisonSpear(AbstractSpear):
    """Ядовитое копье, при создании ему присваиваются случайные характеристики
    (Конкретный продукт B1)"""
    def __init__(self):
        self.parameters = dict()
        self.parameters['mod'] = 'poison'
        self.parameters['type_of_damage'] = 'piercing'
        self.parameters['damage'] = generate_low()
        self.parameters['range'] = generate_medium()
        self.parameters['speed'] = generate_medium()
        print('You created poison spear')

    def change_characteristics(self):
        self.parameters['damage'] = generate_low()
        self.parameters['range'] = generate_medium()
        self.parameters['speed'] = generate_medium()
        print('Characteristics changed')

    def __repr__(self):
        damage = self.parameters['damage']
        mod = self.parameters['mod']
        range_of = self.parameters['range']
        speed = self.parameters['speed']
        type_of = self.parameters['type_of_damage']
        return f'This is a spear. It deals {damage} {mod} {type_of} damage. ' \
               f'His speed equal {speed} and his range equal {range_of} meters'


class FireSpear(AbstractSpear):
    """Огненное копье, при создании ему присваиваются случайные характеристики
        (Конкретный продукт B2)"""
    def __init__(self):
        self.parameters = dict()
        self.parameters['mod'] = 'fire'
        self.parameters['type_of_damage'] = 'piercing'
        self.parameters['damage'] = generate_high()
        self.parameters['range'] = generate_medium()
        self.parameters['speed'] = generate_low()
        print('You created fire spear')

    def change_characteristics(self):
        self.parameters['damage'] = generate_high()
        self.parameters['range'] = generate_medium()
        self.parameters['speed'] = generate_low()
        print('Characteristics changed')

    def __repr__(self):
        damage = self.parameters['damage']
        mod = self.parameters['mod']
        range_of = self.parameters['range']
        speed = self.parameters['speed']
        type_of = self.parameters['type_of_damage']
        return f'This is a spear. It deals {damage} {mod} {type_of} damage. ' \
               f'His speed equal {speed} and his range equal {range_of} meters'


class FrostSpear(AbstractSpear):
    """Морозное копье, при создании ему присваиваются случайные характеристики
    (Конкретный продукт B3)"""
    def __init__(self):
        self.parameters = dict()
        self.parameters['mod'] = 'frost'
        self.parameters['type_of_damage'] = 'piercing'
        self.parameters['damage'] = generate_medium()
        self.parameters['range'] = generate_medium()
        self.parameters['speed'] = generate_low()
        print('You created fire spear')

    def change_characteristics(self):
        self.parameters['damage'] = generate_medium()
        self.parameters['range'] = generate_medium()
        self.parameters['speed'] = generate_low()
        print('Characteristics changed')

    def __repr__(self):
        damage = self.parameters['damage']
        mod = self.parameters['mod']
        range_of = self.parameters['range']
        speed = self.parameters['speed']
        type_of = self.parameters['type_of_damage']
        return f'This is a spear. It deals {damage} {mod} {type_of} damage. ' \
               f'His speed equal {speed} and his range equal {range_of} meters'


class AbstractCrossbow(ABC):
    """Абстрактный арбалет
    Должен уметь менять свои характеристики"""
    @abstractmethod
    def change_characteristics(self):
        pass


class PoisonCrossbow(AbstractCrossbow):
    """Огненный арбалет, при создании ему присваиваются случайные характеристики
    (Конкретный продукт С1)"""
    def __init__(self):
        self.parameters = dict()
        self.parameters['mod'] = 'poison'
        self.parameters['type_of_damage'] = 'range'
        self.parameters['damage'] = generate_low()
        self.parameters['range'] = generate_high()
        self.parameters['speed'] = generate_medium()
        print('You created poison crossbow')

    def change_characteristics(self):
        self.parameters['damage'] = generate_low()
        self.parameters['range'] = generate_high()
        self.parameters['speed'] = generate_medium()
        print('Characteristics changed')

    def __repr__(self):
        damage = self.parameters['damage']
        mod = self.parameters['mod']
        range_of = self.parameters['range']
        speed = self.parameters['speed']
        type_of = self.parameters['type_of_damage']
        return f'This is a crossbow. It deals {damage} {mod} {type_of} damage. ' \
               f'His speed equal {speed} and his range equal {range_of} meters'


class FireCrossbow(AbstractCrossbow):
    """Огненный арбалет, при создании ему присваиваются случайные характеристики
    (Конкретный продукт С2)"""
    def __init__(self):
        self.parameters = dict()
        self.parameters['mod'] = 'fire'
        self.parameters['type_of_damage'] = 'range'
        self.parameters['damage'] = generate_high()
        self.parameters['range'] = generate_high()
        self.parameters['speed'] = generate_low()
        print('You created fire crossbow')

    def change_characteristics(self):
        self.parameters['damage'] = generate_high()
        self.parameters['range'] = generate_high()
        self.parameters['speed'] = generate_low()
        print('Characteristics changed')

    def __repr__(self):
        damage = self.parameters['damage']
        mod = self.parameters['mod']
        range_of = self.parameters['range']
        speed = self.parameters['speed']
        type_of = self.parameters['type_of_damage']
        return f'This is a crossbow. It deals {damage} {mod} {type_of} damage. ' \
               f'His speed equal {speed} and his range equal {range_of} meters'


class FrostCrossbow(AbstractCrossbow):
    """Огненный арбалет, при создании ему присваиваются случайные характеристики
    (Конкретный продукт С2)"""
    def __init__(self):
        self.parameters = dict()
        self.parameters['mod'] = 'frost'
        self.parameters['type_of_damage'] = 'range'
        self.parameters['damage'] = generate_medium()
        self.parameters['range'] = generate_high()
        self.parameters['speed'] = generate_medium()
        print('You created frost crossbow')

    def change_characteristics(self):
        self.parameters['damage'] = generate_medium()
        self.parameters['range'] = generate_high()
        self.parameters['speed'] = generate_medium()
        print('Characteristics changed')

    def __repr__(self):
        damage = self.parameters['damage']
        mod = self.parameters['mod']
        range_of = self.parameters['range']
        speed = self.parameters['speed']
        type_of = self.parameters['type_of_damage']
        return f'This is a crossbow. It deals {damage} {mod} {type_of} damage. ' \
               f'His speed equal {speed} and his range equal {range_of} meters'


def create_set_of_weapons(factory: FantasyFactory):
    # Создание всех объектов каждой фабрики
    sword = factory.create_sword()
    spear = factory.create_spear()
    crossbow = factory.create_crossbow()

    print(f'{sword}\n{spear}\n{crossbow}')
    print('\nOh! Something wrong!')

    # Применение методов каждого объекта
    sword.change_characteristics()
    spear.change_characteristics()
    crossbow.change_characteristics()
    print(f'{sword}\n{spear}\n{crossbow}')
    print('That\'s better!')


# Непосредственно работа фабрики
print('Let\'s create some weapons!')
create_set_of_weapons(PoisonFactory())
print('\n\nAnd more...')
create_set_of_weapons(FireFactory())
print('\n\nMore!')
create_set_of_weapons(FrostFactory())
input('\n\nTo exit press ENTER')
