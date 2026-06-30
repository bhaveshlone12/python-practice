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

i = [17, 3, 11, 5, 1, 9, 7, 15, 13]

index1 = 0

for index in range(len(i)):
    if i[index] > index1 :
        index  = index1
    # if index <= index in range(len(i) - 1):

else:
    print(i[index])