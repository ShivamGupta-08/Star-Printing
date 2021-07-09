print("Enter your number")
int1 = int(input())
print("Enter 0 or 1")
two = int(input())
new =bool(two)
print(new)
star = "*"

if new == True:
    x = range(int1+1)
    for n in x:
     print("*"*n)

elif new==False :
    for i in range(int1, 0,-1):
        print("*" * i)



