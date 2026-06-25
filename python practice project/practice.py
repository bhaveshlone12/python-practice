# print("Hello Mindcoders")

# bhavesh (use ctrl + / shortcut key)

'''are used for multi line comment'''

# print("Hello")
# print("how")
# print("are")
# print("you")
# print("Bhavesh")

# age = 21
# print("my age is", age)

# age = 4
# print("my age is", age)
# print(type(age))

# age = "four"                #string should be used in "" like "four"
# print("my age is", age)
# print(type(age))


# name = "Bhavesh"
# profession = "software developer"
# exprience = 10
# print("Hello, I am", name, ", I am a ", profession, "professionally. And I have Around ", exprience, "years of exprience with it!")


# x = 5
# print(x, type(x))
# x = "Hello World"
# print(x, type(x))
# x = 20
# print(x, type(x))
# x = 20.5
# print(x, type(x))
# x = 1j
# print(x, type(x))
# x = ["apple", "banana", "cherry"]
# print(x, type(x))
# x = ("apple", "banana", "cherry")
# print(x, type(x))
# x = range(6)
# print(x, type(x))
# x = {"name" : "jhon", "age" : 36}
# print(x, type(x))
# x = {"apple", "banana", "cherry"}
# print(x, type(x))
# x = frozenset({"apple", "banana", "cherry"})
# print(x, type(x))
# x = True
# print(x, type(x))
# x = b"Hello"
# print(x, type(x))
# x = bytearray(5)
# print(x, type(x))
# x = memoryview(bytes(5))
# print(x, type(x))
# x = None
# print(x, type(x))


                # operators

# print("10 + 2 = ", 10 + 2)
# print("10 - 2 = ", 10 - 2)
# print("10 * 2 = ", 10 * 2)
# print("10 / 2 = ", 10 / 2)
# print("8 % 4 = ", 9 % 5)
# print("10 // 3 = ", 10 // 3)
# print("2 ** 3 = ", 2 ** 3)

# '''
#     x       y       x & y         #and operation
#     0       0       0
#     1       0       0
#     0       1       0
#     1       1       1

#     x       y       x | y         #or operation
#     0       0       0
#     1       0       1
#     0       1       1
#     1       1       1

# 0010 1010   => 5
# 1100 1101   => 2
# ---------
# 0000 1000
# '''

# print(5 & 3)

                #compuond operators
# x = 5
# # print(x)
# # x += 3
# # print(x)
# # x -= 2
# # print(x)

# # x *= 3
# # print(x)

# x /= 2
# print (x)

# x //= 3
# print (x)

# x **= 2
# print (x)

# x=5

# x%=3          # % returns reminder
# print (x)

# x|=2
# print (x)

# x^=3          # zor operators
# print (x)

# a=10
# b=20

# print("a == b:",a==b)
# print("a==10:",a==10)

# print("a != b:",a!=b)

# print(" a > b",a>b)
# print("a<b:",a<b)

# print(" a >= b",a>=b)
# print(" a <= b",a<=b)
# print(" a >= 10",a>=10)


                #logical operators


# x = 3

# print(x < 5 and x < 10)
# print(x < 5 or x < 4)
# print(not(x > 5 and x > 4))

# y = 3

# print(x is y )
# print(x is not y)

# x = 10
# y = 10

# print(x is y)

# x = ["Maruti", "BMW"]
# y = ["Maruti", "BMW"]

# print(x is y)

# print("Maruti" in x)
# print("Maruti" not in x)

# print("maruti1" in x)
# print("maruti1" not in x)

                    #binary

# x = 10      # 0000 1010
# y = 20      # 0001 0100

# print(x & y)    #0
# print(x | y)    #30
# print(x ^ y)    #30
# print(~x)  
# print(~y)
# print(x << 2)   #   0000 0101 => 0010 1000
# print(y << 2)   #   0001 1110 => 0111 1000
# print(x >> 2)
# print(y >> 2)


'''
0000 1010
0001 1110
---------
0001 1110
'''

                    #input function

# name = input("please enter your name: ")
# print("Hello ", name)

# input takes the data and store it, and return it when required........

