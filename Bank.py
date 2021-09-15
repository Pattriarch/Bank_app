import logging.config
from logger_for_bank import logger_config
from art import logo
from func_and_dict import Bank

logging.config.dictConfig(logger_config)

logger = logging.getLogger('app_logger')

# Словари
users = {}
users_money = {}
container = {}

# Флаги
in_account = True
start_program = True
first_start = True
user_is_acting = False
continue_program = False
name_of_user = ''
flagging = ''
flagger = ''

# Вызов приложения bank
def program():
    # Получаем значение флага из глобальной области и если он равен истине, то
    # выводим наше представление
    global start_program
    if start_program:
        print("Добро пожаловать в приложение 'bank'!")
        logger.info('Вход в банк')
        start_program = False

    global continue_program
    if continue_program:
        print('Вы вернулись в главное меню, продолжайте пользоваться приложением.')
        logger.info('')
        logger.info('Возврат в главное меню банка')
        continue_program = False
    # Запрашиваем у пользователя действие, в зависимости от действия выполняем необходимую нам
    # функцию, далее запрашиваем имя пользователя и пароль пользователя
    what_to_do = input(f"Если вы хотите создать нового пользователя, то введите 'Создать', "
                       f"или если же хотите войти в аккаунт пользователя, то введите 'Войти'.\n")
    logger.info('Выбор между созданием и входом в аккаунт')

    if what_to_do.lower() == 'создать' or what_to_do.lower() == 'войти':
        pass
    else:
        print(f"Вы ввели неверную команду '{what_to_do}', повторите, пожалуйста, заново!")
        logger.info(f"Пользователь ввел неверную команду '{what_to_do}'")
        program()

    user_n = input('Введите логин пользователя: ')
    user_p = input('Введите пароль пользователя: ')

    # Создание пользователя и записываем его в словарь
    def create_user(user_name, user_password):
        users[user_name] = user_password
        users_money[user_name] = 0
        logger.info(f"Создание аккаунта с логином '{user_n}' и паролем '{user_p}'")

    # Если пользователь выбрал действие - 'Создать', то мы вызываем функцию создания
    # пользователя, уведомляем об этом пользователя и возвращаемся в начало программы
    if what_to_do.lower() == 'создать':
        logger.info("Пользователь создает аккаунт...")
        logger.info(f"Пользовать ввел логин '{user_n}'")
        logger.info(f"Пользовать ввел пароль '{user_p}'")
        # Проверка, если аккаунт с таким логином уже сущестует, то пользователь получит предупреждение об этом
        if user_n not in users.keys():
            create_user(user_name=user_n, user_password=user_p)
            print('Вы успешно создали новый аккаунт!')
            logger.info(f"Аккаунт с логином '{user_n}' и паролем '{user_p}' успешно создан")
        else:
            print('Аккаунт с таким логином уже существует, попробуйте создать другой аккаунт!')
            logger.info(f"Аккаунт с таким логином('{user_n}') уже существует")
        program()

    # Если пользователь выбрал действие - 'Войти', то мы проверяем, существует ли такая
    # комбинация логина и пароля
    elif what_to_do.lower() == 'войти':
        logger.info(f"Пользователь входит в аккаунт...")
        logger.info(f"Пользовать ввел логин '{user_n}'")
        logger.info(f"Пользовать ввел пароль '{user_p}'")
        if user_n in users.keys():
            if user_p in users.values():
                logger.info(f"Пользователь вошел в аккаунт с логином '{user_n}' и паролем '{user_p}'")
                print('Отлично, вы вошли в аккаунт!')
                # Записываем имя пользователя в name_of_user и обновляем флаги
                global name_of_user, in_account, user_is_acting
                name_of_user = user_n
                user_is_acting = True
                in_account = True
            else:
                logger.info(f"Пользователь ввел неверную комбинацию логин/пароль")
                print('Вы ввели неверную комбинацию логина/пароля.')
                program()
        else:
            logger.info(f"Пользователь ввел неверную комбинацию логин/пароль")
            print('Вы ввели неверную комбинацию логина/пароля.')
            program()

    else:
        logger.info(f"Пользователь ввел неверную комбинацию логин/пароль")
        print('Вы ввели неверную комбинацию логина/пароля.')
        program()


