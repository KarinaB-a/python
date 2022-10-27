'''"final_grades": "Итоговая оценка_1"'''

import string

from typing import List
import uuid


def add_final_grades(db, id, performance, final_grades):
    "отлично"
    "хорошо"
    "удовлетворительно"
    "не_удовлетворительно"
    grades = ["отлично","хорошо","удовлетворительно","не_удовлетворительно"]
    for item in db:
        if item["id"] == id:
            item["performance"] = grades[performance]
            item["final_grades"] = grades[final_grades]
            return item

def add_awards(db):
    '''
    Награждение_1_для_выпускника
    '''
    for item in db:
        if item["final_grades"] == "отлично" and item["promotion_to_the_next_group"] == "выпуск":
            item ["awards"] = "Золотая медаль"
        if item["final_grades"] == "хорошо" and item["promotion_to_the_next_group"] == "выпуск":
            item ["awards"] = "Серебряная медаль"

def add_promotion_to_the_next_group(db):
    '''
    Перевод_в_следующий_класс_или_выпуск_1
    '''
    for item in db:
        if item["final_grades"] in ["отлично", "хорошо", "удовлетворительно"]:
            num = str(item["group"]).replace(' класс', '')
            if int(num) == 11:
                item ["promotion_to_the_next_group"] = "выпуск"
            else:
                item ["promotion_to_the_next_group"] = f'{int(num) + 1} класс'
        else:
            item ["promotion_to_the_next_group"] = "остается на следующий год в том же классе"

def add_new_student(db, name, surname, patronymic, group):
    '''
    Функция создания нового студента.

    db -- хранилище
    name
    surname
    patronymic
    group
    
    Вернет id нового студента
    '''
    
    id = uuid.uuid4()
    db.append(dict(
        id = id, name = name, surname = surname, patronymic = patronymic,
        group = group,  performance = "",  final_grades = "",  awards = "",  promotion_to_the_next_group = ""
    ))
    return id

def delete_student(db: List, id: string):
    '''
    удалить студента
    db - данные
    id - идентификатор
    '''
    for item in db:
        if item["id"] == id:
            db.remove(item)
            return item
    

def update_student(db: List, id: string, name = '', surname = '', patronymic = ''):
    '''
    обновить студента
    db - данные
    id - идентификатор
    '''
    for item in db:
        if item["id"] == id:
            if name:
                item["name"] = name
            if surname:
                item["surname"] = surname
            if patronymic:
                item["patronymic"] = patronymic
            return item


            