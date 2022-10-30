import sys
def moon_weight():
    kofficent = 0.165
    print('Введите ваш нынешний земной вес:')
    weight = int(sys.stdin.readline())
    print('Введите ежегодный прирост вашего веса:')
    velichina = int(sys.stdin.readline())
    print('Сколько вам лет?')
    age = int(sys.stdin.readline())
    result = round(weight * kofficent, 3)
    for i in range(age):
        print(f'{i + 1} --- {result}')
        weight += velichina


moon_weight()
x = 10


def return10():
    # global x
    return 10 + x


print(return10())


def add():
    a = 15

    def modify():
        global a
        a = 20

    print(a)


add()


