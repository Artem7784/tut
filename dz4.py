# дан словарь, создать новый слловарь, поменяв местами ключ и значение
#
# sales = {'apple': 2, 'orange': 4, 'grapes': 6}
# new_sales = {value: key for key, value in sales.items()}
# print(sales)
# print(new_sales)


# n = int(input('Введите число:'))
# summ = 1
# for i in range(1, n+1):
#     summ = summ * i
#     print('Факториал числа равно:', summ)


# Вычеслить факториал числа n

# def factorial(n):
#     if n < 2:
#         return 1
#     return n * factorial(n - 1)
# n = int(input('Введите число:'))
# print(factorial(n))


Дан список чисел. Посчитать сколько раз встречается каждое число.

# def count_duplicates(lst):
#     counts = {}  # Создаем пустой словарь для подсчета повторений
#     for item in lst:
#         if item in counts:
#             counts[item] += 1  # Увеличиваем значение для существующего элемента
#         else:
#             counts[item] = 1  # Добавляем новый элемент в словарь с начальным значением 1
#
#     return counts
#
# my_list = [1, 2, 3, 2, 4, 1, 5, 2, 1, 11, 11, 5]
# duplicates = count_duplicates(my_list)
# for item, count in duplicates.items():
#     if count > 1:
#         print(f"Элемент {item} повторяется {count} раз(а).")