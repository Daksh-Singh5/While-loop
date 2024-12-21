Num1= int(input("Enter Your Number: "))
answer = 0
copynum = Num1

while copynum>0:
    copynum = copynum//10
    answer+=1
print("Your number",Num1,"is of",answer,"digits")
