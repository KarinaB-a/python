'''Реализуйте алгоритм перемешивания списка.'''
import random
def fill_list_numbers(n):
    result = []
    ran = range(1, n + 1)
    numbers = list(ran)
    while len(numbers) > 0:
        i = random.randint(0, len(numbers) - 1)
        result.append(numbers[i])
        numbers.remove(numbers[i])
    return result
n = int(input('Введите число n = '))
print(n)
print(fill_list_numbers(n))