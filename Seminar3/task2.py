'''2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
Пример:
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
'''
def multiply_numbers(numbers):
    result = []
    for i in range(0,int((len(numbers)+1)/2)):
        result.append(numbers[len(numbers) - 1 - i] * numbers[i])
    return result

# numbers = [3,9,55,9,3,2,6,0]
numbers = [3,9,55,9,7,3,2,6,0]
print(multiply_numbers(numbers))




