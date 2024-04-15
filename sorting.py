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

def selection_sort(cisla,direction):
    #první for cyklus si pamatuje indexy čísel
    for i in range (len(cisla)):
        min_index = i
        #druhý for cyklus si pamatuje minimum
        if direction == "vzestupně":
            for j in range(min_index+1, len(cisla)):
                if cisla[j]< cisla[min_index]:
                    min_index = j
        elif direction == "sestupně":
            for j in range(min_index+1, len(cisla)):
                if cisla[j]> cisla[min_index]:
                    min_index = j
        #prohození čísel
        cisla[i], cisla[min_index] = cisla[min_index], cisla [i]
    return cisla

def bubble_sort(numbers):
    for i in range(len(numbers)):
        for j in range(0, len(numbers)-i-1):
            if numbers[j]>numbers[j+1]:
                numbers[j], numbers[j+1]=numbers[j+1],numbers[j]
    return numbers

def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]

        j = i - 1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = key
    return data


def main():
    data=read_data("numbers.csv")
    print(data)
    sort = selection_sort(data["series_3"],direction="vzestupně")
    print(sort)
    sort2=bubble_sort(data["series_3"])
    print(sort2)
    sort3=insertion_sort(data["series_3"])
    print(sort3)


if __name__ == '__main__':
    main()
