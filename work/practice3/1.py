from random import *

rd = randint(1, 100)
print(rd)

var1 = int(input('Введите загаданное число: '))
if var1 == rd:
    print('Вы угадали число!', rd)
else:
    if var1 > rd:
        print('Ваше число меньше')
    else:
        print('Ваше число больше')
    var2 = int(input('Введите число еще раз: '))
    if var2 == rd:
        print('Вы угадали число!', rd)
    else:
        if rd % 2 == 0:
            print('Ваше число четное')
        else:
            print('Ваше число нечетное')
        var3 = int(input('Введите число еще раз: '))
        if var3 == rd:
            print('Вы угадали число!', rd)
        else:
            print('Вы не угадали число')