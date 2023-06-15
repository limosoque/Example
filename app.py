from binary_search import binary_search

help = "Запустить программу: 1", "Завершить программу: 2", "Справка: 3"
command = 1
print(help)
while True:
    command = int(input())
    if command == 2:
        break
    if command == 1:
        print("Введите через пробел числа, среди которых будет производиться поиск")
        arr = [int(x) for x in input().split()]
        print("Введите через пробел числа, которые хотите найти")
        find = [int(x) for x in input().split()]
        for to_find in find:
            print(to_find, "в" if binary_search(arr, to_find) else "не в", "массиве")
    else:
        print(help)
        continue
