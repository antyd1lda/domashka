list1 = [11, 25, 2, 37, 34]
list2 = "5 10 2 15 8"

def minIndex(data):
    return data.index(min(data))

def sortNumbers(numbers_string):
    list_numbers = numbers_string.split()
    return " ".join([str(num) for num in sorted([int(num) for num in list_numbers])])

print(f"""
Список: {list1}
Индекс минимального элемента: {minIndex(list1)}

Исходная строка: '{list2}'
Отсортированная строка: '{sortNumbers(list2)}'
""")