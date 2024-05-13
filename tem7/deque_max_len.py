from collections import deque

d = deque(maxlen=5)
for i in range(10):
    d.append(i)

print(d)
