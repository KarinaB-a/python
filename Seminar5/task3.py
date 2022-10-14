'''Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.'''
def rle_encode(data):
    encoding = ''
    prev_char = ''
    count = 1
    if not data:
        return ''
    for char in data:
        if char != prev_char:
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    encoding += str(count) + prev_char
    return encoding
def rle_decode(data):
    decode = ''
    count = ''
    for char in data:
        if str(char).isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ''
    return decode
decoded_val = rle_decode('6F8H7y')
print(decoded_val)
with open('decode.txt','w') as file:
    file.write(f'{decoded_val}')
with open ('encode.txt','r') as file:
    readfile = file.read()
encoded_val = rle_encode(readfile)
print(encoded_val)