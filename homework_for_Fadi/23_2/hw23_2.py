"""
Програма мінімум:
Реалізувати алгоритм бінарного пошуку за допомогою рекурсії.
"""

print("\nTASK ONE\n")


# low - index of start of subarray
# high - index of last item of subarray
# arr - [1, 2, 3, 4, 5, 6, 7, 8]
# subarray(start, end) -> subarray(0, 2) -> [1, 2] || subarray(5, 6) -> [6]
# binary_search(arr, 0, len(arr) - 1, 5)
# binary_search(arr, 4, len(arr) - 1, 5)

def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2

        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)

        elif arr[mid] < x:
            return binary_search(arr, mid + 1, high, x)

    else:
        return False


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binary_search(arr, 0, len(arr) - 1, 7))

"""
Прочитати про Fibonacci search та імплементуйте його за допомогою Python.
Визначте складність алгоритму та порівняйте його з бінарним пошуком

Similarities with Binary Search:  
- Works for sorted arrays
- A Divide and Conquer Algorithm.
- Has Log n time complexity.

Differences with Binary Search: 
- Fibonacci Search divides given array into unequal parts
- Binary Search uses a division operator to divide range. Fibonacci Search doesn’t use /, but uses + and -. 
  The division operator may be costly on some CPUs.
- Fibonacci Search examines relatively closer elements in subsequent steps. So when the input array is big that cannot 
  fit in CPU cache or even in RAM, Fibonacci Search can be useful.
"""

# [10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100]
# arr(len) = 11
# X = 85
# fibM = 13, fibMm1 = 8, fibMm2 = 5, offset = 0, index = (offset + min(fibM, fibMm1, fibMm2)) = 5
# arr[5] = X? arr[5] = 45 != 85

# якщо значення менше - ресет офсет = індекс, значення фіб змінюються на -1

# fibM = 8, fibMm1 = 5, fibMm2 = 3, offset = 5, index = 8
# arr[8] = X? arr[8] = 82 != 85
# fibM = 5, fibMm1 = 3, fibMm2 = 2, offset = 8, index = 10
# arr[10] = X? arr[10] = 90 != 85

# якщо значення більше - офсет не міняється, значення фіб змінюються на -2

# fibM = 2, fibMm1 = 1, fibMm2 = 1, offset = 8, index = 9
# arr[9] = X? arr[9] = 85 == 85

print("\nTASK TWO\n")


def fibMonaccianSearch(arr, x, n):
    fibMMm2 = 0
    fibMMm1 = 1
    fibM = fibMMm2 + fibMMm1

    # 0 1 1 -> 1 1 2 -> 1 2 3 -> 2 3 5 -> 3 5 8 -> 5 8 13
    while fibM < n:
        fibMMm2 = fibMMm1  # 5
        fibMMm1 = fibM  # 8
        fibM = fibMMm2 + fibMMm1  # 13

    offset = -1

    while fibM > 1:
        i = min(offset + fibMMm2, n - 1)  # 10, 10

        if arr[i] < x:
            fibM = fibMMm1  # 3
            fibMMm1 = fibMMm2  # 2
            fibMMm2 = fibM - fibMMm1  # 1
            offset = i  # 9
        elif arr[i] > x:
            fibM = fibMMm2  # 1
            fibMMm1 = fibMMm1 - fibMMm2  # 1
            fibMMm2 = fibM - fibMMm1  # 0
        else:
            return i

    if fibMMm1 and arr[n - 1] == x:
        return n - 1

    return False


arr = [10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100]
n = len(arr)
x = 85
ind = fibMonaccianSearch(arr, x, n)

if ind >= 0:
    print("Found at index:", ind)
else:
    print(x, "isn't present in the array")

"""
Середній рівень:

 use hash function? or just:
 print(len(dictionary.values()))
print(None in dictionary.values())

Реалізувати in (__contains__) та len (__len__) методи для HashTable
"""

print("\nTASK THREE\n")

# Hashtable: key-value pairs
dictionary = {"key": ["value1", 'value2'], "1": None}
for key in dictionary.keys():
    print(dictionary.get(key))

print(len(dictionary.values()))
print(None in dictionary.values())
