from binary_search import binary_search

print("Введите через пробел числа, среди которых будет производиться поиск")
arr = [int(x) for x in input().split()]
print("Введите через пробел числа, которые хотите найти")
find = [int(x) for x in input().split()]

for to_find in find:
    print(binary_search(arr, to_find))
