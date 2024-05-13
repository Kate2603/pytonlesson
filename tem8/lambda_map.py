# Функція map() є функцією вищого порядку, що означає, що вона 
# приймає іншу функцію як аргумент. map() використовується для 
# застосування заданої функції до кожного елемента об'єкта 
# ітерації, наприклад списку, та повертає ітератор, 
# який виробляє результати.

# Синтаксис:
# map(function, iterable, ...)

# function - функція, яку треба застосувати до кожного елемента в iterable.
# iterable - об'єкт ітерації (список, кортеж тощо), елементи якого будуть оброблятися function.


# Давайте напишемо за допомогою map генератор, який підносить числа із списку numbers до квадрату:
numbers = [1, 2, 3, 4, 5]

for i in map(lambda x: x ** 2, numbers):
    print(i)

# 1
# 4
# 9
# 16
# 25

#Якщо ми хочем отримати список, а не генератор то код можна записати так:
numbers = [1, 2, 3, 4, 5]

squared_nums = list(map(lambda x: x ** 2, numbers))
print(squared_nums) #[1, 4, 9, 16, 25]

#Можна застосувати map до декількох списків:
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
sum_nums = map(lambda x, y: x + y, nums1, nums2)

print(list(sum_nums)) #[5, 7, 9]

#Замість використання функції map():
numbers = [1, 2, 3, 4, 5]
squared_nums = list(map(lambda x: x ** 2, numbers))
print(squared_nums) #[1, 4, 9, 16, 25]

#Ми використаємо list comprehensions:
nums = [1, 2, 3, 4, 5]
squared_nums = [x * x for x in nums]
print(squared_nums) #[1, 4, 9, 16, 25]

#Для двох списків ми теж можемо використати list comprehensions допомоги функції zip
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
sum_nums = [x + y for x, y in zip(nums1, nums2)]
print(sum_nums)




