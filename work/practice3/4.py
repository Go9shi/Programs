import random

lst = ['камень', 'ножницы', 'бумага']
pc_count = 0
player = 0
while True:
    user = input('Ваш ход - камень-ножницы-бумага :').lower()
    if user not in lst:
        print('Некорректный выбор: Error')
        continue
    
    
    pc = random.choice(lst)
    print('Выбор компьютера:', pc)

    if user == pc:
        print('Ничья')
    elif (user == 'камень' and pc == 'ножницы') or \
         (user == 'ножницы' and pc == 'бумага') or \
         (user == 'бумага' and pc == 'камень'):
        print('Вы выиграли')
        player += 1
    else:
        print('Компьютер выиграл')
        pc_count += 1
    
    
    print('Вы: ', '-', player, 'Компьютер', '-', pc_count)
    if player == 3 or pc_count == 3:
        break

