Num1= int(input("Enter Your Number: "))
answer = 0
copynum = Num1

while copynum>0:
    single = copynum%10
    single = single**3
    answer = answer + single
    copynum = copynum//10

if answer == Num1:
    print("Your number ",Num1,"is an amstrong number")
else:
    print("Your number ",Num1,"is not an amstrong number")
