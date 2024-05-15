# Класи даних

# Модуль dataclasses в Python надає засіб для декларативного 
# визначення класів, які переважно використовуються для зберігання даних. 
# Цей модуль введений у Python 3.7, щоб спростити створення таких класів 
# без необхідності ручного написання бойлерплейт (від англ. - boilerplate) 
# коду, який часто повторюється у традиційних класах.

# Модуль надає декоратор класу @dataclass який спрощує створення класів 
# для зберігання даних. Традиційно, коли ми створюємо клас для зберігання 
# даних, нам потрібно вручну визначити метод як-от __init__() 
# для ініціалізації атрибутів, магічні методи для представлення 
# об'єкта у зрозумілому форматі або для порівняння об'єктів. 
# Декоратор @dataclass автоматизує цей процес, дозволяючи нам 
# оголосити атрибути класу і автоматично генеруючи ці методи. 
# Це робить код чистішим, менш вразливим до помилок і легшим для 
# підтримки. З магічними методами ми детально познайомимося в наступному розділі.

# ☝ Використання @dataclass дозволяє зменшити кількість коду, 
# необхідного для створення класів, які в основному зберігають дані. 
# Це робить код більш читабельним і легшим для розуміння, а також 
# автоматично створює конструктор класу __init__.

# Базовий приклад синтаксису @dataclass виглядає наступним чином:

# from dataclasses import dataclass

# @dataclass
# class ExampleClass:
#     attribute1: type
#     attribute2: type = default_value


# Традиційно, якщо вам потрібно створити клас для зберігання даних, 
# ви б мали б вручну визначити метод __init__ для ініціалізації атрибутів.
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

# У цьому прикладі для створення простого класу Person, 
# який зберігає ім'я та вік особи, ми визначили метод __init__ для ініціалізації атрибутів.

# Якщо використати декоратор @dataclass, ми можемо автоматизувати створення класу, значно спростивши код.
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

# У цьому прикладі @dataclass автоматично генерує метод __init__
# а інші магічні методи, на основі оголошених атрибутів. Ми отримуємо 
# той самий функціонал, що й у попередньому прикладі, але з меншою 
# кількістю коду та меншою ймовірністю помилок, 
# пов'язаних з ручним визначенням методів.

# ☝ Перевага використання @dataclass полягає у тому, 
# що він автоматизує багато рутинних задач, пов'язаних із 
# створенням класів, які зберігають дані.

# В наступному прикладі клас Article містить атрибути зі 
# стандартними значеннями. Це корисно, коли деякі поля мають 
# звичайні значення, які не вимагають вказівки при кожному створенні об'єкта:

@dataclass
class Article:
    title: str
    author: str
    views: int = 0