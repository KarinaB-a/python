'''Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.'''
import random
def fill_list_numbers(n):
    positions = []
    path = 'file.txt'
    data = open(path, 'r')
    for line in data:
        positions.append(int(line))
    data.close()
    d = 1
    numbers = []
    for i in range(n):
        numbers.append(random.randint(-n, n))
        if i in positions:
            d = d * numbers[i]
    print (numbers) 
    return d
n = int(input('Введите число n = '))
print(n)
print(fill_list_numbers(n))