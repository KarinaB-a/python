'''Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
Пример:
- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)'''
def kit_multiplitation_numbers(n):
    result = []
    for i in range(1, n + 1):
        if i == 1:
            result.append(i) 
        else:
            result.append(result[i - 2] * i) 
    return result
n = int(input('Введите число n = '))
print(n)
print(kit_multiplitation_numbers(n))