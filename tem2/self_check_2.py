################1

is_next = None
num = int(input("Enter the number of points: "))
if num >= 83:
    is_next = True
else: 
    is_next = False

################2

work_experience = int(input("Enter your full work experience in years: "))

if work_experience > 1 and work_experience <= 5 :
    developer_type = "Middle"
elif work_experience <= 1:
    developer_type = "Junior"
else :
    developer_type = "Senior"
print(work_experience)
print(developer_type)

################3

num = int(input("Enter a number: "))

if num > 0:
    if num % 2 == 1:
        result = "Positive odd number"
    else:
        result = "Positive even number"
elif num < 0:
    result = "Negative number"
else :
    result = "It is zero"
print(num)

################4