# Если программа запущена в первый раз, то запускаем её выполнение
if first_start:
    logger.info(f"Запуск программы")
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
            logger.info(f"Вход в меню банковского приложения пользователя с логином '{name_of_user}'")
            Class = Bank(container[name_of_user])
            choose = input(f"Вы находитесь в банковском приложении, для того, чтобы воспользоваться "
                           f"услугами выберите услугу 'Пополнить', 'Снять', 'Проверить баланс'.\n")
            if choose.lower() == 'проверить баланс':
                logger.info(f"Пользователь с логином '{name_of_user}' проверяет баланс")
                Class.check_balance()
            elif choose.lower() == 'пополнить' or choose.lower() == 'снять':
                val = int(input('Введите значение услуги: '))
                if choose.lower() == 'пополнить':
                    logger.info(f"Пользователь с логином '{name_of_user}' пополнил баланс на '{val}' рублей")
                    # Использование метода из класса Bank в модуле func_and_dict.py
                    value = Class.top_up_balance(val)
                    # Присваивание списку с именем и текущим балансом нового баланс
                    users_money[Class] = value
                else:
                    # Использование метода из класса Bank в модуле func_and_dict.py
                    logger.info(f"Пользователь с логином '{name_of_user}' снял с баланса '{val}' рублей")
                    value = Class.remove_from_balance(val)
                    # Присваивание списку с именем и текущим балансом нового баланс
                    users_money[Class] = value

            else:
                logger.info(f"Пользователь с логином '{name_of_user}' при выборе услуг выбрал "
                            f"неверную команду '{choose}'")
                print('Вы ввели неверную команду, повторите, пожалуйста, заново!')
                do_it()

            def check():
                if choose.lower() == 'пополнить' or choose.lower() == 'снять':
                    # Хэшируем наш результат в контейнер
                    logger.info(f"Хэширование результата услуги '{choose}' пользователя с логином '{name_of_user}' "
                                f"в контейнер")
                    container[name_of_user] = users_money[Class]
                else:
                    pass

            def ask_flagger():
                global flagger
                flagger = input("Вы хотите продолжить, то введите 'Продолжить', вернуться в базовое меню 'Меню' "
                                "или закрыть программу 'Закрыть'?\n")
            ask_flagger()

            if flagger.lower() == 'продолжить':
                logger.info(f"Пользователь с логином '{name_of_user}' продолжил пользоваться банковским приложением")
                check()
                do_it()
            elif flagger.lower() == 'меню':
                logger.info(f"Пользователь с логином '{name_of_user}' переходит в меню")
                check()
                global continue_program
                continue_program = True
                program()
            elif flagger.lower() == 'закрыть':
                logger.info(f"Пользователь с логином '{name_of_user}' закрыл банковское приложение")
                global in_account
                in_account = False
                print('Вы закрыли банковское приложение.')
            else:
                logger.info(f"Пользователь с логином '{name_of_user}' ввел неверное значение '{flagger}' при "
                            f"выборе команд с банковским приложением")
                print('Вы ввели неверное значение, повторите, пожалуйста, заново!')
                ask_flagger()

        else:
            logger.info(f"Вход в меню банковского приложения пользователя с логином '{name_of_user}'")
            Name = Bank(users_money[name_of_user])
            choose = input(f"Вы находитесь в банковском приложении, для того, чтобы воспользоваться "
                           f"услугами выберите услугу 'Пополнить', 'Снять', 'Проверить баланс'.\n")
            if choose.lower() == 'проверить баланс':
                logger.info(f"Пользователь с логином '{name_of_user}' проверяет баланс")
                Name.check_balance()
            elif choose.lower() == 'пополнить' or choose.lower() == 'снять':
                val = int(input('Введите значение услуги: '))
                if choose.lower() == 'пополнить':
                    logger.info(f"Пользователь с логином '{name_of_user}' пополнил баланс на '{val}' рублей")
                    value = Name.top_up_balance(val)
                    users_money[Name] = value
                else:
                    logger.info(f"Пользователь с логином '{name_of_user}' попробовал "
                                f"снять с баланса '{val}' рублей")
                    value = Name.remove_from_balance(val)
                    users_money[Name] = value
            else:
                logger.info(f"Пользователь с логином '{name_of_user}' при выборе услуг выбрал "
                            f"неверную команду '{choose}'")
                print('Вы ввели неверную команду, повторите, пожалуйста, заново!')
                do_it()

            def check():
                if choose.lower() == 'пополнить' or choose.lower() == 'снять':
                    logger.info(f"Хэширование результата услуги '{choose}' пользователя с логином '{name_of_user}' "
                                f"в контейнер")
                    container[name_of_user] = users_money[Name]
                else:
                    pass

            def ask_flagging():
                global flagging
                flagging = input("Вы хотите продолжить, то введите 'Продолжить', вернуться в базовое меню 'Меню' "
                                 "или закрыть программу 'Закрыть'?\n")
            ask_flagging()

            if flagging.lower() == 'продолжить':
                logger.info(f"Пользователь с логином '{name_of_user}' продолжил пользоваться банковским приложением")
                check()
                do_it()
            elif flagging.lower() == 'меню':
                logger.info(f"Пользователь с логином '{name_of_user}' переходит в меню")
                check()
                continue_program = True
                program()
            elif flagging.lower() == 'закрыть':
                logger.info(f"Пользователь с логином '{name_of_user}' закрыл банковское приложение")
                in_account = False
                print('Вы закрыли банковское приложение.')
            else:
                print('Вы ввели неверное значение, повторите, пожалуйста, заново!')
                logger.info(f"Пользователь с логином '{name_of_user}' ввел неверное значение '{flagging}' при "
                            f"выборе команд с банковским приложением")
                ask_flagging()
    do_it()
