#Приватні (Private) атрибути та методи

class Person:
    def __init__(self, name: str, age: int, is_active: bool, is_admin: bool):
        self.name = name
        self.age = age
        self._is_active = is_active
        self.__is_admin = is_admin

    def greeting(self):
        return f"Hi {self.name}"

    def is_active(self):
        return self._is_active

    def set_active(self, active: bool):
        self._is_active = active
        
    def set_is_admin(self, is_admin: bool):
        # Тут можна додати будь-яку логіку перевірки або обробки
        self.__is_admin = is_admin

p = Person("Boris", 34, True, False)
#print(p.__is_admin) #AttributeError: 'Person' object has no attribute '__is_admin'
p.set_is_admin(True)
print(p.get_is_admin()) #True