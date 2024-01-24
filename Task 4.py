def pancake_sort(stack):
    n = len(stack)
    for i in range(n - 1, 0, -1):
        max_index = stack.index(max(stack[:i + 1]))

        if max_index != i:
            stack[:max_index + 1] = reversed(stack[:max_index + 1])
            stack[:i + 1] = reversed(stack[:i + 1])


try:
    input_stack = input("Введіть стос млинців (радіуси через кому): ")
    pancakes = [int(radius) for radius in input_stack.split(',')]
except ValueError:
    print("Некоректний ввід для стосу млинців.")
    exit()

print("Не відсортований стос млинців:", pancakes)
pancake_sort(pancakes)
print("Відсортований стос млинців:", pancakes)