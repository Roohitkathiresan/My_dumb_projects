i = float(input("enter an value to get operated :"))
square = i**2
square_root =i**0.5
cube = i**3
print("1.square")
print("2.square root")
print("3.cube")
choice = int(input("enter your choice:"))
if choice==1:
    print(f"square of the number is{square} ")
elif choice==2:
    print(f"square root of the number is{square_root} ")
elif choice==3:
    print(f"cube of the number is {cube} ")
