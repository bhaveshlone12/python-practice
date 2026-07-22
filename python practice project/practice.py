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

'''============================================================================================================================'''

                    #   sorting 
                    #   1. bubble sort

# print("CURRENTLY WE ARE LEARNINGN ABOUT SORTING, " \
#         "WE ARE USING BUBBLE SORT PROCESS, " \
#         "IN THIS WE CREAT FOR LOOPS TO SORT THE LIST")

# my_list = [8, 10, 6, 2, 4]
# count = 0
# print("original list:", my_list)

# for index1 in range(len(my_list) - 1):
#     for index in range(len(my_list) - 1):
#         count += 1
#         if (my_list[index] > my_list[index + 1]):
#             my_list[index], my_list[index +1] = my_list[index +1], my_list[index]

# print(f"sorted list: {my_list}")
# print(f"my program has run for : {count} times")


'''============================================================================================================================'''


# print("IN THIS WE JUST ADDED '- index1' FOR THIS LOOP 'for index in range(len(my_list) - 1):'," \
# "       SO IT BECAME THIS 'for index in range(len(my_list) - 1 - index1):', " \
# "       THIS REDUSES THE NUMBER OF ITRATIONS AND MADE IT MORE EFFICIENT.")

# my_list = [8, 10, 6, 2, 4]
# count = 0
# print("original list:", my_list)

# for index1 in range(len(my_list) - 1):
#     for index in range(len(my_list) - 1 - index1):
#         count += 1
#         if (my_list[index] > my_list[index + 1]):
#             my_list[index], my_list[index +1] = my_list[index +1], my_list[index]

# print(f"sorted list: {my_list}")
# print(f"my program has run for : {count} times")


                    # used while loop and used swapped as an variable.

# my_list = [8, 10, 6, 2, 4]
# swapped = True           #its a little fake, we need to enter the while loop. 
# count = 0
# print("original list:", my_list)

# while swapped:
#     swapped = False # no swaps sp far.
#     for i in range(len(my_list) - 1):
#         count += 1
#         if (my_list[i] > my_list[i + 1]):
#             swapped = True # a swap occurred.
#             my_list[i], my_list[i +1] = my_list[i +1], my_list[i]

# print(f"sorted list: {my_list}")
# print(f"my program has run for : {count} times")

                # used swapped in for loop to increass the efficinecy.

# my_list = [1, 2, 3, 4, 5]
# swapped = 0
# count = 0
# print("original list:", my_list)

# for index1 in range(len(my_list) - 1):
#     for index in range(len(my_list) - 1 - index1):
#         count += 1
#         if (my_list[index] > my_list[index + 1]):
#             my_list[index], my_list[index +1] = my_list[index +1], my_list[index]
#     if swapped == 0:
#         break
        
# print(f"sorted list: {my_list}")
# print(f"my program has run for : {count} times")



                #   using sort function***************



# my_list = [8, 10, 6, 2, 4]
# my_list.sort()
# print(my_list)


'''reverse the list'''

# my_list = [1, 2, 3, 4, 5]
# swapped = True
# count = 0
# print(f"my original list: {my_list}")

# print((len(my_list) // 2))

# for i in range(len(my_list) // 2):
#     #print((len(my_list) // 2))
#     my_list[i], my_list[-1 * (i + 1)] = my_list[-1 * (i + 1)], my_list[i]

# print(my_list)

'''
[a, b, c, d. e, f, g]
[g, f, e, d, c, b, a]

0 - -1
1 - -2
-1 * (index - 1)      # minus index


[a, b, c, d. e, f, g, h, i, j]

loop = 5

a = j
0 = -1 => (-1 * (index * 1))
index => len(list) - (index + 1)      # positive index
'''

# lst = ["D", "F", "a", "Z"]
# lst.sort()
# print(lst)


# print("A" > "a")  # output false as per thr acii value the acii value of a > A (acii value of a is 97, acii value pf A is 65)

# a = 3
# b = 1
# c = 2
# lst = [a, c, b]
# lst.sort()
# print(lst)


