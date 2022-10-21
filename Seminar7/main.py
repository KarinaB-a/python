from model import read_format_lines, write_format_lines, read_format_csv, write_format_csv


if __name__=='__main__':
    data = read_format_lines('./Seminar7/lines.txt')
    write_format_lines(data, './Seminar7/lines_out.txt')
    data = read_format_csv('./Seminar7/csv.txt')
    write_format_csv(data, './Seminar7/csv_out.txt')