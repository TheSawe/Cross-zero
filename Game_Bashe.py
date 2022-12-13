n = int(input('Введите количество палочек: '))
player1 = input('Введите имя первого игрока: ')
player2 = input('Введите мя второго игрока: ')
step = False
print()

print('|' * n, end=' ')
print()
print()
while True:
    if n != 0:
        if not step:
            print(f'Ход игрока {player1}: ')
            wood = int(input('Введите количество палочек, которые хотите убрать(от 1 до 3): '))
            if wood > 3 or wood <= 0:
                print('Я просил ввести цифру от 1 до 3:')
            n -= wood
            if n == 0:
                break
            print(f'Осталось {n} палочек: ')
            print('|' * n, end=' ')
            print()
            print()
            step = not step
        else:
            print(f'Ход игрока {player2}: ')
            wood = int(input('Введите количество палочек, которые хотите убрать(от 1 до 3): '))
            if wood > 3 or wood <= 0:
                print('Я просил ввести цифру от 1 до 3')
            n -= wood
            if n == 0:
                break
            print(f'Осталось {n} палочек: ')
            print('|' * n, end=' ')
            print()
            print()
            step = not step
print()
print(f'Молодец')
