# n=int(input("enter nummber"))
# f=1
# for i in  range(1,n+1):
#     f=f*i
#     print("fact=",f)

# while loop
# a while loop is used to repeatly execute a block of codes as long as a specific condition remains.
# 1- used to execute a bock of code as long as condition is true means 
# 2- condition is check before each allitration 
# 3- loop continues until the cond is become false .
# 4- must update the loop variable to avoid infinite loop. 
# a = int(input("enter a number"))
# b= int(input("enter a number"))
# c=int(input("enter a number"))
# if a>=b and a>=c:
#     print("largest number=",a)
# elif b>=a and b>=c:
#     print("largest number=",b)
# else:
#     print("largest number=",c)    

# ques- wap to reverse a number
n= int(input("enter a number="))
org= n
r=0
while n>0:
    d= n%10
    r= r*10+d
    n= n//10
print("rev=",r)
if r == org:
    print("palindrom")
else:
    print("not a palindrom")    

# wap to count a digit
# abs funct- the abs funct is build in function used to return positive value of a number remob=ve the nagative sign of the number 
# n= int(input("enter a number"))
# print("nagative=",n)
# p= abs(n)
# print("positive=",p)

# ques23
# start= int(input("enter a start number"))
# end= int(input("enter a end number"))
# print("even number:")
# for i in range(start,end+1):
#     if i%2 ==0:
#         print(i,end="")
# print("odd number:")
# for i in range(start,end+1):
#     if i%2!=0:
#         print(i,end="")

# strip remove leading and removing space
# s= input("enter a string=")
# print(s)
# sp= s.strip()
# print(sp) 

# remove wide space from l side and r side
# l= s.lstrip()
# print(l)
# r= s.rstrip()
# print(r)

# replace method old,new replace a one sub string with another 
# s= "i like java"
# print(s)
# r= s.replace("java","javascript")
# print(r)

# counrt of a substring
# s= input("enter a string=").lower()
# print(s)
# o= input("enter a find=").lower()

# c= s.count(o)
# print(c)
# sring builtin function 
# length
# s= input("enter a string=")
# print(s)
# l= len(s)
# print(l)
# max= written largest char by unique code value
# s= input("enter a string=")
# print(s)
# l= len(s)
# print(l)
# m= max(s)
# print(m)
# min= written smallest char by unique code value
# mi= min(s)
# print(mi)

# sorted funct= written sorted list of char 
# s= input("enter a string=")
# print(s)
# so= sorted(s)
# print("sort=",so)

#htr func= it converts value to string
# n= input("enter a num=")
# print(type(n),n)
# s= str(n)
# print(type(s),s)

# hey 