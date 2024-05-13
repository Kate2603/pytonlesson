def add(a, b):
    return a + b


def add(a):
    def add_b(b):
        return a + b
    return add_b

# Використання:
add_5 = add(5)
result = add_5(10)
print(result)


def apply_discount(price: float, discount_percentage: int) -> float:
    return price * (1 - discount_percentage / 100)

# Використання
discounted_price = apply_discount(500, 10)  # Знижка 10% на ціну 500
print(discounted_price)

discounted_price = apply_discount(500, 20)  # Знижка 20% на ціну 500
print(discounted_price)
