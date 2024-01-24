import random

def partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


try:
    input_list = input("Введіть список цілих чисел (числа через кому): ")
    my_list = [int(num) for num in input_list.split(',')]
except ValueError:
    print("Некоректний ввід для списку.")
    exit()

print("Не відсортований список:", my_list)

quick_sort(my_list, 0, len(my_list) - 1)

print("Відсортований список методом швидкого сортування:", my_list)
