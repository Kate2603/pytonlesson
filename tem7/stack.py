# Створення стеку
def create_stack():
    return []

# Перевірка на порожнечу
def is_empty(stack):
    return len(stack) == 0

# Додавання елементу
def push(stack, item):
    stack.append(item)

# Вилучення елементу
def pop(stack):
    if not is_empty(stack):
        return stack.pop()
    else:
        print("Стек порожній")

# Перегляд верхнього елемента
def peek(stack):
    if not is_empty(stack):
        return stack[-1]
    else:
        print("Стек порожній")


stack = create_stack()
push(stack, 'a')
push(stack, 'b')
push(stack, 'c')

print(peek(stack))  # Виведе 'c'
print(pop(stack))  # Виведе 'c'

print(stack)

# Тепер стек містить ['a', 'b']. Якщо ми спробуємо знову переглянути 
# або видалити верхній елемент, ми отримаємо 'b'.
# Якщо ми продовжимо видаляти елементи, поки стек не стане порожнім, 
# а потім спробуємо ще раз видалити або переглянути верхній елемент, 
# обидві функції pop() та peek() виведуть повідомлення "Стек порожній".
# Стеки в програмуванні є ідеальними для задач, де потрібно відслідковувати 
# елементи в зворотному порядку. Наприклад, стеки застосовуються в управлінні 
# викликами функцій та в різноманітних алгоритмах.
