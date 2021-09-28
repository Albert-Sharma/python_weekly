num =abs(int(input()))
digits =1
while(num>9):                   #..for any one digit number i.e. 1-9
    num = num //10
    digits = digits +1
print(digits)