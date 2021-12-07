import csv


FILE_NAME = 'uiklist_2021_09_19_ЦИК_России_Выборы_депутатов_Государственной_Думы.tsv'


def read_tsv_from_csv(file_name):
    with open(file_name, 'r', encoding='utf8') as file_tsv:
        return list(csv.reader(file_tsv, delimiter='\t'))


def read_tsv(file_name):
    # print(file_name)
    with open(file_name, 'r', encoding='utf8') as file_tsv:
        return file_tsv.readlines()

def print_content(my_list,methode):
    if methode==1:
        methode_str="Метод 1"
    elif methode==2:
        methode_str="метод 2"
    else: 
        print("неизвестный метод")
        return

    for line in my_list:
        if methode==1:
            new_line=line.split('\t')
    else:
        new_line=line
    print(methode_str,new_line,sep='\t')
        

def main():
    file_tsv_content = read_tsv(FILE_NAME)
    print_content(file_tsv_content[1:2],1)
    # for line in file_tsv_content[1:2]:
    #     # print(line.strip().split('\t'))
    #     line_strip_split = line.strip().split('\t')
    #     print('Метод 1 (ручное чтение)',
    #         line_strip_split[0],
    #         line_strip_split[4],
    #         line_strip_split[-4],
    #         line_strip_split[-3],
    #         sep='\t'
    #     )
    
    file_tsv_from_csv_content = read_tsv_from_csv(FILE_NAME)
    print_content(file_tsv_from_csv_content[1:2],2)

    # print(file_tsv_from_csv_content)
    # for line in file_tsv_from_csv_content[1:2]:
    #     print('Метод 2 (чтение csv)', line[0], line[4], line[-4], line[-3], sep='\t')


if __name__ == '__main__':
    main()
