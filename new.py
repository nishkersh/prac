# studing from anuj bhaiya 

# using range function 
''' a=range(10)
print(a) '''
# list is used to print all the values of range 
''' a=list(range(2,10,2))
print(a)
a=list(range(2,11,2))
print(a) '''

# loop
# for x in range(10):
    # print(2*x) # prints each value at new line 
    # print(2*x,end=" ") #end decides what will be there after each output
    # print(2*x,end=" , ")

# names = ['anuj','rik','nik','sagar']
# for name in names:
#  print(name*2,end=" ")

# n=5
# while n >= 0:
#     print(n)
#     n-=1

# a=int(input())
# for i in range(a):
#     if i>7:
#         break
#     elif i==4:
#         continue
#     else:
#         print(i)

# we use triple quotes to add multiline strings
# intro = ''' hi there  my name is 
# ckk jjbckwb bckb
# ewueu'''
# print(intro)

#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||#
#-----------------------------------------------------------------------------------------#
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||#

# studing from Hashit Vashisth

# strings

# name = "hrarshirt"
# name2 = 'RBERIBBKWRB'
#  1.string indexing 
# print(name[-1])

# 2. string slicing 
# print(name2[1:6:2])

# here 1 is inclusive and represents start index 6 is ending index but it's exclusive and 2 means it will escape 1 character inbetween

# 3. take two user inputs
# name,userage=input("enter userage and name : ").split(',')
# print(userage)
# print(name)
# 4. lower,upper,title method
# print(name.upper())
# print(name.title())
# print(name2.lower())


# 5. find,replace,centre method
# print(name.find("r",3 ))
# the first position describes the word which is to be find and another word is that from which place it's to be found
# print (name.replace('r','x',2)) 
# at last 2 means  only 2 r's will be replaced by the x
# print(name.center(13, '$'))

# 6. strings are immutable
    # means we can perform operations to change and print different values in defined string but the original value can't be changed in string i.e 
# name[2]='s' will give error

# string formatting
# name = "harshit"
# age= 24
# print("hello " + name + " your age is " +  str(age) )
# print("hello {} your age is {} ".format(name,age + 2))
# print(f"hello {name} your age is {age + 2} ")

#-----------------------------------------------------------------------------------------#

# if statement
# age=int(input("enter your age"))
# if age>=18:
#     print(" You Are An Adult Now ")
#     print(" you can ride bikes")
# else:
#      print(" You are a kid")

# in python we use and ,or instead of && , || repectively 
# name = "dccifbw"
# if 'c' in name:
#     print("present in name")
# else : 
#     print("not present")

# name=""
# if name:
#     print("name is not empty")
# else:
#     print("it's empty")
# i=0
# while i<=10:
#     print("hello world")
#     i+=1

# num = int(input("enter n : "))
# sum= 0 
# i=1
# while i<=num:
#     val = int(input("enter value to be added : "))
#     sum+=val
#     i+=1
# print(sum)

# num =input("enter numeric value with more than 1 digit ")
# n = len(num)
# sum=0
# i = 0
# print(type(num[1]))

# while i<n:
#     sum =sum + int(num[i])
#     i+=1
# print(sum)

# name = input("enter your name ") 

# for i in range(1,11):
#    print(f"hello world : {i}")     
    
# sum = 0
# num = input()
# for i in range(0,len(num)):
#     sum+=int(num[i])

# print(sum)

# name=input()
# tmp=""
# for i in range(0,len(name)):
#     if name[i] not in tmp:
#         tmp+=name[i]
#         print(f"{name[i]} : {name.count(name[i])}")
#     i+=1

# import random
# n  = random.randint(1,101)
# num = int(input("Enter the guessed number "))
# guess=1
# gameover = False
# while not gameover:
#     if num==n:
#         print(f"u guessed right and no of attempts {guess}")
#         gameover=True
#     elif num>n:
#         print("value assumed is too high")
#         guess+=1
#         num=int(input("guess again  "))
#     else:
#         print("value assumed is too low")
#         guess+=1
#         num=int(input("guess again  "))

#-----------------------------------------------------------------------------------------#

# step argument
# for i in range(10,0,-1):
#     print(i)

# for loop and strings

# name = "rikchatterjee"
# for i in name:
#     print(i , end=" ")

#-----------------------------------------------------------------------------------------#

# function
# def greater(a,b ):
#     if a > b:
#         print(a)
#     else :
#         print (b)
# greater(9,10)

# palindrome number 
# def palindrome(word):
#     reverse=word[::-1]
#     return word==reverse

# print(f"{palindrome(input( ' enter word '))}")

# fibonaccci series

# def fibonacci(n):
#     a=0
#     b=1
#     if n==1:
#         print(a)
#     elif n==2:
#         print(a,b)
#     else:
#         print(a,b , end=" ")
#         for i in range(n-2):
#             c=a+b
#             a=b
#             b=c
#             print(b , end = " ")


# fibonacci(int(input()))

#-----------------------------------------------------------------------------------------#

# lists
# list = [1,2,3 , "rik" , 5.03 , [1,2,3] , None] 
# print(list)
 
