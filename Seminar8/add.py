'''"final_grades": "Итоговая оценка_1"'''



import uuid


def add_final_grades(db, id, value):
    "отлично"
    "хорошо"
    "удовлетворительно"
    "не_удовлетворительно"
    grades = ["отлично","хорошо","удовлетворительно","не_удовлетворительно"]


    pass

def add_awards(db, id, value):
    ...

def add_promotion_to_the_next_group(db, id, value):
    ...

def add_new_student(db, name, surname, patronymic):
    '''
    Функция создания нового студента.

    db -- хранилище
    name
    surname
    patronymic
    
    Вернет id нового студента
    '''
    
    id = uuid.uuid4()
    db.append(dict(
        id = id, name = name, surname = surname, patronymic = patronymic,
        group = "",  performance = "",  final_grades = "",  awards = "",  promotion_to_the_next_group = ""
    ))
    return id