print('Привет, я калькулятор от Супрончика Артёма!')

while True:
    try:
        c = input('Что будем делать? +, -, *, /: ')
        a = int(input('Введите первое число: '))
        b = int(input('Введите второе число: '))

        if c == '+':
            result = a + b
        elif c == '-':
            result = a - b
        elif c == '*':
            result = a * b
        elif c == '/':
            if b != 0:
                result = a / b
            else:
                print('Деление на ноль невозможно!')
                continue
        else:
            print('Неизвестная операция')
            continue

        print(f'Результат: {result}')
    except ValueError:
        print('Ошибка: Введите корректные числа.')
    except Exception as e:
        print(f'Произошла ошибка: {e}')

    while True:
        x = input('Ещё раз? (y/n): ')
        if x == 'n':
            exit()
        elif x == 'y':
            break
        else:
            print('Некорректный ввод. Введите "y" для продолжения или "n" для выхода.')