# a = "A"
# b = "B"
# c = "C"
# d = " "

# lst = [a, b, c, d]
# lst.reverse()
# print(lst)

# a = 1
# b = a
# a= 2
# print(a)
# print(b)


# lst_1 = [1]
# lst_2 = lst_1   # reference copy (reference copy is used for copying the address of the first reference, also known as refernce variable.)
# lst_1[0] = 2
# print(lst_2)


# lst_1 = [1, 2, 3, 4]
# lst_2 = lst_1[0:2]    # we can provide the index before and after : like 0:2 so take only 0,1 and exclude 2 just like range works from n to n-1. this process is known as slicing.
# lst_1[0] = 2
# print(f"list 2: {lst_2}")
# print(f"list 1: {lst_1}")

# my_list = [1, 2, 3, 4]
# new_list = my_list[1:3]    # we can provide the index before and after : like 0:2 so take only 0,1 and exclude 2 just like range works from n to n-1.

# print(new_list)


# new_list = my_list[1:-1]
# print(new_list)


# new_list = my_list[-1:1]
# print(new_list)


# print(ord(" "))     # use ord function to find the acii value of anything.


# my_list  = [10, 8, 6, 4, 2]
# del my_list
# print(my_list)      # outpt will be error, because my_list dose not exist due to del keyword.


# my_list = [0, 3, 12, 8, 2]
# print(5 in my_list)     # in checks weather the element exist in the list, if not then false, if yes the true.
# print(5 not in my_list)     # not checks weather the  element dose not exist in the list, if not then true, if yes the false.
# print(12 in my_list)

''' find the largest in the list?'''


''' 1st approach '''

# i = [17, 3, 11, 5, 1, 9, 7, 15, 13]

# largest = 0

# for element in range(len(i)):
#     if largest < i[element]:
#         largest = i[element]
# else:
#     print(largest)



''' second approach '''


# i = [17, 3, 11, 5, 1, 9, 7, 15, 13]

# largest = i[0]

# for element in range(len(i)):
#     if largest < i[element]:
#         largest = i[element]
# else:
#     print(largest)


'''___________________________________________________________________________________________________________________________________________'''


# i = [17, 3, 11, 5, 1, 9, 7, 15, 13]

# l = 5

# for index in range(len(i)):
#     if l == i[index]:
#         print(index)
#         break

# i = [17, 3, 11, 5, 1, 9, 7, 15, 13]

# l = int(input("number: "))

# for index in range(len(i)):
#       if l == i[index]:
#         print("5 is found at index: ", index)
#         break

'''___________________________________________________________________________________________________________________________________________'''

# i = 1
# j = not not i
# print(i)
# print(j)

'''
Truthy:         1, 2, 3, -1, 28, "a", "hello", [1, 2], {1:1}, " "
Falsy:          0, "", [], {}, (), None, NULL
'''



'''     List        '''

'''     
        Question            

why we use use 0 index rather then 1?

        Answer

In programming, indexing starts at 0 because an index represents an offset (a distance) from the starting point of a memory block, 
rather than a count of items. The first element is exactly zero steps away from the beginning.

This zero-based convention fundamentally boils down to efficiency and how computer memory is accessed:

Pointer Math: When a computer retrieves data from an array, it uses the formula: Target Address = Base Address + (Index x Size of Element). 
If indexing started at 1, 
the computer would have to execute an extra subtraction step (Index - 1) before calculating the memory address.

zero exactly stores the address rather then count, thats makes it easy the acces the first step, it represents 
that the 1st element is zero step away from you. 

'''


# numbers = [1, 2, 3, 4, 5]
# print(numbers)
# print(type(numbers))

# print(numbers[0])
# print(numbers[1])
# print(numbers[2])
# print(numbers[3])
# print(numbers[4])

# numbers[3] = 20
# print(numbers)

# numbers[2] = numbers[4]
# print(numbers)

# numbers[2], numbers[1] = numbers[1], numbers[2]
# print(numbers)


