import numpy as np

# 1. Створення масиву
arr = np.random.randint(-100, 101, 200)

print("Початковий масив:")
print(arr)

# 2. Фільтрація додатних чисел
positive_numbers = arr[arr > 0]

print("\nДодатні числа:")
print(positive_numbers)

# 3. Замінюємо від’ємні значення на 0
modified_arr = arr.copy()
modified_arr[modified_arr < 0] = 0

print("\nМасив після заміни від’ємних значень:")
print(modified_arr)

# 4. Середнє значення
average = np.mean(modified_arr)

print("\nСереднє значення:")
print(average)