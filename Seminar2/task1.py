''' 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
Пример:
- 6782 -> 23
- 0,56 -> 11 '''

def sum_numbers(n):
    s = 0
    a = int(n * 100000000000) 
    a = abs(a) # модуль
    while a > 0:
        s = a % 10 + s
        a = a // 10
    return s
n = float(input('Введите вещественное число n = '))

print(n)

print(sum_numbers(n))