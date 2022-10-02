# Задача 1: Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Например 6 -> да, 7 -> да, 1 -> нет

def check_day(number):
    if number >=1 and number <= 5:
        print (f'{number} -> будний день')
    elif number >= 6 and number <= 7:
        print (f'{number} -> выходной день')
    else:
        print (f'{number} -> день недели не определен')

number = int (input ('Введите цифру: '))
check_day(number)