# name = input("please enter your name: ")
# print("Hello ", name)
# age = input("please enter your age: ")
# print("Hello ", name, "you are ", age, " years old.")
# phone = input("please enter your phone number: ")
# print("your phone number is ", name)
# email = input("please enter your email: ")
# print("your email is ", name)


                # this is the case of string concatination (pronouncition: con cati nation)
# x = input("Enter first value for sum: ")
# y = input("Enter second value for sum: ")
# z = x + y
# print("sum: ", z)

'''we use type casting, to change the data type and to prevent the data from case of string concatination.....'''


                # we used TYPE CASTING here.....
                # to use it proprely use in there are 2 ways to int
                # 1st one is to use int as 

# x = int(input("Enter first value for sum: "))
# y = int(input("Enter second value for sum: "))
# z = x + y
# print("sum: ", z)

#                 # 2st one is to use int as 



# x = (input("Enter first value for sum: "))
# y = (input("Enter second value for sum: "))
# z = int(x) + int(y)
# print("sum: ", z)

'''Write program to calculate hypotenuse between sides '''
# formula for hypotenuse = H^2 = P^2 + B^2


# p = int(input("perpendicular of triangle: "))
# b = int(input("base of triangle: "))

# h = (((p ** 2) + (b ** 2)) ** (1/2))       # logic for square root

# print(h)

# p = (input("perpendicular of triangle: "))
# b = (input("base of triangle: "))

# h = (((int(p) ** 2) + (int(b)** 2)) ** (1/2))       # logic for square root

# print(h)

# print("+-----------------+")
# print("|                 |")
# print("|                 |")
# print("|                 |")
# print("|                 |")
# print("|                 |")
# print("+-----------------+")

# print("+" + "-" * 10 + "+")
# print(("|" + ' ' * 10 + "|\n")*5, end="")
# print("+" + "-" * 10 + "+")

# print("hello how are you ?", end="\n")
# print("i am good")

# print("hello how are you ?", end=" ")
# print("i am good")

# print("hello how are you ?", end="")
# print("i am good")


# print(("+" + "-" * 10 + "+\n")+ (("|" + ' ' * 10 + "|\n")*5) + ("+" + "-" * 10 + "+") )
# print("+" + "-" * 10 + "+")
# print(("|" + ' ' * 10 + "|\n")*5, end="")
# print("+" + "-" * 10 + "+")

# city = 'Bhopal'

# 012345 <- index positions
# -6-5-4-3-2-1 <- negative indices 

# print(city[0])          # B     (first character)
# print(city[-5])         
# print(city[2])          # o
# print(city[-1])         # l
# print(city[-3])         # p

# print(2 == 2)
# print(2 == 2.0)

# var = 0             # assingning 0 to var
# print(var == 0)

# var = 1             # assingning 1 to var
# print(var == 0)

# var = 13

# if var == 11:
#     print("var is 11")
#     print("hello")

# elif var == 12:
#     print("var is 12")
#     print("hi")

# else:
#     print("var is not 11 or 12")

# number1 = int(input("enter the first number: "))
# number2 = int(input("enter the second number: "))

# if number1 > number2:
#     larger_number = number1

# else:
#     larger_number = number2
    
#     print("the large number is: ", larger_number)

# number1 = int(input("enter the first number: "))
# number2 = int(input("enter the second number: "))

# if number1 > number2: larger_number = number1
# else: larger_number = number2
# print("larger number is: ", larger_number)

# number1 = int(input("enter the first number: "))
# number2 = int(input("enter the second number: "))
# number3 = int(input("enter the third number: "))

# largest_number = number1


# if number2 > largest_number:
#     largest_number = number2

# if number3 > largest_number:
#     largest_number = number3

# print("the larger number is: ", largest_number)

# number1 = int(input("enter the first number: "))
# number2 = int(input("enter the second number: "))
# number3 = int(input("enter the third number: "))

# largest_number  = max(number1, number2, number3)
# lowest_number  = min(number1, number2, number3)

# print("the larger number is: ", largest_number)
# print("the lowest number is: ", lowest_number)


                # Loops

                # while loop


# while True:
#     print("I am stuck in a loop.")

                # to escape the loop press ctrl + c


# largest_number = -999999999

# number = int(input("Enter a number or type -1 to stop: "))

# while number != -1:
#     if number > largest_number:
#         largest_number = number
#     number = int(input("enter a number or type -1 to stop: "))

