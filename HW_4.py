'''
1. Вычислить число пи c заданной точностью *d*
    *Пример:*
    - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
'''
# from math import pi

# d = int(input('Введите число для заданной точности Пи:\n'))
# str = str(pi)
# lst = []
# for i in range(d + 2):
#     lst.append(str[i])

# my_pi = ''.join(lst)
# print(f'число Пи с заданной точностью {d} равно {my_pi}')

#ИЛИ

# from math import pi

# a =  int(input("Введите число для заданной точности Пи:\n"))
# print(f'число Пи с заданной точностью {a} равно {round(pi, a)}')



'''
2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
'''
# import math

# num = int(input('Введите натуральное число: '))
# result = []

# while num % 2 == 0:
#     result.append(2)
#     num /= 2

# for i in range(3, int(math.sqrt(num)) + 1, 2):
#     while num % i == 0:
#         result.append(i)
#         num /= i

# if num > 2:
#     result.append(num)

# print(f'Список простых множителей: ', end='')
# print(*result, sep=', ', end='.')

'''
3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся
элементов исходной последовательности.
1 2 2 1 3 4 5 6 6 7 4 -> 3 5 7
'''
# a = [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]
# new_list = []
# for i in range(len(a)):
#     for j in range(len(a)):
#         if i != j and a[i] == a[j]:
#             break
#     else:
#         new_list.append(a[i])
# print(new_list)

'''
4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
(значения от 0 до 100) многочлена и записать в файл многочлен степени k.

    *Пример:*

    - k=9 => 2*x^9 - 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
'''
# import itertools
# from random import randint

# print('Для формирования многочлена в степени а, введите степень a. ')
# a = int(input("Введите степень a: "))

# fact = []
# for i in range(1, a + 2):
#     fact.append(randint(1, 101))

# result = []
# for i in range(len(fact)):
#     if a == 1:
#         result.append(f'{fact[i]}*x')
#     elif a == 0:
#         result.append(f'{fact[i]}')
#     else:
#         result.append(f'{fact[i]}*x^{a}')
#     signs = randint(0, 1)
#     if signs == 1:
#         result.append('+')
#     elif signs == 0:
#         result.append('-')
#     a -= 1

# result.pop(-1)
# result.append('=0')

# record = open('new_file.txt', 'w')
# record.write(''.join(result))
# record.close()


'''
5. Даны два файла, в каждом из которых находится запись многочлена.
Задача - сформировать файл, содержащий сумму многочленов.

5x^2 + 3x - 9
3x^2 - 2x - 5

8x^2 + 1x - 14
'''