# numbers = [1, 2, 3, 4, 5]
# print(len(numbers))


# del numbers[4]
# print(numbers)

# print(len(numbers))

# len_of_list = len(numbers)
# print(len_of_list)

# print(numbers[-1])
# print(numbers[-2])
# print(numbers[-3])
# print(numbers[-4])


# a = 10
# print("Variable a: ", a)

# print("Address of Variable a in integers: ", id(a))
# print("Address of Variable a in hex (hexa-decima): ", id(a))

# print(hex(id(numbers)))
# print(hex(id(numbers[0])))
# print(hex(id(numbers[1])))
# print(hex(id(numbers[2])))

'''     append & insert     '''

# list = [5,4,3,2,1]
# print(list)
# list.append(6)              #append (used to insert at last index of the of the list.)
# print(list)
# list.insert(0,222)          #insert   (used to insert at desired index)
# print(len(list))
# print(list)

# list[0],list[6] = list[6],list[0]       #swapping (used to swap index 0 & 6 with each other.)
# print(list)

# del list[6]             #delet
# print(list)

''' can you wirte a program to traverse a list'''

# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for index in range(len(list)):
#     print(list[index])         

''' index represents the entire elements index from 0th index to 9th index, to print element of the list we use list[0], list[1]
but we need to use loop, and that's how its done.


for index in range(len(list)):
    print(list[index])         
'''

'''     question        

write a program to insert 10 numbers starting fron 1 to 10 a  list
'''
'''     used for loop       '''
# list = []

# for i in range(1,11):
#     list.insert(i,i)
# print(list)

'''     used while loop     '''

# list = []
# i = 1

# while i < 11:
#     list.append(i)
#     i +=1
# print(list)

'''     Bubble sorting       '''

# list = [8, 10, 6, 2, 4]

# print("Current list: ", list)

# for index in range(len(list)- 1):
#     for index_inner in range(len(list)- 1):
#         if list[index_inner] > list[index_inner + 1]:
#             list[index_inner],list[index_inner + 1] = list[index_inner +1 ],list[index_inner]
# print("Sorted list: ", list)

'''
dry run 

Current list:  [8, 6, 2, 4, 10]

index           0
index_inner     0   1   2   3
'''

# list = [8, 10, 6, 2, 4]

# print(list)

# count = 0

# for i in range(len(list)- 1):
#     for i_n in range(len(list)- 1):
#         if list[i_n] > list[i_n + 1]:
#             list[i_n], list[i_n + 1] = list[i_n + 1], list[i_n]
#         count += 1
# print(list)
# print(count)

'''     efficient       '''

# list = [8, 10, 6, 2, 4]

# print("Current list: ", list)

# count = 0
# swapped = False

# for index in range(len(list)- 1):
#     for index_inner in range(len(list)- 1 - index):
#         if list[index_inner] > list[index_inner + 1]:
#             list[index_inner],list[index_inner + 1] = list[index_inner +1 ],list[index_inner]
#             swapped = False
#         count += 1
#     if not swapped:
#         break
# print("Sorted list: ", list)
# print(count)

# list = [2,4,1,9,7,6]
# print(list)

# list.sort()
# print(list)

# list.reverse()
# print(list)

# list = ["a","c","b","d","g"]
# print(list)

# list.sort()
# print(list)

# list.reverse
# print(list)


'''         MEMBERSHIP OPERATORS          '''

# my_list = [0,3,12,8,2]
# print(5 in my_list)
# print(5 not in my_list)
# print(12 in my_list)

'''     "question"

find the largest number in the list?
find the given element ( 5 )in the list with index?

my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]        '''


'''_________________________________________________________________________________________________________________________________________'''

'''         list Comprehension          '''

# row = []

# for i in range(8):
#     row.append("White Pawn")

# print(row)

#                 #   List comprehension


# row = ["White Pawn" for i in range(8)]

# print(row)


# squares = [x ** 2 for x in range(10)]

# print(squares)

