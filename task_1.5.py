a = int(input('Введите выручку фирмы:'))
b = int(input('Введите издержки фирмы:'))
if a > b:
    print('Фирма работает в прибыль')
else:
    print('Фирма работает в убыток')
p = int(a) / int(b)
r = int(input('Введите количество сотрудников:'))
rp = int(p) / int(r)
print(f'Прибыль на сотрудника: {rp:.3f}')