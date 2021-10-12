#--------------------QUESTION1--------------#

#
##
###
####
#####

# METHOD 1
print("Method1 \n")
def fun1(n): #Function declaration

    #outer loop for number of rows
    for i in range(0,n): 

        #inner loop for number of columns
        for j in range(0, i+1):
            print("*", end="")

        #Ending the line after each row
        print("\r")

n =5
fun1(5)

# METHOD 2
print("\nMethod2 \n")

def fun2(m):
    list = []
    for i in range(1 , m+1):
        list.append("*"*i)
    print("\n".join(list))
m = 5
fun2(m)

#--------------------QUESTION2--------------#
        #
       ##
      ### 

print("\nQuestion2\n")

def num3(o):
    k = 2*o -2

    for i in range(0, o):
        for j in range(0, k):
            print(end=" ")
        k = k -2
        for j in range(0, i+1):
            print("* ", end="")
        print("\r")
o = 3
num3(o)
