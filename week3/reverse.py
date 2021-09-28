num = int(input("Enter a nuber:")) #let number be 1234
absnum = abs(num)
if (num>0):
    rev = num % 10                     #now here rev= 1234 %10 = 4(remainder)
    num = num // 10                    #now num//10 i.e. 1234 //10 i.e. 123---quotient 
    while(num >0):
        r = num %10                    #here r = num %10 = 123%10 = 3(remainder)
        num = num //10                 #now num = num //10 = 123//10 i.e. 12---quotient
        rev = rev*10 + r               #now rev = rev*10 +r ----4*10 + 3 == 43
    print(rev)
else:
    rev = absnum % 10                        #now here rev= 1234 %10 = 4(remainder)
    absnum = absnum // 10                    #now num//10 i.e. 1234 //10 i.e. 123---quotient 
    while(absnum >0):
        r = absnum %10                       #here r = num %10 = 123%10 = 3(remainder)
        absnum = absnum //10                 #now num = num //10 = 123//10 i.e. 12---quotient
        rev = rev*10 + r                     #now rev = rev*10 +r ----4*10 + 3 == 43
    print(rev - 2*rev)                       #this print statement helps print the number in reverse wtih the (-ve) sign
