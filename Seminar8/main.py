from add import add_new_student, delete_student, update_student, add_final_grades, add_promotion_to_the_next_group, add_awards
from model import read_format_csv, write_format_csv

fields = ["id",  "name",  "surname",  "patronymic",  "group",  "performance",  "final_grades",  "awards",  "promotion_to_the_next_group"]

db_path = './Seminar8/db.txt'

if __name__=='__main__':
    #пустая база(автоматическая чистка)
    write_format_csv({}, db_path)
    
    # data = read_format_lines('./Seminar8/lines.txt', fields)
    # write_format_lines(data, './Seminar8/lines_out.txt')
    db = read_format_csv(db_path, fields)

    id1 = add_new_student(db, "Петр", "Николаев", "Сергеевич", "1 класс")
    id2 = add_new_student(db, "Светлана", "Заворотнюк", "Алексеевна", "3 класс")
    id3 = add_new_student(db, "Максим", "Дудкин", "Матвеевич", "8 класс")
    id4 = add_new_student(db, "Лера", "Зеленеева", "Константиновна", "11 класс")

    delete_student(db, id1)
    updated = update_student(db, id3, "name", "surname", "patronimic" )
    print(updated)
    add_final_grades(db, id2, 3, 1)
    add_final_grades(db, id3, 2, 3)
    add_final_grades(db, id4, 0, 0)

    add_promotion_to_the_next_group(db)
    add_awards(db)
    
    write_format_csv(db, db_path)

   