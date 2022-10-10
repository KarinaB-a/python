'''4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
Пример:
- 45 -> 101101
- 3 -> 11
- 2 -> 10'''
def to_binary(n):
    result = ''
    while n > 0:
        result = str(n % 2) + result
        n = n // 2
    return result
n = int(input('Введите целое число '))
print(to_binary(n))
