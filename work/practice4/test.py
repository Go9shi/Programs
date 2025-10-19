from datetime import datetime, date
from decimal import Decimal 


goods = {
    'Яйца' : [{'amount' : Decimal(10), 'expiration_date' : datetime.strptime('08.09.2023', '%m.%d.%Y').date()}],
    'Сыр' : [{'amount' : Decimal(0), 'expiration date' : datetime.strptime('06.09.2021', '%m.%d.%Y')}],
}
title = ['Яйца', 'Масло сливочное', 'Сыр пармезан', 'Вода']


def add(eats):
    lst = []
    eat = input('Добавьте продукт в холодильник: ')
    for item in title:
        if eat == item:
            goods[item].append({
            'amount' : Decimal(int(input('Введите количество/объем: '))),
            'expiration_date' : datetime.strptime(input('Введите дату изготовления (мм.дд.гггг): '), '%m.%d.%Y').date(),
            })
            return goods
        else:
            goods[eat] = [{
            'amount' : Decimal(int(input('Введите количество/объем: '))),
            'expiration_date' : datetime.strptime(input('Введите дату изготовления (мм.дд.гггг): '), '%m.%d.%Y').date()
            }]
            return goods
def find(item):
    lst = []
    for item in goods:
        lst.append(item)
    return lst

def amount(title):
    total = Decimal('0')
    for t in find(title):
        for batch in goods[t]:
            total += batch['amount']
    return total               
print(amount(goods))
print(find(goods))
print(add(goods))
