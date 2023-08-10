
visitors = int(input('Введите количество поситителей '))

tic = 0

for i in range(visitors):
    age = int(input('Введите возраст посетителя '))
    if age < 18:
        tic = tic + 0
    elif 18 <= age <= 25:
        tic = tic + 990
    else:
        25 < age
        tic = tic + 1390
if visitors > 3:
    tic = tic - (tic * 0.1)
print(f'Сумма к оплате составляет {tic}')

