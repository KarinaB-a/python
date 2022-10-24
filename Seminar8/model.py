'''Задача: Доделать информационную систему позволяющую работать с сотрудниками некой компании \ студентами вуза \ учениками школы.'''
# surname,name,patronymic,group,performance,final_grades,awards,promotion_to_the_next_group
# Внутренний вид данных
data = [
    {
        "id": "Идентификатор_ученика_1",
        "name": "Имя_1",
        "surname": "Фамилия_1", 
        "patronymic": "Отчество_1",
        "group": "Класс_1",
        "performance": "Успеваемость_1",
        "final_grades": "Итоговая оценка_1",
        "awards": "Награждение_1_для_выпускника",
        "promotion_to_the_next_group": "Перевод_в_следующий_класс_или_выпуск_1"
    }
]

def read_format_lines(path, fields):
    '''Прочитать файл формата:

    Идентификатор_ученика_1
    Имя_1
    Фамилия_1
    Отчество_1
    Класс_1
    Успеваемость_1
    Итоговая оценка_1
    Награждение_1_для_выпускника
    Перевод_в_следующий_класс_или_выпуск_1

    path -- путь к файлу

    вернет data внутренний вид
    '''
    data = []
    with open (path, "r") as f:
        lines = list(f)
        for i in range(0, len(lines), len(fields)+1):
            item = {}
            count = 0
            for field in fields:
                item[field] = lines[i + count].strip()
                count += 1
            data.append(item)
    return data
    
def write_format_lines(data, path):
    '''
    Записать файл формата:

    Идентификатор_ученика_1
    Имя_1
    Фамилия_1
    Отчество_1
    Класс_1
    Успеваемость_1
    Итоговая оценка_1
    Награждение_1_для_выпускника
    Перевод_в_следующий_класс_или_выпуск_1

    data -- данные, которые нужно записать
    path -- путь, куда записать

    '''
    sep = "\n"
    with open (path, 'w') as f:
        for item in data:
            f.write(f"{sep.join(item.values())}\n\n")

def read_format_csv(path, fields, sep = ','):
    '''
    Прочитать файл формата:
    
    Идентификатор_ученика_1, Имя_1, Фамилия_1, Отчество_1, Класс_1, Успеваемость_1, Итоговая оценка_1, Награждение_1_для_выпускника, Перевод_в_следующий_класс_или_выпуск_1

    path -- путь к файлу

    '''
    data = []
    with open (path, "r") as f:
        for line in f:
            s = line.split(sep)
            item = {}
            count = 0
            for field in fields:
                item[field] = s[count].strip()
                count += 1
            data.append(item)
    return data

def write_format_csv(data, path, sep = ','):
    '''
    Записать файл формата:

    Идентификатор_ученика_1, Имя_1, Фамилия_1, Отчество_1, Класс_1, Успеваемость_1, Итоговая оценка_1, Награждение_1_для_выпускника, Перевод_в_следующий_класс_или_выпуск_1

    data -- данные, которые нужно записать
    path -- путь, куда записать
    sep -- разделитель, значение по умолчанию ","

    '''
    with open (path, 'w') as f:
        for item in data:
            f.write(f"{sep.join(map(str,item.values()))}\n")
           



