Login1 = 'TheSawe'
Password1 = 'Ice2010'
Login2 = 'TheOnly'
Password2 = 'Ice2013'
Login3 = 'TheSweetKey'
Password3 = 'Ice2015'

Enter_User_Login = input('Input login:')
Enter_User_Password = input('Input password:')
Enter_User_Login = Enter_User_Login.replace(' ', '')
Enter_User_Password = Enter_User_Password.replace(' ', '')

if (Enter_User_Login == Login1 and Enter_User_Password == Password1) or (Enter_User_Login == Login2 and
                                                                         Enter_User_Password == Password2) or \
        (Enter_User_Login == Login3 and Enter_User_Password == Password3):
    print('Здравствуйте, Вы готовы начать тест по математике?')
    YesOrNo = input('Введите:(Yes / No)')
    if YesOrNo == 'No':
        exit()
    if YesOrNo == 'Yes':
        ask = input(f'Вопрос 1\n\nВычислите:\n\n(270-5*34)/100=?\n')
        answer_1 = (270 - 5 * 34) / 100
        if ask == int(answer_1):
            print('Правильно!')
        elif ask != int(answer_1):
            print('Ты допустил ошибку!')
            exit()
else:
    print('Wrong login or password!')
    exit()
