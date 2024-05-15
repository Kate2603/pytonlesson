# UserDict — це клас, що міститься в модулі collections і 
# слугує обгорткою навколо словника. Він дозволяє легше 
# створювати власні класи словників, модифікуючи або додаючи 
# нову поведінку до стандартних методів словника.

from collections import UserDict

class MyDictionary(UserDict):
    # Приклад додавання нового методу
    def add_key(self, key, value):
        self.data[key] = value

# Створення екземпляра власного класу
my_dict = MyDictionary({'a': 1, 'b': 2})
my_dict.add_key('c', 3)
print(my_dict) #{'a': 1, 'b': 2, 'c': 3}

