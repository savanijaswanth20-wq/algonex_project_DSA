#Square Star Pattern
rows = 5

for i in range(rows):
    for j in range(rows):
        print("*", end=" ")
    print()

#Right Triangle Star Pattern
rows = 5
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()
#Inverted Triangle
rows = 5
for i in range(rows, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

#Pyramid Pattern    
rows = 5
for i in range(rows):
    print(" " * (rows - i - 1), end="")
    print("* " * (i + 1))

#Reverse Pyramid  
rows = 5
for i in range(rows, 0, -1):
    print(" " * (rows - i), end="")
    print("* " * i)  

