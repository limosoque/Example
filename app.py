from binary_search import binary_search

help = "Запустить программу: 1", "\n", "Завершить программу: 2", "\n", "Справка: 3"
command = 1
print(help)
while True:
    command = int(input())
    if command == 2:
        break
    if command == 3:
        print(help)
        continue
    print("Введите через пробел числа, среди которых будет производиться поиск")
    arr = [int(x) for x in input().split()]
    print("Введите через пробел числа, которые хотите найти")
    find = [int(x) for x in input().split()]

    for to_find in find:
        print(to_find, "в " if binary_search(arr, to_find) else "не в ", "массиве")
