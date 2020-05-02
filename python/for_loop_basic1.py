#1)
for x in range (0, 151, 1):
    print(x)

#2)
for x in range (5, 1001, 5):
    print(x)

#3)
for x in range (1, 101, 1):
    if (x % 10 == 0):
        print("Coding Dojo")
    elif (x % 5 == 0):
        print("Coding")
    else:
       print(x)

#4)
sum = 0
for x in range (0, 500001):
    if (x == 0 or x % 2 == 1):
        print(x)
        sum += x   
print(sum)

#5)
y = 2018
while y > 0:
    print(y)
    y -= 4

#6)
for lowNum in range (lowNum, highNum+1, 1):
    if (lowNum % mult == 0):
        print(lowNum)