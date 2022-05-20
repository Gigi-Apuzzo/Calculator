import math, time
x = 1
pi = 3.14159

print("Calculator")
time.sleep(x)
name = input("Enter name: ")
name = name.strip().capitalize()
print("Welcome", name)
print("")

print("     **Choose an Option**")
time.sleep(0.1)
print("     1. Addition")
time.sleep(0.1)
print("     2. Subtraction")
time.sleep(0.1)
print("     3. Multiplication")
time.sleep(0.1)
print("     4. Division")
time.sleep(0.1)
print("     5. Square Root")
time.sleep(0.1)
print("     6. Circle Calculator")
time.sleep(x)

print("")
print("Select an option 1-6")
time.sleep(x)
s = int(input("Select: "))

if s == 1:
    n1 = int(input("Input 1st Number: "))
    time.sleep(x)
    n2 = int(input("Input 2nd Number: "))
    time.sleep(x)
    ans = n1+n2
    print(ans)
    time.sleep(x)
  
elif s == 2:
    n1 = int(input("Input 1st Number: "))
    time.sleep(x)
    n2 = int(input("Input 2nd Number: "))
    time.sleep(x)
    ans = n1-n2
    print(ans)
    time.sleep(x)
  
elif s == 3:
    n1 = int(input("Input 1st Number: "))
    time.sleep(x)
    n2 = int(input("Input 2nd Number: "))
    time.sleep(x)
    ans = n1*n2
    print(ans)
    time.sleep(x)
  
elif s == 4:
    n1 = int(input("Input 1st Number: "))
    time.sleep(x)
    n2 = int(input("Input 2nd Number: "))
    time.sleep(x)
    ans = n1/n2
    print(ans)
    time.sleep(x)
  
elif s == 5:
    n = int(input("Input Number: "))
    time.sleep(x)
    ans = math.sqrt(n)
    print(ans)
    time.sleep(x)
  
elif s == 6:
    radius = int(input("Enter Radius: "))
    diameter = (2*radius)
    circumference = (2*pi*radius)
    area = (pi*(radius*radius))
    time.sleep(x)
    print("Diameter =", diameter)
    time.sleep(0.1)
    print("Circumference =", circumference)
    time.sleep(0.1)
    print("Area =", area)
    time.sleep(x)

else:
    print("Invalid Selection, please try again.")