# print("The largest number is: ", largest_number)


# number = int(input("type a number: "))
# even_count = 0
# odd_count = 0

# while number != 0:
#     if number % 2 == 0:
#         even_count += 1    # even_count = even_count + 1

#     else:
#         odd_count += 1

#     number = int(input("type a number: "))

# print("even: ", even_count)
# print("odd: ", odd_count)


# name = input("name of the plant: ")

# if name == "Spathiphyllum":
#     print("Yes - Spathiphyllum is the best plant ever!")

# elif name == "spathiphyllum":
#      print("No, I want a big Spathiphyllum!")

# else:
#     print( "Spathiphyllum! Not", name, "!" )


# counter = 5 

# while counter != 0:
#     print("Inside the loop.", counter)
#     counter -= 1 
# print("Outside the loop =.", counter)


# counter = 5 

# while counter:
#     print("Inside the loop.", counter)
#     counter -= 1 
# print("Outside the loop =.", counter)


                    # FOR LOOP


# for counter in range(10):
#     print("counter: ", counter)

# for counter in range(2, 8):
#     print("counter: ", counter)


                # Break


# print("The break instruction:")
# for counter in range(1, 6):
#     if counter == 3:
#         break
#     print("Inside the loop.", counter)
# print("Outside the loop.")


                # Continue

# print("The break instruction:")
# for counter in range(1, 6):
#     if counter == 3:
#         continue
#     print("Inside the loop.", counter)
# print("Outside the loop.")


# largest_number = -999999999

# counter = 0

# while True:
#     number = int(input("enter a number or type -1 to stop: "))
#     if number == -1:
#         break
#     counter += 1
#     if number > largest_number:
#         largest_number = number

# if counter != 0:
#     print("The largest number is: ", largest_number)
# else:
#     print("You havent't entered any number")


# largest_number = -999999999
# counter = 0

# number = int(input("Enter a number or type -1 to stop: "))

# while number != -1:

#     if number == -1:
#         continue
#     counter += 1

#     if number > largest_number:
#         largest_number = number
#     number = int(input("enter a number or type -1 to stop: "))


# if counter:
#     print("The largest number is: ", largest_number)
# else:
#     print("You haven't entered any number")


                # to debugthe code

# largest_number = -999999999
# counter = 0

# number = int(input("Enter a number or type -1 to stop: "))

# while number != -1:
#     print("Start: ", number)
#     if number == -1:
#         continue
#     counter += 1

#     if number > largest_number:
#         largest_number = number
#     number = int(input("enter a number or type -1 to stop: "))
#     print("End: ", number)

# if counter:
#     print("The largest number is: ", largest_number)
# else:
#     print("You haven't entered any number")

# counter = 1

# while counter < 5:
#     print(counter)
#     counter += 1
# else:
#     print("else: ", counter)


# counter = 5

# while counter < 5:
#     print(counter)
#     counter += 1
# else:
#     print("else: ", counter)

# for counter in range(5):
#     print(counter)
# else:
#     print("else", counter)

# counter = 111
# for counter in range(2 , 1):
#     print (counter)

# else:
#     print("else", counter)    

# block = int(input("enter a value: "))

# counter = 0

# while (block - counter > 0):
#     counter += 1
#     block = block - counter
    
    
# print("height of the pyramid is: ", counter)

'''
blocks              13  12  10  7   3
counter             1   2   3   4   5
'''

'''
in the above code first we used this code:


block = int(input("enter a value: "))

counter = 

while (block - counter > 0):
    block = block - counter
    counter += 1
    
print("height of the pyramid is: ", counter)

in this code the counter is increasing (counter += 1) before subtracting form block (block = block - counter) 
thats's why its incorrect........

to correct it we used the above code.....'''


# git add *
# git comit -m ""
# git add *
# git commit -m "explain the commit here"
# git puch


                # List


# a list is a data set of pythan  '''''

# numbers = []     #   declaration
# numbers = [10,5,7,2,1] #      declaration and initialisation

# print(numbers)
# print(type(numbers))

# print(numbers[0])
# print(numbers[1])
# print(numbers[2])
# print(numbers[3])
# print(numbers[4])

# numbers[0]= 100
# print(numbers)


# numbers = [10,5,7,2,1]
# print("original list contents:", numbers)    # printing original list contents'

