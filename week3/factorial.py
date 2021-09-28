#to find the factorial using whgile loop
n=int(input())              #let integer be 5
i=1                         # i =1
if n<0:                         
    print("Not Defined")
else:   
    while n>0:              
        i=i*n               # i = 1*5
        n =n-1              # n = 4...... then i = 5*4 & n =3..... then i = 20*3 & n=2..
    print(i)
