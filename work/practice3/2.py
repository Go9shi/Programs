text = input('Введите вашу строку: ').lower()

alphabet1 = 'бвгджзйклмнпрстфхцчшщ'
alphabet2 = 'аеёиоуыэюя'
list1 = []
list2 = []
res = []
itog = []
for x in text:
    if x in alphabet1:
        list1.append(x)
    elif x in alphabet2:
        list2.append(x)
    if [x, text.count(x)] not in res:
        res.append([x, text.count(x)])
mx = 0
for i in range(len(res)):
    if res[i][1] > mx:
        mx = res[i][1]
k = 0
for i in range(len(res)):
    if res[i][1] == mx:
        k += 1
        if k == 3:
            print(res[i][0], res[i][1])