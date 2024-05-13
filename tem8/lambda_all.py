# Функція all() є вбудованою функцією, яка повертає True, 
# якщо всі елементи в переданому їй об'єкті ітерації є 
# істинними - тобто не False, 0, "", None або будь-яке 
# інше значення, яке Python оцінює як хибне. Але будьте уважні, 
# якщо об'єкт ітерації порожній, функція all() повертає True.

# Наприклад перевірка, чи всі елементи у списку істинні?
nums = [1, 2, 3, 4]
result = all(nums)  
print(result) #True

# Чи всі елементи списку є парними?
nums = [1, 2, 3, 4]
is_all_even = all(x % 2 == 0 for x in nums) 
print(is_all_even) #False

# Чи всі слова у списку мають велику початкову букву?

words = ["Hello", "World", "Python"]
is_all_title_case = all(word.istitle() for word in words)
print(is_all_title_case) #True




