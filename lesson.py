message = "Never argue with stupid people, they will drag you down to their level and then beat you with experience."
search = "r"
result = 0
for symbol in message:
    if symbol == "r": 
        result += 1
        continue
    
print(result)