'''Задание в группах: Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.
- под форматами понимаем структуру файлов, например: в файле на одной строке хранится одна часть записи, разделитель - пустая строка.
в файле на одной строке хранится все записи, символ разделитель - ",":
Фамилия_1,Имя_1,Телефон_1,Описание_1
Фамилия_2,Имя_2,Телефон_2,Описание_2
и т.д.'''
# surname,name,telephone,description
# Внутренний вид данных
data = [
    {
        "surname": "Фамилия_1", 
        'name': "Имя_1",
        "phone": "Телефон_1",
        "description": "Описание_1"
    },
    {
        "surname": "Фамилия_2", 
        'name': "Имя_2",
        "phone": "Телефон_2",
        "description": "Описание_2"
    },
]

def read_format_lines(path):
    '''Прочитать файл формата:

    Фамилия_1
    Имя_1
    Телефон_1
    Описание_1

    Фамилия_2
    Имя_2
    Телефон_2
    Описание_2

    path -- путь к файлу

    вернет data внутренний вид
    '''
    data = []
    with open (path, "r") as f:
        lines = list(f)
        for i in range(0, len(lines), 5):
            data.append({
                "surname": lines[i].strip(), 
                'name': lines[i+1].strip(),
                "phone": lines[i+2].strip(),
                "description": lines[i+3].strip()
            })
    return data
    
def write_format_lines(data, path):
    '''
    Записать файл формата:

    Фамилия_1
    Имя_1
    Телефон_1
    Описание_1

    Фамилия_2
    Имя_2
    Телефон_2
    Описание_2
    data -- данные, которые нужно записать
    path -- путь, куда записать

    '''
    sep = "\n"
    with open (path, 'w') as f:
        for item in data:
            f.write(f"{sep.join(item.values())}\n\n")
            # f.write(f"{item['surname']}\n")
            # f.write(f"{item['name']}\n")
            # f.write(f"{item['phone']}\n")
            # f.write(f"{item['description']}\n\n")

def read_format_csv(path, sep = ','):
    '''
    Прочитать файл формата:

    Фамилия_1,Имя_1,Телефон_1,Описание_1
    Фамилия_2,Имя_2,Телефон_2,Описание_2

    path -- путь к файлу

    '''
    data = []
    with open (path, "r") as f:
        for line in f:
            s = line.split(sep)
            data.append({
                "surname": s[0],
                'name': s[1],
                "phone": s[2],
                "description": s[3].strip()
            })
    return data

def write_format_csv(data, path, sep = ','):
    '''
    Записать файл формата:

    Фамилия_1,Имя_1,Телефон_1,Описание_1
    Фамилия_2,Имя_2,Телефон_2,Описание_2

    data -- данные, которые нужно записать
    path -- путь, куда записать
    sep -- разделитель, значение по умолчанию ","

    '''
    with open (path, 'w') as f:
        for item in data:
            f.write(f"{sep.join(item.values())}\n")
            # f.write(f"{item['surname']}{sep}")
            # f.write(f"{item['name']}{sep}")
            # f.write(f"{item['phone']}{sep}")
            # f.write(f"{item['description']}\n")



