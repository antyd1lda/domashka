def find_max_recursive(lst, n=None):
    if n is None:
        n = len(lst)

    if n == 1:
        return lst[0]

    max_of_rest = find_max_recursive(lst, n - 1)
    return max(lst[n - 1], max_of_rest)

test_list = [3, 41, 12, 9, 74, 15, 27, 6]
print(f"Список: {test_list}")
print(f"Наибольший элемент: {find_max_recursive(test_list)}")

print()

print("Рекурсивное разбиение числа")

def partition_number(n, max_value=None, current=[]):

    if max_value is None:
        max_value = n

    if n == 0:
        return [current[:]]

    if n < 0:
        return []

    result = []

    for i in range(1, min(n, max_value) + 1):
        current.append(i)
        result.extend(partition_number(n - i, i, current))
        current.pop()

    return result

number = 4
partitions = partition_number(number)
print(f"Все разбиения числа {number}:")
for i, partition in enumerate(partitions, 1):
    print(f"{i}. {partition} = {sum(partition)}")
print(f"\nВсего разбиений: {len(partitions)}")

print()