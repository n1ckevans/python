#1)
def countdown(num):
    for x in range(num, -1, -1):
        print(x)

#2)
def print_and_return(list = []):
    print(list[0])
    return list[1

#3)
def first_plus_length(list = []):
    sum = list[0] + len(list)
    return sum

#4)
def values_greater_than_second(list1 = []):
    if len(list1) < 2:
        return False
    list2=[]
    count=0
    for i in range(0,len(list1)-1, 1):
        if list1[i] > list1[i+1]:
            list2.append(list1[i])
            count += 1
    print (count)
    return list2

#5)
def length_and_value(int1, int2):
    myList = []
    for i in range(int1):
        myList.append(int2)
    return myList