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

def make_dict_list(my_list):
    new_list =[]
    for line in my_list:
        new_dict={"Название": line[4], "Адресс":line[12], " Широта": line[-4],"Долгота": line[-3]}
        new_list.append(new_dict)



    return new_list  

def main():
    file_tsv_content = read_tsv(FILE_NAME)
    print_content(file_tsv_content[1:2],1)
    for line in file_tsv_content[1:2]:
     # print(line.strip().split('\t'))
        line_strip_split = line.strip().split('\t')
        print('Метод 1 (ручное чтение)',
            line_strip_split[0],
            line_strip_split[4],
            line_strip_split[-4],
            line_strip_split[-3],
            sep='\t'
        )
def search(my_list, find_str, index):
    new_list = []
    for line in my_list:
        if find_str.upper() in line[index].upper():
            new_list.append(line)
    return new_list

def read_tsv_from_csv(file):
    with open(file, 'r', encoding='utf8') as file_tsv:
        return list(csv.reader(file_tsv, delimiter='\t'))

def print_content(my_list, method):
    for line in my_list:
        print(
            method, 
            line[0],
            line[4],
            line[-4],
            line[-3], 
            sep=', \t')
            
def make_dict(my_list):
    new_list = []
    return new_list   
    file_tsv_from_csv_content = read_tsv_from_csv(FILE_NAME)
    print_content(file_tsv_from_csv_content[1:2],2)

    # print(file_tsv_from_csv_content)
    # for line in file_tsv_from_csv_content[1:2]:
    #     print('Метод 2 (чтение csv)', line[0], line[4], line[-4], line[-3], sep='\t')


if __name__ == '__main__':
    main()
