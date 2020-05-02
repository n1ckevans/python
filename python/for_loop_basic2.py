#1) Biggie Size
def biggie_size(my_list = []):
    for x in range(0, len(my_list), 1):
        if (my_list[x] > 0):
            my_list[x] = "big"
        print(my_list[x])

#2) Count Positives
def count_positives(my_list = []):
    count = 0
    for x in range(0, len(my_list), 1):
       if (my_list[x] > 0):
           count += 1
    my_list.pop()
    my_list.append(count)
    return my_list

#3) Sum Total
def sum_total(myList = []):
    sum = 0
    for x in range(0,len(myList), 1):
        sum += myList[x]
    return sum

#4) Average
def average(myList = []):
    sum = 0
    for x in range(0,len(myList), 1):
        sum += myList[x]
    return (sum/len(myList))

#5) Length
def length(myList = []):
    length_list = len(myList)
    return length_list

#6) Minimum
def minimum(myList = []):
    if (len(myList) == 0):
        return False
    min = myList[0]
    for x in range(1, len(myList), 1):
        if (myList[x] < min):
            min = myList[x]
    return min

#7) Maximum
def maximum(myList = []):
    if (len(myList) == 0):
        return False
    max = myList[0]
    for x in range(1, len(myList), 1):
        if (myList[x] > max):
            max = myList[x]   
    return max

#8) Ultimate Analysis 
def ultimate_analysis(my_list = []):
    length = len(my_list)
    sumTotal = my_list[0]
    minimum = my_list[0]
    maximum = my_list[0]
    for x in range(1, len(my_list), 1):
        if (my_list[x] > maximum):
            maximum = my_list[x]
        elif (my_list[x] < minimum):
            minimum = my_list[x]
            sumTotal += my_list[x]
    average = sumTotal/length
    d={'sumTotal': sumTotal,'average': average, 'minimum' : minimum, 'maximum' : maximum, 'length' : length}
    return(d)

#9)  Reverse List
def reverse_list(input_list): 
   for item in range(len(input_list)//2): 
        input_list[item], input_list[len(input_list)-1-item] = input_list[len(input_list)-1-item], input_list[item]
   return input_list