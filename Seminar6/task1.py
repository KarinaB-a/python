'''Задача: предложить улучшения кода для уже решённых задач с помощью использования лямбд, filter, map, zip, enumerate, list comprehension.'''

'''filter, map '''

'''Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.'''
import random
def fill_list_numbers(n):
    path = './Seminar6/file.txt'
    data = open(path, 'r')
    positions = [int(line) for line in data] # list comprehension
    data.close()
    d = 1
    numbers = [random.randint(-n, n) for i in range(n)] # list comprehension
    for i in range(n):
        if i in positions:
            d = d * numbers[i]
    print (numbers) 
    return d
n = int(input('Введите число n = '))
print(n)
print(fill_list_numbers(n))



