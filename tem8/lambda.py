#lambda arguments: expression

add = lambda x, y: x + y
print(add(5, 3))  # Виведе 8

# У прикладі ми створили лямбда-функцію add, яка повертає суму 
# двох чисел. Насправді це "поганий тон" зберігати лямбда-функції 
# у змінних, вони повинні створюватися там, де будуть 
# використовуватися і більше ніде у коді не залишають слідів

#print((lambda x, y: x + y)(5, 3))  # Виведе 8

# Лямбда-функції часто використовуються як аргументи для функцій 
# вищого порядку, таких як map(), filter() або sorted(). 
# Наприклад зворотне сортування списку для sorted():

nums = [1, 2, 3, 4, 5]
nums_sorted = sorted(nums, key=lambda x: -x)
print(nums_sorted) #[5, 4, 3, 2, 1]


