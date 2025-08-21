# # print("Hello, World!") 
# # # variable declaration, operatros, separators, datatypes, control structures, functions 

# # # duck typing in Python

# # num = 10
# # print(num)  
# # num = 11
# # print(num)  
# # num = 'abc'
# # print(num)
# # num = False
# # print(num)

# # # if num > 10 && num < 20 :
# # if num > 10 and num < 20 :
# #     print("num is 10")

# # datatypes in Python:
# # int, float, str, bool, list, tuple, set, dict

# # num = 10
# # print(type(num))  
# # num = 10.5
# # print(type(num))
# # num = 'abc'
# # print(type(num))
# # num = True
# # print(type(num))
# # num = [1, 2, 3]
# # print(type(num))
# # num = (1, 2, 3)
# # print(type(num))    
# # num = {1, 2, 3}
# # print(type(num))
# # num = {'a': 1, 'b': 2}

# # mutable = [1, 2, 3]
# # print(type(mutable))  # <class 'list'>
# # mutable[0] = 10
# # print(mutable)  # [10, 2, 3]

# myList = [1, 2, 3, 4, 5] # arrays in C++
# myList[0] = 10
# print(myList)  

# myDict = {
#   "id": 2,
#   "name": "Ervin Howell",
#   "username": "Antonette",
#   "email": "Shanna@melissa.tv",
#   "address": {
#     "street": "Victor Plains",
#     "suite": "Suite 879",
#     "city": "Wisokyburgh",
#     "zipcode": "90566-7771",
#     "geo": {
#       "lat": "-43.9509",
#       "lng": "-34.4618"
#     }
#   }
# }

# # print(myDict)

# myTuple = (1, 2, 3)
# # myTuple[0] = 10  # This will raise an error because tuples are immutable
# print(myTuple)
# myTuple = (11, 21, 31)
# print(myTuple)


# mySet = {1, 2, 3}
# print(mySet)  

# # functions in Python:
# def greet(name):
#     print(f"Hello, {name}!")

# greet("Sonu")

def addNums(num1, num2 = 5):
    # print( num1 + num2)  
    return num1 + num2

result = addNums(10)
print(result)  

def fun():
    print("This is a function without parameters")

fun(10)