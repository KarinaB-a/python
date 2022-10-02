# Задача 5: Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
def input_point(name):
    point = input(f'Введите координаты точки через пробел {name} ').split(' ')
    return int(point[0]),int(point[1])
a = input_point('a')
b = input_point('b')

def count_distance(a,b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5

result = count_distance(a,b)
print(f'Расстояние между {a} и {b} = {result}')







