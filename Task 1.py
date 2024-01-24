def shell_sort(arr, steps):
    n = len(arr)

    for step in steps:
        for i in range(step, n):
            temp = arr[i]
            j = i
            while j >= step and arr[j - step] > temp:
                arr[j] = arr[j - step]
                j -= step
            arr[j] = temp


try:
    steps_input = input("Введіть набір кроків (числа через кому): ")
    steps = [int(step) for step in steps_input.split(',')]
except ValueError:
    print("Некоректний ввід для набору кроків.")
    exit()


try:
    input_list = input("Введіть список цілих чисел (числа через кому): ")
    my_list = [int(num) for num in input_list.split(',')]
except ValueError:
    print("Некоректний ввід для списку.")
    exit()

print("Не відсортований список:", my_list)
shell_sort(my_list, steps)
print("Відсортований список методом Шелла:", my_list)