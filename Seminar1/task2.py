# Задача 2. Напишите программу для проверки истинности утверждения not(X or Y or Z) = not X and not Y and not Z.

def check_assertion(x,y,z):
    left = not (x or y or z)
    right = not x and not y and not z
    result = left == right
    print(f'{x,y,z} {result}')
for x in range(0,2):
    for y in range(0,2):
        for z in range(0,2):
            check_assertion(x,y,z)








    
        
