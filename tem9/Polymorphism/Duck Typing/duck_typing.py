# Качина типізація (Duck Typing) - це концепція в програмуванні, 
# яка відіграє важливу роль в динамічно типізованих мовах, 
# таких як Python. Назва походить від англійського вислову 
# "Якщо це ходить як качка і крякає як качка, то це, ймовірно, качка".

# У контексті програмування, качина типізація означає, що замість 
# перевірки типу об'єкта перед його використанням, важливіше 
# зосередитися на тому, чи має об'єкт потрібні методи чи властивості, 
# які вимагаються для виконання певної функції або операції.

# Механізм Python дозволяє використовувати будь-які об'єкти 
# один замість іншого, аби в обох були потрібні методи та поля. 
# Інтерпретатор не перевіряє, що у функцію або метод був переданий 
# об'єкт потрібного або дочірнього класу, достатньо 
# щоб в об'єкта були потрібні методи і все буде працювати.

class Duck:
    def quack(self):
        print("Quack, quack!")

class Person:
    def quack(self):
        print("I'm Quacking Like a Duck!")

def make_it_quack(duck):
    duck.quack()

duck = Duck()
person = Person()

make_it_quack(duck)
make_it_quack(person)

# Quack, quack!
# I'm Quacking Like a Duck!