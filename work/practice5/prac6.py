class Hero:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
    def equipment(self, var):
        equip = {
            '1' : {'armor' : 'Легкая броня', 'weapon' : 'Копье'},
            '2' : {'armor' : 'Средняя броня', 'weapon' : 'Булава'},
            '3' : {'armor' : 'Тяжелая броня', 'weapon' : 'Меч'},
            '4' : {'armor' : 'Мантия', 'weapon' : 'Лук'}
        }
        for pick in equip:
            if pick == var:
                return equip[pick]
    def get_data(self):
        self.equip = new_player.equipment(pick)
        print('Добро пожаловать!',self.name,',','Ваше снаряжение:', self.equip)
    def attack(self, damage):
        if damage > self.hp:
            self.hp = 0
        else:
            self.hp -= damage

                


new_player = Hero(input('Введите имя вашего персонажа: '), 100)
pick = input('Выбор снаряжения - (Крестьянин - 1, Пехотинец - 2, Рыцарь - 3, Лучник - 4): ')
equip_pick = new_player.equipment(pick)
data = new_player.get_data()