# Асоціація поділяється на два основних типи: композиція та агрегація, 
# кожен з яких має свої особливості та застосування.

# Агрегація - це тип відношення між об'єктами, яке також представляє 
# відносини "ціле" до "частини", але в цьому випадку "частини" можуть 
# існувати незалежно від "цілого". Це означає, що якщо "ціле" буде знищено, 
# "частини" можуть продовжувати існувати самостійно. Агрегація вказує на 
# більш слабку залежність між об'єктами і часто використовується, 
# коли об'єкти можуть входити до складу різних груп або колекцій. 
# Наприклад, бібліотека (ціле) може містити книги (частини) через 
# агрегацію; якщо бібліотека закриється, книги все одно залишаться 
# і можуть бути переміщені до іншої бібліотеки.

# Розглянемо приклад, який ілюструє, чому наслідування не є найкращим рішенням, 
# і як асоціація між цими класами через агрегацію є більш відповідним підходом.

# Спочатку розглянемо ситуацію, де ми могли б неправильно вирішити використати 
# наслідування. Маємо клас Owner для господаря кішки та клас Cat для самої кішки.

# class Owner:
#     def __init__(self, name, phone):
#         self.name = name
#         self.phone = phone

#     def info(self):
#         return f"{self.name}: {self.phone}"

# class Cat(Owner):
#     def __init__(self, nickname, age, name, phone):
#         super().__init__(name, phone)
#         self.nickname = nickname
#         self.age = age

#     def cat_info(self):
#         return f"Cat Name: {self.nickname}, Age: {self.age}"
        
#     def sound(self):
#         return "Meow"

# cat = Cat('Simon', 4, 'Boris', '+380503002010')
# print(cat.info())
# print(cat.cat_info())

# Boris: +380503002010
# Cat Name: Simon, Age: 4

# Натомість, ми повинні показати, що кішка "має" господаря. 
# Це не робить кішку господарем. Просто означає, що між кішкою 
# та людиною є зв'язок. Людина - це господар кішки, 
# а кішка - це вихованець цієї людини.

class Owner:
    def __init__(self, name: str, phone: str):
        self.name = name
        self.phone = phone

    def info(self):
        return f"{self.name}: {self.phone}"

class Cat(Owner):
    def __init__(self, nickname: str, age: int, owner: Owner):
        self.nickname = nickname
        self.age = age
        self.owner = owner

    def get_info(self):
        return f"Cat Name: {self.nickname}, Age: {self.age}"

    def sound(self):
        return "Meow"

owner = Owner("Boris", "+380503002010")
cat = Cat("Simon", 4, owner)
print(cat.owner.info())
print(cat.get_info())
# Boris: +380503002010
# Cat Name: Simon, Age: 4