a=int(input("enter the first length: "))
b=int(input("enter the second length: "))
c=int(input("enter the third length: "))

if a+b>c and a+c>b and b+c>a:
    print("you can make a triangle")
else:
    print("you cannot make a triangle :( ")

