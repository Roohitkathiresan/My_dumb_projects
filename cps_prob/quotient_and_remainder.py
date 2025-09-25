n1 = int(input("enter n1 value :"))
n2 = int(input("enter n2 value :"))
if n2==0:
    print("Not defined")
else:
    quo = n1/n2
    rem = n1%n2
    print(f"\nquotient = {quo}\nremainder = {rem}")