# append (stores element at last in list), insert , extend in list and differnce between append and extend
# list  = []
# list.append("rik")
# list.append("sagar")
# list1=[ 1,2,3,4,5 ]
# list1.insert(2,"NewlyAdded")
# list3=list+list1
# list.extend("extendeditem")
# list2=[ 3.8 , 8.7 , 9.0 , 2.3 , 4.7 ]
# list2.extend(list)
# print(f"{list} and the other is {list2} and now it's {list3} and at last {list1}")
# num1=[1,2,3,]
# num2=[4,5,6]
# num1.append(num2)
# print(f"{num1} and {num2}")
# so becoz of append therre will be list in the list therefore we can crate multidimensional list using append
#-----------------------------------------------------------------------------------------#
# delete data from list using pop , del operator ,remove method
# list=[1,2,3,4,5,6,7,1,2,3]
# popped_item = list.pop()
# by default it pops from last index if not mentioned
# popped1= list.pop(2)
# print(F"{popped_item} and {popped1} and list is {list}")
# list.remove(2) it removes only first occurance of the value 
# del list[4]
# print(f"{list}")
#-----------------------------------------------------------------------------------------#
# in keyword in list used to check if the searched element is in the list or not 
# fruit= ["apple","mango","Banana","Papaya"]
# def check(fruit , item):
#     return item in fruit 
# print(f"{check(fruit,input('enter fruit name '))}")

#-----------------------------------------------------------------------------------------#

#  count , sorting , reverse , clear (used to empty the list) , copy   in list
# list1 = [12,45,7.3,7,55,6,3,]
# list.sort()
# print(f"{list}") 
    #  OR 
# print(sorted(list1))

# fruit= ["apple","mango","Banana","Papaya","Banana","mango","Banana"]
# print(fruit.count("Banana"))
# fruit.reverse()
# print(f'{fruit}')
#    OR  
# print(list(reversed(fruit)))
# fruit.clear()
# print(fruit)
# fruit1=fruit.copy()
# print(fruit1)
# list comparison using is and == 
# print(fruit1==fruit) double equal checks if the list values are same or not 
# print(fruit1 is fruit) true only when list refer to same memory location 
#-----------------------------------------------------------------------------------------#
# split method to convert string to list 
# user_info="hi my name is rik".split()
# hobby_info=input(" enter your hobbies ").split()
# sub1,sub2,sub3=input('enter your subjects').split( ",")
# print(user_info)
# print(hobby_info)
# print(sub1 , sub2 , sub3)
#-----------------------------------------------------------------------------------------#
# and join method to convert list to string 
# userinfo=["Hi","My","Name","Is","Rik"]
# print(''.join(userinfo))
#-----------------------------------------------------------------------------------------#
# loops in list 
# fruit= ["apple","mango","Banana","Papaya","Banana","mango","Banana"]
# for fruit1 in fruit:
#     print(fruit1)
#-----------------------------------------------------------------------------------------#
# list inside list 2D list 
# matrix=[[1,2,3],[4,5,6],[7,8,9]]
# for l1 in matrix:
#     print(l1)


# for submatrix in matrix:
#     for l1 in submatrix:
#         print(l1)

# print(matrix[2][1])
#-----------------------------------------------------------------------------------------#
# generating list with range functions , something more about pop method , index method , pass list to a function 
# values=list(range(1,10))
# print(values)
# fruit= ["apple","mango","Banana","Papaya","Banana","mango","Banana"]
# print(fruit.index("mango")) considers the very first index from left 
#-----------------------------------------------------------------------------------------#
# min and max functions in list
# num=list(range(1,11))
# print(max(num))
# print(min(num))

# num=list(range(1,11))
# def nev_func(l):
#     nev_num=[]
#     for value in l:
#         nev_num.append(-value)
#     print(nev_num)

# nev_func(num)

# def sq_func(arr):
#     sq_arr=[]
#     for l in arr:
#         sq_arr.append(l**2)
#     print(sq_arr)  

# num=list(range(1,11))
# sq_func(num)

# EX : 1   to convert ['abc' , 'tuv' , 'xyz'] into  ['cba' , 'vut' , 'zyx']
# matrix = [ 'abc' , 'tuv' , 'xyz' ]
# def rev_matrix(matrix):
#  matrix1=[]
#  for submatrix in matrix:
#     matrix1.append(list(reversed(submatrix)))
#  print(matrix1)
# rev_matrix(matrix)

# in list of numbers filter out odd and and even numbers in it and make it a 2D list
# num=list(range(1,11))
# def filter_func(num):
#     output=[]
#     odd=[]
#     even=[]
#     for l in num:
#         if l%2==0:
#             even.append(l)
#         else:
#             odd.append(l)
#     output.append(odd)
#     output.append(even)
#     print(output)
# filter_func(num)
    
# function to print common elements in list 
# num1 =[1,2,3,4,5,0]
# num2=[0,9,8,7,6,5,54,3,2]
# def common(sub1,sub2):
#     num=[]
#     for l in sub1:
#         if l in sub2:
#             num.append(l)
#         else:
#             pass
#     print(num)
# common(num1,num2)

# num=[1,2,3,[1,2],[3,4],[]]
# num1=[]
# def check_list(arr):
#     count=0
#     for l in arr:
#         if type(l)==type(num1):
#             count+=1
#     print(count)
# check_list(num)

#-----------------------------------------------------------------------------------------#

# Tuples are data structures that are immutable and are comparitively fast then list becoz of this.As they are immutable therefore we can't use  like pop ,delete ,remove ,append ,insert etc 
# but we can use methods like count,index,len,slicing
# and functions that we can use are min,max,sum

# tuple with one element
# word=('words',)
# num=(1), 

#tuple without parenthesis
# word1='rik','sagar','piyush'
# print(type(word1))
# print(type(word))

# tuple unpacking(always take same no of elements as in mno of elements in tuple )
# word1='rik','sagar','piyush'
# name1,name2,name3=(word1)
# print(name1)

# list inside tuples
 
list=("rik" ,"chatterjee" ,["flute" , "soccer" , "swimming"])
list[2].append("volleyball")
list[2].pop(0)

print(list)
