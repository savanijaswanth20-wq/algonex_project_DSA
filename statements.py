#An if statement is a decision-making statement in Python. It executes a block of code only if the specified condition is True.
for i in range(1, 6):
    print(i)

students = ["Rahul", "Jaswanth", "Anil", "Priya"]

for student in students:
    print(student)    
name = "Python"

for letter in name:
    print(letter)

count = 1
while count <= 5:
    print(count)
    count += 1

for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)    

for i in range(1, 11):
    if i == 6:
        break
    print(i)

#pass statement   
for i in range(1, 4):
    if i == 2:
        pass
    print(i)