# twos = [2 ** i for i in range(8)]

# print(twos)


# # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# odds = [x for x in squares if x % 2 != 0]

# print(odds)

# board = []

# for i in range(8):
#     row = ["EMPTY" for i in range(8)]
#     board.append(row)

# print(board)

'''
git fetch : git 

Cafe Management
Z
Dev - Development / Dev Environment         dev.cafemanagement.com
Testing - Stage Environment                 stage.cafemanagement.com
Client Testing - UAT environment            uat.cafemanagement.com
Users - Production Evironment               cafemanagement.com

Dev         - Development branch
            - feature/v1.0/khushi
            - bugfix/v1.1/khushi


|
stage       - stage branch
|
uat         - uat branch
|
Prod        - main branch

'''
# print("Checking branch changes!")

'''CHESS BOARD'''


# board = []

# for i in range(8):
#     row = ["EMPTY" for i in range(8)]
#     board.append(row)

# print(board)

# board [0] [0] = "ROOK"
# board [0] [7] = "ROOK"
# board [7] [0] = "ROOK"
# board [7] [7] = "ROOK"

# board [0] [1] = "KNIGHT"
# board [0] [6] = "KNIGHT"
# board [7] [1] = "KNIGHT"
# board [7] [6] = "KNIGHT"

# board [0] [2] = "BISHOP"
# board [0] [5] = "BISHOP"
# board [7] [2] = "BISHOP"
# board [7] [5] = "BISHOP"

# board [0] [3] = "KING"
# board [7] [4] = "KING"


# board [0] [4] = "QUEEN"
# board [7] [3] = "QUEEN"

# pawns = "PAWNS"

# for index in range(len(board)):
#     board [1] [index] = pawns
#     board [6] [index] = pawns

# for index in range(len(board)):
#     print(board[index])


'''TEMP PER DAY in a month'''

# temps = [[0.0 for h in range(24)] for d in range(31)]
# print(temps)

# random = [20, 34, 44, 12, 34, 20, 34, 44, 12, 34, 20, 34, 44, 12, 34, 20, 34, 44, 12, 34, 20, 34, 44, 12, 34, 20, 34, 44, 12, 34, 10]

# for index in range(len(temps)):
#     temps[index] [11] = random[index]

# for index in range(len(temps)):
#     print(temps[index])

''' calculate the avg temp of month'''

# sum = 0

# for index in range(len(temps)):
#     sum += temps[index] [11]
# print(sum/31)

# highest = 0

# for index in range(len(temps)):
#     for inner_index in range(len(temps[index])):
#         if highest < temps[index][inner_index]:
#             highest = temps[index][inner_index]
# print(highest)

# lowest = 0


# for index in range(len(temps)):
#     for inner_index in range(len(temps[index])):
#         if lowest > temps[index][inner_index]:
#             lowest = temps[index][inner_index]
# print(lowest)

'''example'''

# rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]

# for building_index in range(len(rooms)):
#     print("Building: ", building_index+1)
#     for floor_index in range(len(rooms[building_index])):
#         print("Floor: ", floor_index+1)
#         print(rooms[building_index][floor_index])

# # in the second building, on the tenth floor 14

# rooms [1] [9] [13] = True

# #and release the second room on the fifth floor located in the first building

# rooms [0] [4] [1] = False

# # Check if there are any vacancies on the 15th floor of thr building...

# '''
# building        1       [2]
# floors          1       [14]
# rooms           20
# '''

# rooms [2] [14] [0] = True
# rooms [2] [14] [1] = True
# rooms [2] [14] [2] = True
# rooms [2] [14] [3] = True
# rooms [2] [14] [4] = True
# rooms [2] [14] [5] = True

# temp = -1

# for room_index in range(len(rooms[2] [14])):
#     if rooms [2] [14] [room_index] == False:
#         temp = room_index
#         break

# if temp == -1:
#     print("no rooms availabe")
# else:
#     print(f'{temp+1}th room is availabe')

i = [3,1,-2]
print(i[-1])