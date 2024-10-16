from random import randint, choice


class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return f'{self.__name} health: {self.__health} damage: {self.__damage}'


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)
        self.__defence = None

    def choose_defence(self, heroes_list):
        random_hero = choice(heroes_list)
        self.__defence = random_hero.ability

    def attack(self, heroes_list):
        for hero in heroes_list:
            if hero.health > 0:
                if type(hero) == Berserk and self.__defence != hero.ability:
                    hero.blocked_damage = choice([5, 10])
                    hero.health -= (self.damage - hero.blocked_damage)
                else:
                    hero.health -= self.damage

    @property
    def defence(self):
        return self.__defence

    def __str__(self):
        return 'BOSS ' + super().__str__() + f' defence: {self.__defence}'


class Hero(GameEntity):
    def __init__(self, name, health, damage, ability):
        super().__init__(name, health, damage)
        self.__ability = ability

    @property
    def ability(self):
        return self.__ability

    def apply_super_power(self, boss, heroes_list):
        pass

    def attack(self, boss):
        boss.health -= self.damage

    def take_damage(self, damage):
        self.health -= damage


class Warrior(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'CRITICAL_DAMAGE')

    def apply_super_power(self, boss, heroes_list):
        coeff = randint(2, 5)
        boss.health -= coeff * self.damage
        print(f'Warrior {self.name} hits critically {coeff * self.damage}.')


class Magic(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'BOOST')

    def apply_super_power(self, boss, heroes_list):
        # TODO here will be implementation of boosting
        pass


class Berserk(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'BLOCK_DAMAGE')
        self.__blocked_damage = 0

    def apply_super_power(self, boss, heroes_list):
        boss.health -= self.blocked_damage
        print(f'Berserk {self.name} reverted {self.__blocked_damage} damages to boss.')

    @property
    def blocked_damage(self):
        return self.__blocked_damage

    @blocked_damage.setter
    def blocked_damage(self, value):
        self.__blocked_damage = value

class Medic(Hero):
    def __init__(self, name, health, damage, heal_points):
        super().__init__(name, health, damage, 'HEAL')
        self.__heal_points = heal_points

    def apply_super_power(self, boss, heroes_list):
        for hero in heroes_list:
            if hero.health > 0 and hero != self:
                hero.health += self.__heal_points


class Witcher(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'revive')

    def apply_super_power(self, boss, heroes_list):
        for hero in heroes_list:
            if hero.health <= 0:
                print(F'{self.name} жертвует собой ради {hero.name} и погибает сам!')
                hero.health = self.health
                self.health = 0
                break

class Magic_another(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'BUFF')

    def apply_super_power(self, boss, heroes_list):
            if round_number >= 1:
                Buff = randint(5, 10,)
                print(F"В этом раунде маг {self.name} наложил заклинание усиления на"
                      F" всех героев и увеличил урон каждого на:{Buff}")
                for hero in heroes_list:
                    if hero.health > 0:
                       hero.damage += Buff
                    break

class Hacker(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'STEAL HP')

    def apply_super_power(self, boss, heroes_list,):
        steal_hp = randint(1, 10)
        if boss.health > 0:
            boss.health -= steal_hp

            target_hero = choice(heroes_list)

            target_hero.health += steal_hp
            print(f"{self.name} украл {steal_hp} очки здоровья и передал их {target_hero.name}.")

class Golem(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'DAMAGE_SHARE')

    def apply_super_power(self, boss, heroes_list):
        for hero in heroes_list:
            if hero != self and hero.health > 0:
                shared_damage = boss.damage * 0.2
                hero.take_damage(boss.damage - shared_damage)
                self.health -= shared_damage
                print(f'Golem {self.name} принял {shared_damage} урона от босса за {hero.name}.')

class Avrora(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'INVISIBILITY')
        self.invisible = False
        self.rounds_in_invisibility = 0

    def apply_super_power(self, boss, heroes_list):
        if not self.invisible and self.rounds_in_invisibility == 0:
            self.invisible = True
            self.rounds_in_invisibility = 2
            print(f'Avrora {self.name} стала невидимой.')
        elif self.invisible:
            self.rounds_in_invisibility -= 1
            print(f'Avrora {self.name} невидима. Урона не получено.')
            if self.rounds_in_invisibility == 0:
                self.invisible = False
                boss.health -= boss.damage
                print(f'Avrora {self.name} возвращает {boss.damage} урона боссу.')

    def take_damage(self, damage):
        if not self.invisible:
            super().take_damage(damage)


round_number = 0


def is_game_over(boss, heroes_list):
    if boss.health <= 0:
        print('Heroes won!!!')
        return True
    all_heroes_dead = True
    for hero in heroes_list:
        if hero.health > 0:
            all_heroes_dead = False
            break
    if all_heroes_dead:
        print('Boss won!!!')
        return True
    return False


def show_statistics(boss, heroes_list):
    print(f' ------------- ROUND {round_number} -------------')
    print(boss)
    for hero in heroes_list:
        print(hero)


def play_round(boss, heroes_list):
    global round_number
    round_number += 1
    boss.choose_defence(heroes_list)
    boss.attack(heroes_list)
    for hero in heroes_list:
        if hero.health > 0 and boss.health > 0 and boss.defence != hero.ability:
            hero.attack(boss)
            hero.apply_super_power(boss, heroes_list)
    show_statistics(boss, heroes_list)

def start_game():
    boss = Boss(name='Minotavr', health=1000, damage=50)

    warrior_1 = Warrior(name='Asterix', health=290, damage=10)
    warrior_2 = Warrior(name='Obelix', health=280, damage=15)
    magic = Magic(name='Alice', health=270, damage=5)
    berserk = Berserk(name='Guts', health=220, damage=10)
    doc = Medic(name='Doc', health=200, damage=5, heal_points=15)
    assistant = Medic(name='Junior', health=300, damage=5, heal_points=5)
    witcher = Witcher(name='Geralt', health=350, damage=0,)
    magic_buff = Magic_another(name='Ezra', health=250, damage=5)
    hacker = Hacker(name='ShadowTrace', health=300, damage=10)
    golem = Golem(name='Rocky', health=450, damage=20)
    avrora = Avrora(name='Avrora', health=270, damage=15)

    heroes_list = [warrior_1, doc, warrior_2, magic, berserk, assistant]
    show_statistics(boss, heroes_list)
    heroes_list.append(witcher)
    heroes_list.append(magic_buff)
    heroes_list.append(hacker)
    heroes_list.append(golem)
    heroes_list.append(avrora)

    while not is_game_over(boss, heroes_list):
        play_round(boss, heroes_list)

start_game()