# numbers[0] = 111
# print("new list contents:", numbers)      #   current list contents.
# print("original list contents:", numbers)    # printing original list contents.


# numbers[1] = numbers[4]    # copying value of the fifth element to the second'
# print("new list contents:", numbers)    #   printing current list contents.


# print(numbers)
# print(len(numbers))      #  its a function -  len = lenght of the list ''''''


# del numbers[1]      #  its a keyword -   del = delete any number in list ''''''

# print(numbers)
# print(len(numbers))


# numbers = [111,7,2,1]
# print(numbers[-1])         #    negative numbers index is start from  [-1]''''''''

# print(numbers[-4])
# print(len(numbers))

# print(numbers[len(numbers) * -1])


# hat_list = [1,2,3,4,5]

# var = int(input("enter an integer to replace the middle element:"))

# hat_list[int(len(hat_list) // 2)] = var

# print(hat_list)



            # functions and methods


# list = [5,4,3,2,1]
# print(list)
# print(f'length of List: {len(list)}')

# list.append(6)            # apend method
# print(list)
# print(f'length of the list: {len(list)}')

# numbers = [111, 7, 2, 1]
# print(len(numbers))
# print(numbers)

# numbers.append(4)

# print(len(numbers))
# print(numbers)

# numbers.insert(0, 222)

# print(len(numbers))
# print(numbers)


# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for count in range (len(list)):
#     print(list[count])

# list = []

# for count in range(1,11):
#     list.append(count)
# print(list)

# for count in range(1,11):
#     list.insert(count-1, count)
# print(list)

# count = 1
# while count<=10:
#     list.append(count)
#     count += 1
# print(list)


# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# for count in range(len(my_list)):
    
#     my_list[count] += 1
# print(my_list)

'''print sum of all elements from the list'''

# x = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# sum = 0 
# for count in range(len(x)):
    
#     sum += x[count]
# print(sum)  


# for element in x:
#     sum += element
# print(sum)


# a = 10
# b = 20
# print("a:", a)
# print("b:", b)
# #
# a, b = b, a
# print("a:", a)
# print("b:", b)

# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# z = 0
# for i in range(len(x)):
#         z = x[i] + z

# print(z)


# my_list = [10, 1, 8, 3, 5]
# print(my_list)
# my_list[0], my_list[4] = my_list[4], my_list[0] 
# my_list[1], my_list[3] = my_list[3], my_list[1] 
# print(my_list)


# lst =[1,2,3,4,5]
# lst.insert(1,6)
# del lst[0]
# lst.append(1)
# print(lst)


# lst =[1,2,3,4,5]
# lst_2 =[]
# add = 0

# for number in lst:
#     add += number
#     lst_2.append(add)
# print(lst_2)
# print(lst)



                    #   sorting 
                    #   1. bubble sort

print("CURRENTLY WE ARE LEARNINGN ABOUT SORTING, " \
        "WE ARE USING BUBBLE SORT PROCESS, " \
        "IN THIS WE CREAT FOR LOOPS TO SORT THE LIST")

my_list = [8, 10, 6, 2, 4]
count = 0
print("original list:", my_list)

for index1 in range(len(my_list) - 1):
    for index in range(len(my_list) - 1):
        count += 1
        if (my_list[index] > my_list[index + 1]):
            my_list[index], my_list[index +1] = my_list[index +1], my_list[index]

print(f"sorted list: {my_list}")
print(f"my program has run for : {count} times")

'''-----------------------------------------------------------------------------------------------------------------------------'''

print("IN THIS WE JUST ADDED '- index1' FOR THIS LOOP 'for index in range(len(my_list) - 1):'," \
"       SO IT BECAME THIS 'for index in range(len(my_list) - 1 - index1):', " \
"       THIS REDUSES THE NUMBER OF ITRATIONS AND MADE IT MORE EFFICIENT.")

my_list = [8, 10, 6, 2, 4]
count = 0
print("original list:", my_list)

for index1 in range(len(my_list) - 1):
    for index in range(len(my_list) - 1 - index1):
        count += 1
        if (my_list[index] > my_list[index + 1]):
            my_list[index], my_list[index +1] = my_list[index +1], my_list[index]

print(f"sorted list: {my_list}")
print(f"my program has run for : {count} times")