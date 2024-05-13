#[new_item for item in iterable if condition]

sq = [x**2 for x in range(1, 6)]
print(sq) # Виведе [1, 4, 9, 16, 25]

even_squares = [x**2 for x in range(1, 10) if x % 2 == 0]
print(even_squares) # Виведе [4, 16, 36, 64]


even_squares = []
for x in range(1, 10):
    if x % 2 == 0:
        even_squares.append(x**2)

print(even_squares)  # Виведе [4, 16, 36, 64]
