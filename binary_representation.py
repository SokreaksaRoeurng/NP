# #18. python program to check number representation is in binary 

# b = int(input("Enter number: "))

# x = int(bin(b)[2:])

# print("binary represent: ", x)

number = int(input("enter number: "))

while number !=0:
    remainder =number %10
    if(remainder!=0 and remainder!=1):
        print("Number is not in bunary representation! ")
        break
    number = number//10
    if(number==0):
      print("Number is bunary representation !")
