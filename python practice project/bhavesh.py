''' rvision class '''

                                # comaprision opreator 
# equals (==)
# no equals (!=)
# a < b
# a > b
# a <= b
# a >= b


# << left shift opretor         used for bits
# >> right shift opretor

''' and, or, not'''

# a = 20
# b = 30

# print(a < b and a == 20)
# print(a > b and a == 20)


# print(a < b or a == 20)
# print(a > b or a == 20)


# print(not(a < b and a == 20))
# print(not(a > b and a == 20))

'''
a   b   a and b
T   F   F
F   T   F
T   T   T
F   F   F

a   b   a or b
T   F   T
F   T   T
T   T   T
F   F   F
'''

                                    # identity opretor

# a = 20
# b = 30

# print(a is b)
# print(a is not b)

# x = ["a", "b"]

# y = ["a", "b"]

# z = x

# print(x is y, x is z, y is not z)       # x is y sirf vlues ke sath kaam karta list ke sath nahi. jab bhi hum lsit check karte tab hum 
                                          # address check karte hai, issliye false aaya.. 












'''write a loop to creat a list of even numbers between 1 to 10?'''

# x = [i for i in range(1, 11) if i % 2 == 0]
# print(x)

# even = []
# odd = []
# for i in range(1, 11):
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(f"Even numbers: {even}")
# print(f"Odd numbers: {odd}")


'''write a loop to create a list of odd numbers between 1 to 10?'''

# x = [i for i in range(1, 11) if i % 2 == 0]
# print(x)

# even = []
# odd = []
# for i in range(1, 11):
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(f"Even numbers: {even}")
# print(f"Odd numbers: {odd}")

'''print a number from 1 to 100.'''

# i = 1

# while i <= 100:
#     print(i)
#     i += 1

# print("loop ended")

'''print a number from 1 to 100.'''


# i = 100

# while i >= 1:
#     print(i)
#     i -= 1

# print("loop ended")

'''print a multiplication table of number n.'''


# n = int(input("eneter a number: "))
# x = 1

# while x <= 10:
#     print(n*x) 
#     x += 1
# print("loop ended")

'''print the elements of following list in a loop'''

# num = [1, 4, 9, 16, 36, 49, 64, 81, 100]

# index = 0

# while index < len(num):
#     print(num[index])
#     index += 1

'''search for the value x in the following list'''

# num = (1, 4, 9, 16, 36, 49, 64, 81, 100)

# x = int(input("enter a number: "))
# i  = 0
# while x <= len(num):
#     if x == len(num):
#         print(x)
#         break
# else:
#         print("x dose not exsist")

        
''' need to work on line 953'''

# i = [17, 3, 11, 5, 1, 9, 7, 15, 13]

# index1 = 0

# for index in range(len(i)):
#     if i[index] > index1 :
#         index  = index1
#     # if index <= index in range(len(i) - 1):

# else:
#     print(i[index])


# for i in range(1,6,1):                  #1 2 3 4 5
    
#     for j in range(1,6,1):              #1 22 333 4444 55555
    
#         print(" * ", end = " ")
#     print()

    
# for i in range(1,6,1):
    
#     for j in range(i):
    
#         print(" * ", end = " ")
#     print()


'''
column     row
i           j           *
1           1(1,5)      * * * * *
2          1(1,5)      * * * * * 
3

i   j       *
1   1(1)    *
2   2(2)    **


'''



    
# for i in range(1,6):
    
#     for j in range(1,6,1):
#         if(j<=i):
#             print(" * ", end = " ")
#         else:
#             print(" ", end = " ")
#     print()    



for i in range(1,6):
    #print("*")
    for j in range(1,6):
        if(j-i>=j):
            print(" * ", end = " ")
        else:
            print(" ", end=  " ")
    print()

'''
column      row         output
i           j               *
1           2


'''
# count = 0


# for count in range(1,6):
#    if count <= 6:
#     print(count,"missipily") 
# else:
#    print("ready or not, here i come.")

'''
                                                question

-> The people paid taxes, of course - their happiness had limits. 
The most important tax, called the Personal Income Tax (PIT for short) had to be paid once a year, 

and was evaluated using the following rule:

-> If the citizen's income was not higher than 85,528 thalers,  the tax was equal to 18% of the income minus 556 thalers and 2 cents 
(this was what they called tax relief)

-> if the income was higher than this amount, the tax was equal to 14,839 thalers and 2 cents, plus 32% of the surplus over 85,528 thalers.

-> Your task is to write a tax calculator.

'''

'''
                                                brainstroming


income = how much did he earned
name = of the person


'''

# name_1 = input("name of the person 1: ")
# name_2 = input("name of the person 2: ")

# basic_income = 85528

# income_1 = float(input("income of the person 1: "))
# #gst 18 %, if income < 85,528, then minus 556.2
# #gst 32 %, if income > 85,528, then tax = 14,839.2  + 32% over 85,528.
# income_2 = float(input("income of the person 2: "))

# tax = 0

# if income_1 <= basic_income:
#     tax = ((income_1/100)*18) - 556.2
#     print(f'{name_1}, income = {income_1}, tax = {tax:.2f}')
    
# elif income_1 >= 85528:
#     tax = (((income_1-85528)/100)*32) + 14839.2
#     print(f'{name_1}, income = {income_1}, tax = {tax:.2f}')


# if income_2 <= basic_income:
#     tax = ((income_2/100)*18) - 556.2
#     print(f'{name_2}, income = {income_2}, tax = {tax:.2f}')
    
# elif income_2 >= 85528:
#     tax = (((income_2-85528)/100)*32) + 14839.2
#     print(f'{name_2}, income = {income_2}, tax = {tax:.2f}')


'''
90

80 = 18

80< 32


'''


# num = int(input("enter a number: "))

# odd = 0
# even = 0

# while num != 0:
#     if num%2 == 0:
#         even += 1
#         print("even number")
        
#     else:
#         odd += 1
#         print("odd number")
        
#     num = int(input("enter a number: "))
