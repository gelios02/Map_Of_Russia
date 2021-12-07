import csv
import folium
from folium.plugins import MarkerCluster

FILE_NAME = 'uiklist_2021_09_19_ЦИК_России_Выборы_депутатов_Государственной_Думы.tsv'


def make_map(my_list):
    start_coord = (55.03019, 82.92043)
    my_map = folium.Map(location=start_coord, zoom_start=7)
    marker_cluster = MarkerCluster().add_to(my_map)
    count = 0
    sum_lat = 0
    sum_lon = 0

    for line in my_list:
        lat = line[-4]
        lon = line[-3]
        if lat != "" and lon != "":
            folium.Marker(location=[float(lat), float(lon)],
                          popup=line[12][:120]).add_to(marker_cluster)
            count=count+1; sum_lat=sum_lat + float(lat); sum_lon=sum_lon + float(lon)
    my_map.location=(sum_lat/count,sum_lon/count)
    my_map.save('map.html')


def read_tsv_from_csv(file_name):
    with open(file_name, 'r', encoding='utf8') as file_tsv:
        return list(csv.reader(file_tsv, delimiter='\t'))


def read_tsv(file_name):
    # print(file_name)
    with open(file_name, 'r', encoding='utf8') as file_tsv:
        return file_tsv.readlines()


def print_content(my_list, methode):
    if methode == 1:
        methode_str = "Метод 1"
    elif methode == 2:
        methode_str = "метод 2"
    else:
        print("неизвестный метод")
        return

    for line in my_list:
        if methode == 1:
            new_line = line.split('\t')
    else:
        new_line = line
    print(methode_str, new_line, sep='\t')


def make_dict_list(my_list):
    new_list = []
    for line in my_list:
        new_dict = {"Название": line[4], "Адресс": line[12], " Широта": line[-4], "Долгота": line[-3]}
        new_list.append(new_dict)

    return new_list


def main():
    file_content = read_tsv(FILE_NAME)
    print_content(file_content[1:2], method='Метод 1')

    file_content_from_tsv = read_tsv_from_csv(FILE_NAME)
    print_content(file_content_from_tsv[1:2], method='Метод 2')

    search_result = search(my_list=file_content_from_tsv, find_str='Новосибирская область', index=1)
    print(search_result[:50])
    print(f"Найдено {len(search_result)} Строк")

    make_map(search_result)


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
    print_content(file_tsv_from_csv_content[1:2], 2)

    # print(file_tsv_from_csv_content)
    # for line in file_tsv_from_csv_content[1:2]:
    #     print('Метод 2 (чтение csv)', line[0], line[4], line[-4], line[-3], sep='\t')


if __name__ == '__main__':
    main()
