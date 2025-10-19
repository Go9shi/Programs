import random


def create(a):
    b = 0
    ID_create = random.randint(1000_0000_0000_0000,9999_9999_9999_9999)
    res = b + ID_create
    return res
def add(a):
    b = balance
    res = b + adding
    return res
def deduction(a):
    b = balance
    res = b - diff
    return res
def check(a):
    b = balance
    return b
ID = 0
password = '0000'
print('Добрый день! Выполните вход в аккаунт')
balance = 0
acc = 0
if ID != 0:
    logup = input('Введите пароль: (Подсказка: 0000): ')
    if password == logup:
        success_login = input('Добро пожаловать! Выберите действие: ')
        pick = input('Пополнение - 1, Списание - 2, Проверка баланса - 3: ')
        if pick == '1':
            adding = int(input('Выберите сумму пополнения: '))
            print('Успешно! Ваш баланс:', add(balance))
        if pick == '2':
            diff = int(input('Выберите сумму списания: '))
            if balance > diff:
                print('Успешно! Ваш баланс:', deduction(balance))
            else:
                print('Ошибка списания, проверьте счет')
        if pick == '3':
            print('Ваш баланс:', check(balance))
    else:
        print('Неправильный пароль')
else:
    account = input('Вы не зарегестрированы! Создать новый счет? | Да\Нет: ')
    if account == 'Да':
        pay_system = input('Выберите платежную систему: (Visa, Mastercard, Мир)')
        print('Успешно! Ваш номер счета:', create(acc))
        print('Добрый день! Выполните вход в аккаунт')
        logup = input('Введите пароль: (Подсказка: 0000): ')
        if password == logup:
            success_login = input('Добро пожаловать! Выберите действие: ')
            pick = input('Пополнение - 1, Списание - 2, Проверка баланса - 3: ')
            if pick == '1':
                adding = int(input('Выберите сумму пополнения: '))
                print('Успешно! Ваш баланс:', add(balance))
            if pick == '2':
                diff = int(input('Выберите сумму списания: '))
                if balance > diff:
                    print('Успешно! Ваш баланс:', deduction(balance))
                else:
                    print('Ошибка списания, проверьте счет')
            if pick == '3':
                print('Ваш баланс:', check(balance))
    else:
        print('Закрытие программы...')
            


            
        




    ID_create = random.randint(1000_0000_0000_0000,9999_9999_9999_9999)