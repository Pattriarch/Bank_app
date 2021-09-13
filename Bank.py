import logging
from art import logo
from func_and_dict import Bank

# Словари и
users = {}
users_money = {}
container = {}
name_of_user = ''

# Флаги
in_account = True
user_is_acting = False
start_program = True
continue_program = False
first_start = True
flagging = ''
flagger = ''

# Вызов приложения bank
def program():
    # Получаем значение флага из глобальной области и если он равен истине, то
    # выводим наше представление
    global start_program
    if start_program:
        print("Добро пожаловать в приложение 'bank'!")
        start_program = False

    global continue_program
    if continue_program:
        print('Вы вернулись в главное меню, продолжайте пользоваться приложением.')
        continue_program = False
    # Запрашиваем у пользователя действие, в зависимости от действия выполняем необходимую нам
    # функцию, далее запрашиваем имя пользователя и пароль пользователя
    what_to_do = input(f"Если вы хотите создать нового пользователя, то введите 'Создать', "
                       f"или если же хотите войти в аккаунт пользователя, то введите 'Войти'.\n")

    if what_to_do.lower() == 'создать' or what_to_do.lower() == 'войти':
        pass
    else:
        print(f"Вы ввели неверную команду '{what_to_do}', повторите, пожалуйста, заново!")
        program()

    user_n = input('Введите логин пользователя: ')
    user_p = input('Введите пароль пользователя: ')

    # Создание пользователя и записываем его в словарь
    def create_user(user_name, user_password):
        users[user_name] = user_password
        users_money[user_name] = 0

    # Если пользователь выбрал действие - 'Создать', то мы вызываем функцию создания
    # пользователя, уведомляем об этом пользователя и возвращаемся в начало программы
    if what_to_do.lower() == 'создать':
        # Проверка, если аккаунт с таким логином уже сущестует, то пользователь получит предупреждение об этом
        if user_n not in users.keys():
            create_user(user_name=user_n, user_password=user_p)
            print('Вы успешно создали новый аккаунт!')
        else:
            print('Аккаунт с таким логином уже существует, попробуйте создать другой аккаунт!')
        program()

    # Если пользователь выбрал действие - 'Войти', то мы проверяем, существует ли такая
    # комбинация логина и пароля
    elif what_to_do.lower() == 'войти':
        if user_n in users.keys():
            if user_p in users.values():
                print('Отлично, вы вошли в аккаунт!')
                # Записываем имя пользователя в name_of_user и обновляем флаги
                global name_of_user, in_account, user_is_acting
                name_of_user = user_n
                user_is_acting = True
                in_account = True
            else:
                print('Вы ввели неверную комбинацию логина/пароля.')
                program()
        else:
            print('Вы ввели неверную комбинацию логина/пароля.')
            program()

    else:
        print('Вы ввели неверную комбинацию логина/пароля.')
        program()


# Если программа запущена в первый раз, то запускаем её выполнение
if first_start:
    print(logo)
    program()
    first_start = False

# Если мы вошли в аккаунт, то мы попадаем в интерфейс банковского приложения

while in_account:
    # Функция, выполняющая роль интерфейса банкового придожения
    def do_it():
        # Если наша функция уже участвовала в цикле, то она помещается в контейнер и здесь происходит проверка этого
        if name_of_user in container:
            # Создание класса типа Bank, который в аргумент принимает числовое значение баланса пользователя
            Class = Bank(container[name_of_user])
            choose = input(f"Вы находитесь в банковском приложении, для того, чтобы воспользоваться "
                           f"услугами выберите команду 'Пополнить', 'Снять', 'Проверить баланс'.\n")
            if choose.lower() == 'проверить баланс':
                Class.check_balance()
            elif choose.lower() == 'пополнить' or choose.lower() == 'снять':
                val = int(input('Введите значение услуги: '))
                if choose.lower() == 'пополнить':
                    # Использование метода из класса Bank в модуле func_and_dict.py
                    value = Class.top_up_balance(val)
                    # Присваивание списку с именем и текущим балансом нового баланс
                    users_money[Class] = value
                else:
                    # Использование метода из класса Bank в модуле func_and_dict.py
                    value = Class.remove_from_balance(val)
                    # Присваивание списку с именем и текущим балансом нового баланс
                    users_money[Class] = value
            else:
                print('Вы ввели неверную команду, повторите, пожалуйста, заново!')
                do_it()

            def check():
                if choose.lower() == 'пополнить' or choose.lower() == 'снять':
                    # Хэшируем наш результат в контейнер
                    container[name_of_user] = users_money[Class]
                else:
                    pass

            def ask_flagger():
                global flagger
                flagger = input("Вы хотите продолжить, то введите 'Продолжить', вернуться в базовое меню 'Меню' "
                                "или закрыть программу 'Закрыть'?\n")
            ask_flagger()

            if flagger.lower() == 'продолжить':
                check()
                do_it()
            elif flagger.lower() == 'меню':
                check()
                global continue_program
                continue_program = True
                program()
            elif flagger.lower() == 'закрыть':
                global in_account
                in_account = False
                print('Вы закрыли банковское приложение.')
            else:
                print('Вы ввели неверное значение, повторите, пожалуйста, заново!')
                ask_flagger()

        else:
            Name = Bank(users_money[name_of_user])
            choose = input(f"Вы находитесь в банковском приложении, для того, чтобы воспользоваться "
                           f"услугами выберите команду 'Пополнить', 'Снять', 'Проверить баланс'.\n")
            if choose.lower() == 'проверить баланс':
                Name.check_balance()
            elif choose.lower() == 'пополнить' or choose.lower() == 'снять':
                val = int(input('введите значение услуги: '))
                if choose.lower() == 'пополнить':
                    value = Name.top_up_balance(val)
                    users_money[Name] = value
                else:
                    value = Name.remove_from_balance(val)
                    users_money[Name] = value
            else:
                print('Вы ввели неверную команду, повторите, пожалуйста, заново!')
                do_it()

            def check():
                if choose.lower() == 'пополнить' or choose.lower() == 'снять':
                    container[name_of_user] = users_money[Name]
                else:
                    pass

            def ask_flagging():
                global flagging
                flagging = input("Вы хотите продолжить, то введите 'Продолжить', вернуться в базовое меню 'Меню' "
                                 "или закрыть программу 'Закрыть'?\n")
            ask_flagging()

            if flagging.lower() == 'продолжить':
                check()
                do_it()
            elif flagging.lower() == 'меню':
                check()
                continue_program = True
                program()
            elif flagging.lower() == 'закрыть':
                in_account = False
                print('Вы закрыли банковское приложение.')
            else:
                print('Вы ввели неверное значение, повторите, пожалуйста, заново!')
                ask_flagging()
    do_it()
