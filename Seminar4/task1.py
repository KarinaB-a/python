'''Вычислить число c заданной точностью d
Пример:
при d = 0.001, π = 3.141 10^(-1) ≤ d ≤10^(-10)'''
import math
def print_pi_accuracy(d):
    a = 0
    while d < 1:
        d = d * 10
        a += 1
    return round(math.pi, a)  
d = float(input('Введите число d = '))
print(d)
print(print_pi_accuracy(d))