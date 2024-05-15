# Композиція - це тип відношення між об'єктами, де один об'єкт є частиною іншого. 
# У відношенні композиції "частина" не може існувати без "цілого". Це означає, 
# що якщо "ціле" буде знищено або видалено, то "частина" також буде знищена або видалена.

# Композиція ефективно використовується в ситуаціях, де об'єкти мають сильну 
# залежність один від одного, і "частина" не може існувати без "цілого". 
# Тобто, якщо один об'єкт володіє іншим об'єктом і відповідальний за його 
# життєвий цикл, то між ними існує відношення композиції.

# Уявімо, що ми розробляємо програмне забезпечення для управління проектами. 
# У цій системі кожен "Проект" (клас Project), може містити кілька "Задач" (клас Task), 
# і ці задачі не мають сенсу поза контекстом свого проекту. Якщо проект видаляється, 
# то всі його задачі також повинні бути видалені.

# Розглянемо реалізацію
class Task:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def display_info(self):
        print(f"Задача: {self.name}, Опис: {self.description}")

class Project:
    def __init__(self, name: str):
        self.name = name
        self.tasks: list(Task) = []

    def add_task(self, name: str, description: str):
        self.tasks.append(Task(name, description))

    def remove_task(self, name: str):
        self.tasks = [task for task in self.tasks if task.name != name]

    def display_project_info(self):
        print(f"Проект: {self.name}")
        for task in self.tasks:
            task.display_info()

# Створення проекту
my_project = Project("Веб-розробка")

# Додавання задач
my_project.add_task("Дизайн інтерфейсу", "Створити макет головної сторінки.")
my_project.add_task("Розробка API", "Реалізувати ендпоінти для користувачів.")

# Відображення інформації про проект
my_project.display_project_info()

# Видалення задачі
my_project.remove_task("Розробка API")

# Перевірка видалення задачі
my_project.display_project_info()

# Проект: Веб-розробка
# Задача: Дизайн інтерфейсу, Опис: Створити макет головної сторінки. 
# Задача: Розробка API, Опис: Реалізувати ендпоінти для користувачів.
# Проект: Веб-розробка
# Задача: Дизайн інтерфейсу, Опис: Створити макет головної сторінки.


# ☝ Композиція є ідеальним вибором для моделювання відносин, де існує 
# сильна залежність між об'єктами, і "частини" не можуть існувати 
# самостійно без "цілого". Вона забезпечує чітку структуру володіння 
# та керування об'єктами, підтримуючи цілісність та консистенцію системи.