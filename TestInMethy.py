def Authorisation():
    Login, Password = "test", "test"
    Input_Login = str(input("Введите логин: "))
    Input_Password = str(input("Введите пароль: "))
    if Input_Login == Login and Input_Password == Password:
        print()
        print("Вы успешно вошли в аккаунт!")
        print()
    else:
        print("Login or password is wrong")
        exit()
def EasyCalculator():
    Cash = int(input("Введите количесто денег котрые хотите внести в наш банк: "))
    Procents = int(input("Введите процент под котрый хотите внести деньги в наш банк: "))
    Time = int(input("На какой срок вклад?(месяцев)"))
    One_procent = Cash / 100
    CashWithProcents = Cash + ((One_procent * Procents) * (Time / 12))
    print(CashWithProcents)
def HardCalculator():
    Cash = int(input("Введите количесто денег котрые хотите внести в наш банк: "))
    Procents = int(input("Введите процент под котрый хотите внести деньги в наш банк: "))
    Time = int(input("На какой срок вклад?(месяцев)"))
    AllCash = Cash
    for i in range(Time):
        AllCash = AllCash + (AllCash / 100) * (Procents / 12)
    print('Мы положили', Cash, 'на', Time, 'месяцев')
    print('В результате получим:', AllCash)
def Menu():
    print('1. Рассчитать простой процент')
    print('2. Рассчитать сложный процент')
    print('3. Выйти')
    Choose = int(input())
    print()
    if Choose == 1:
        EasyCalculator()
    if Choose == 2:
        HardCalculator()
    if Choose == 3:
        exit()

Authorisation()
Menu()