a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))
d = (b**2) - (4*a*c)
if d > 0:
    root1 = (-b + d**0.5) / (2*a)
    root2 = (-b - d**0.5) / (2*a)
    print(f"The roots are real and distinct: {root1} and {root2}")
elif d == 0:
    root = -b / (2*a)
    print(f"The roots are real and equal: {root}")
else: 
    root1 = (-b + d**(0.5)) / (2*a)
    root2 = (-b - d**(0.5)) / (2*a)
    print(f"The roots are complex: {root1} and {root2}")

