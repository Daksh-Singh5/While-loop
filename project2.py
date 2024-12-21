Num1= int(input("Enter Your Number: "))
answer = 0
copynum = Num1

while copynum>0:
    single = copynum%10
    answer=(answer*10)+single
    copynum = copynum//10
print(answer)

