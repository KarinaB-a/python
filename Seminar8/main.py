from add import add_new_student, delete_student
from model import read_format_lines, write_format_lines, read_format_csv, write_format_csv

fields = ["id",  "name",  "surname",  "patronymic",  "group",  "performance",  "final_grades",  "awards",  "promotion_to_the_next_group"]

db_path = './Seminar8/db.txt'

if __name__=='__main__':
    
    # data = read_format_lines('./Seminar8/lines.txt', fields)
    # write_format_lines(data, './Seminar8/lines_out.txt')
    db = read_format_csv(db_path, fields)

    id1 = add_new_student(db, "Петр", "Николаев", "Сергеевич")
    id2 = add_new_student(db, "Светлана", "Заворотнюк", "Алексеевна")
    id3 = add_new_student(db, "Максим", "Дудкин", "Матвеевич")
    id4 = add_new_student(db, "Лера", "Зеленеева", "Константиновна")

    delete_student(db, id1)

    write_format_csv(db, db_path)

   