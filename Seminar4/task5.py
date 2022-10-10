'''Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.'''
def read_m(path):
    f = open(path,'r')
    data = f.read()
    f.close()
    return data
def parse_m(data):
    m = {}
    parts = str(data).replace(' = 0','').split('+')
    # print(parts)
    for p in parts:
        a = p.split('*')
        b = p.split('^')
        if len(a) == 2:
            k = int(a[0])
        elif 'x' in p:
            k = 1
        else:
            k = int(p) # коэф
        if len(b) == 2:
            d = int(b[1]) # cтепень
        elif 'x' in p:
            d = 1
        else:
            d = 0
        m[d] = k
        # print(a, b)
    return m
data1 = read_m('m1.txt')
data2 = read_m('m2.txt')
print(data1)
print(data2)
m1 = parse_m(data1)
# print(parse_m(data1))
m2 = parse_m(data2)
for i in m1.keys():
    if i in m2.keys():
        m2[i] = m1[i] + m2[i]
    else:
        m2[i] = m1[i] 
print(m2)
result = []
for i in m2.keys():
    if m2[i] != 0:
        if i == 0:
            result.append(f'{m2[i]}')
        elif i == 1:
            result.append(f'{m2[i]}*x')
        else:
            result.append(f'{m2[i]}*x^{i}')
with open ('t5.txt', 'w') as data:
    data.write(" + ".join(result) + " = 0")    


