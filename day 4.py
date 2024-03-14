# ----> while loop
#-----> break using while loop

# Eg:1
# 1.) Iterate from 20 to 30 and breake the loop
# i =20
#while i<31:
# if i ==27:
 #     break
 # print(i)
 # 1+=i

i= 20
while i<20:
    print(i)
    i+=1
        #if i==27:
            #break

    #3.)
"""
    # i =20
    # while i<31:
    # print(i)
    # if i==27:
    # break
 #   1+=i
            
"""


#--------> continue

i= 20
while i<31:
  if i==27:  
    continue
    print(i)
""
""
# ! Eg:5
#i =12
#while i<22:
    #  i=i+1
    #  if i== 11:
  #        break
#   print(i)

   
i=12
sum=0
while i<23:
     suum=sum+i
     i+1
print(sum)

  #! eg:6

i = 20
sum = 0
count =0
while i<=30:
     sum=sum+i
     count+=1
     i+=1
print(sum/count)



# ! -------> nested forr loop
# Eg:1

for i in range (1,3):
    for j in range(1,4):
        print(i,j)

 ! -------> nested forr loop
# Eg:1

for row in range (1,3+1):
    for col in range(1,4+1):
        print(row, col)

# Eg;2
# * * * *
# * * * *
# * * * *
# * * * *
rows = int(input("enter the rows: "))
col = int(input("enter the col: "))
for row in range (row):
    for col in range(col):
        print("*", end=" ")
    print()

    for row in range(5):
        for col in range (5):
            print(row, end=" ")
        print() 


sum = 0
for row in range (5):
    for col in range(5):
        sum= sum+1
        print(sum, end=" ")
    print()


# ! tom print stars in right angled triangle

for row in range(0,6):
    for col in range(0, row+1):
        print("*",end=" ")
    print()


#* * * * * *
#* * * * *
#* * * *
#* * *
#* * *
#* *
#*

for row in range(0,6):
    for col in range(0,row):
        print("*",end=" ")
        print()

#* * * * *
#*       *
#*       *
#*       *
#* * * * *
for row in range(5):
 for col in range(5):
     if col==0 or col==5-1 or row==0 or row==5-1:
         print("*", end=" ")
     else:
             print(" ",end=" ")
             print()
             



for row in range(0,5):
    for col in range(0,6):
        if (((row==0 and col==3) or (row==1 and col<=4))or (row==2 and (col<=5))):
             print("*" , end=" ")
        else:
             print(" ",end=" ")
    print()





   #----> list
#number--> int, float complex
#string
#boolean
#none
    
# Collection
# List
# tuple
# set
# dictionary

# ? ----> list
                                
#1.) if the collection of clements are sorounded by square brackets, it is considered #to be list
#eg:
#11 [4, 7, 9, 9.89, "hello", 7+91, [8, 9, 0]]

#Charactristics of list:
#1.) list have to be sorrrounded by
#2.) It is mutable (the elements in the list are changable) 3.) Every element inside list is indexed
#4.) The elements inside list will be ordered format
#5.) It can hold duplicate values
#6.) Its heterogenous

#To access the elements in list
#11 = [1, 4, 1, 7,89.7, 715, "p","1"]
# print(11)

# -----> indexing
# In the collection datatypes like list, tuple, string, the elements will be alloted
# with pre-defined unique value called index value

#we have 2 types of indexing
#Positive indexing starts with a from left hand side
#Negative indexing --> starts with -1 from right hand side


#> Positive indexing
#1st1 [1, 4, 1, 7,89.7, 7.5, "p", "1"]
#print(isti[a])
#print(1st1[4])
#print(1stl[20]) --> error
#? Negative indexing
#1st1 [1, 4, 1, 7,89.7, 7.5, "p", "i"]
#print(ist1[-1])
#print(isti[-5])

#?----> slicing
#1stl [1, 4, 19 7,897, 7.5, "p", "1"1
#1st1[start_index:end_index:step]
#print(isti[0:4])
#print (1st1[6:8])
#print(1st1[3:6])
#print(1sti[:5])
#print(1st1[3:])
#print(isti[:])
#print(Isti[0:7:11) # 1st1[8:7]--> both are same
#print(Isti[8:7:2])


1st1 - [1, 4, 1, 7,89.7, 7.5, "p", ""1
#print(istil-4:-1])
#print(1st1[-1:-4])[]
#print(1st1[ 7: 1])
#print(1st1[7:-1:2])

   #append() --> used to add elelement at last position of list
 #11 [9, 8, 6, 61
#11.append("car")
 #print(11)


   
    

  























































































































































































































































































































































































































