n = int(input("enter the number of elements: "))

a,b = 0,1

print("fibonacci series:")
while a <= n:
    print(a)
    a,b = b,a+b
print()