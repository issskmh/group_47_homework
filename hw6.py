n = 6
mas = [5, 7, 4, 3, 8, 2]
count = 0
for run in range(n-1):
    for i in range(n-1):
        print(F' Сейчас сравним {mas[i]} c {mas[i+1]}')
        if mas[i] > mas[i+1]:
            count += 1
            mas[i], mas[i+1] = mas[i+1], mas[i]
    print(*mas)
print(count)


def binary_search(lst, search_item):
    low = 0
    high = len(lst) - 1
    search_res = False

    while low <= high and not search_res:
        middle = (low + high) // 2
        guess = lst[middle]

        # Печать текущих значений
        print(f"Low: {low}, Hihg: {high}, Midle: {middle}, Guess: {guess}")

        if guess == search_item:
            search_res = True
            print(f"Element {search_item} found in index {middle}")
            return search_res
        if guess > search_item:
            high = middle - 1
        else:
            low = middle + 1

    print(f"Element {search_item} not found")
    return search_res


lst = [3, 5, 11, 12, 15, 23, 25, 34, 67, 86]
value = 3
result = binary_search(lst, value)
if result:
    print('Element found!')
else:
    print("Element not found")
