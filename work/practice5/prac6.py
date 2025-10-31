class Hero:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def armor(self, armor):
        armor_dict = {
            'light': 'Кожанка',
            'middle': 'Кольчуга',
            'heavy': 'Латный доспех',
            'ultra_heavy': 'Рыцарские доспехи',
        }
        return armor_dict.get(armor)

    def weapon(self, weapon):
        weapon_dict = {
            'melee_low_range': 'Кинжалы',
            'melee_middle_range': 'Рапира',
            'melee_long_range': 'Двуручный меч',
            'ranger_light': 'Арбалет',
            'ranger_middle': 'Лук',
            'ranger_heavy': 'Мушкет',
        }
        return weapon_dict.get(weapon)

    def get_data(self, pick_armor, pick_weapon):
        self.pick_armor = self.armor(pick_armor)
        self.pick_weapon = self.weapon(pick_weapon)
        print('Добро пожаловать!', self.name, 'Ваша броня:', self.pick_armor, 'Ваше оружие:', self.pick_weapon)


name = input('Введите имя вашего персонажа: ')
new_player = Hero(name, 100)

pick_armor = input('Выбор брони: (light), (middle), (heavy), (ultra_heavy): ').lower()
pick_weapon = input('Выбор оружия: (melee_low_range), (melee_middle_range), (melee_long_range), (ranger_light), (ranger_middle), (ranger_heavy): ')

new_player.get_data(pick_armor, pick_weapon)


                

