#1) Update Values in Dictionaries and Lists
x = [ [5,2,3], [15,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Bryant'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Andres', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 30} ]

#2) Iterate Through a List of Dictionaries
def iterateDictionary(students):
    for item in students:
         print(item)

#3) Get Values From a List of Dictionaries
def iterateDictionary2(key_name, some_list):
    for item in some_list:
        print(item[key_name])

#4) Iterate Through a Dictionary with List Values
def printInfo(some_dict):
    for key, value in some_dict.items():
        print(len(value), key, value)