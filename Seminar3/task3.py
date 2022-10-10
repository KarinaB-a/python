'''3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
Пример:
[1.1, 1.2, 3.1, 5, 10.01] => 0.19'''

def find_diffrence(numbers):
    min = 1
    max = 0
    for i in range(0,len(numbers)):
        fract = numbers[i] - int(numbers[i]) 
        if fract != 0:
            if max < fract:
                max = fract
            if min > fract:
                min = fract
    return round (max - min,3)
    
numbers = [1.1, 1.2, 3.1, 5, 10.01]
print(find_diffrence(numbers))