'''Задача: предложить улучшения кода для уже решённых задач с помощью использования лямбд, filter, map, zip, enumerate, list comprehension.'''

'''map, enumerate, lambda'''

'''5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
Пример:
для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи'''

n = int(input('Введите число '))

numbers = [0,1]
for i in range(2, n + 1):
    numbers.append(numbers[i - 1] + numbers [i - 2])

not_numbers = list(map(lambda p: p[1] * (-1)**p[0], enumerate(numbers[1:])))

not_numbers.reverse()
print (not_numbers + numbers)