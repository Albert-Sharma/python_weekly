num = int(input("Enter a nuber:")) #let number be 1234
rev = num % 10                     #now here rev= 1234 %10 = 4(remainder)
num = num // 10                    #now num//10 i.e. 1234 //10 i.e. 123---quotient 
while(num >0):
    r = num %10                    #here r = num %10 = 123%10 = 3(remainder)
    num = num //10                 #now num = num //10 = 123//10 i.e. 12---quotient
    rev = rev*10 + r               #now rev = rev*10 +r ----4*10 + 3 == 43
print(rev)