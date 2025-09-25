n1 = int(input("enter the value of n1 :"))
n2 = int(input("enter the value of n2 :"))
n3 = int(input("enter the value of n3 :"))
if n1>n2 and n1>n3:
    print("n1 is big")
    
elif n2>n3 and n2>n1:
    print("n2 is big")
elif n2<n3 and n1<n3:
    print("n3 is big")

elif n1==n2 and n2>n3:
    print("both n1 and n2 are greater and equal")
elif n2==n3 and n3>n1:
    print("both n2 and n3 are greater and equal")
elif n3==n1 and n1>n2:
    print("both n3 and n1 are greater and equal")
elif n2==n1==n3 :
    print("all are equal")
