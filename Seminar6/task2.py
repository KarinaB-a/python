'''Задача: предложить улучшения кода для уже решённых задач с помощью использования лямбд, filter, map, zip, enumerate, list comprehension.'''

'''filter'''

'''Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.'''

lst = [4, 5, 7, 83, 21, 50, 0, 5, 21]
def f(item):
    return len(list(filter(lambda x: x == item, lst))) == 1
result = list(filter(f, lst))
print(result)