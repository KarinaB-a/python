# Задача 2. Напишите программу для проверки истинности утверждения not(X or Y or Z) = not X and not Y and not Z.

def input_bool(msg):
    return input(msg).lower() in ['true', '1', 't', 'yes']
def check_assertion(X,Y,Z):
    left = not (X or Y or Z)
    right = not X and not Y and not Z
    result = left == right
    print(f'{X,Y,Z} {result}')
X = input_bool('Введите значение X ')
Y = input_bool('Введите значение Y ')
Z = input_bool('Введите значение Z ')   
check_assertion(X,Y,Z)






    
        
