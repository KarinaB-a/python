from model import read_format_lines, write_format_lines


if __name__=='__main__':
    data = read_format_lines('./Seminar7/lines.txt')
    write_format_lines(data, './Seminar7/lines_out.txt')