import os
import csv


def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        data={}
        for row in reader:
            for header, value in row.items():
                if header not in data:
                    data[header] = [int(value)]
                else:
                    data[header].append(int(value))
    return data

def selection_sort(cisla):
    #první for cyklus si pamatuje indexy čísel
    for i in range (len(cisla)):
        min_index = i
        #druhý for cyklus si pamatuje minimum
        for j in range(min_index+1, len(cisla)):
            if cisla[j]< cisla[min_index]:
                min_index = j
        #prohození čísel
        cisla[i], cisla[min_index] = cisla[min_index], cisla [i]
    return cisla

def main():
    data=read_data("numbers.csv")
    print(data)
    sort = selection_sort(data["series_3"])
    print(sort)


if __name__ == '__main__':
    main()
