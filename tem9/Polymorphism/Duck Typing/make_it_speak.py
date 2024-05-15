# # У Python можна використовувати статичну типізацію для анотації 
# # типів і одночасно покладатися на качину типізацію для 
# # поліморфізму та гнучкої поведінки об'єктів.

# # Розглянемо наступний приклад:

# class Dog:
#     def speak(self) -> str:
#         return "Woof"

# class Cat:
#     def speak(self) -> str:
#         return "Meow"

# class Robot:
#     def speak(self) -> str:
#         return "Beep boop"

# def make_it_speak(speaker) -> None:
#     # У цьому прикладі, качина типізація дозволяє нам передавати 
#     # будь-який об'єкт, який має метод speak, у функцію make_it_speak, 
#     # не зважаючи на його конкретний клас. Але, що стосується 
#     # типу параметру speaker для функції make_it_speak?
#     print(speaker.speak())

# dog = Dog()
# cat = Cat()
# robot = Robot()

# make_it_speak(dog)  # Виведе: Woof
# make_it_speak(cat)  # Виведе: Meow
# make_it_speak(robot)  # Виведе: Beep boop


# У цьому прикладі, качина типізація дозволяє нам передавати 
# будь-який об'єкт, який має метод speak, у функцію make_it_speak, 
# не зважаючи на його конкретний клас. Але, що стосується типу 
# параметру speaker для функції make_it_speak?

# Щоб занотувати тип параметра функції speaker ми можемо 
# використати typing.Protocol, який визначає набір методів, 
# які цей параметр має виконувати, не прив'язуючись до конкретного класу.

# Створимо інтерфейс, використовуючи typing.Protocol, 
# для об'єктів, які можуть "говорити". Ми хочемо, щоб будь-який об'єкт, 
# який має метод speak, вважався сумісним з цим інтерфейсом.

from typing import Protocol

class Speaker(Protocol):
    def speak(self) -> str:
        pass

class Dog:
    def speak(self) -> str:
        return "Woof"

class Cat:
    def speak(self) -> str:
        return "Meow"

class Robot:
    def speak(self) -> str:
        return "Beep boop"

def make_it_speak(speaker: Speaker) -> None:
    print(speaker.speak())

dog = Dog()
cat = Cat()
robot = Robot()

make_it_speak(dog)  # Виведе: Woof
make_it_speak(cat)  # Виведе: Meow
make_it_speak(robot)  # Виведе: Beep boop
