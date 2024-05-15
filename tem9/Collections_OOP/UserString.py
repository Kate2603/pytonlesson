# Останнім розглянемо UserString який є класом, аналогічним до UserList, 
# але для рядків. Він дозволяє створювати класи, які наслідують поведінку 
# звичайного рядка, з можливістю додавання нових методів або зміни 
# стандартної поведінки рядків. Це корисно, коли вам потрібно 
# працювати з рядками спеціалізованим чином, який не 
# підтримується стандартними рядками Python.

# Розглянемо наступний приклад:
from collections import UserString

# Створення класу, який розширює UserString
class MyString(UserString):
    # Додавання методу, який перевіряє, чи рядок є паліндромом
    def is_palindrome(self):
        return self.data == self.data[::-1]

# Створення екземпляру MyString
my_string = MyString("radar")
print("Рядок:", my_string)
print("Чи є паліндромом?", my_string.is_palindrome())

# Створення іншого екземпляру MyString
another_string = MyString("hello")
print("Рядок:", another_string)
print("Чи є паліндромом?", another_string.is_palindrome())

# Рядок: radar
# Чи є паліндромом? True
# Рядок: hello
# Чи є паліндромом? False

# Останній приклад показує модифікований рядок з методом truncate, 
# який обмежує розмір рядка до MAX_LEN символів.
from collections import UserString

class TruncatedString(UserString):
    MAX_LEN = 7

    def truncate(self):
        self.data = self.data[:self.MAX_LEN]

ts = TruncatedString('hello world!')
ts.truncate()
print(ts) #hello w
