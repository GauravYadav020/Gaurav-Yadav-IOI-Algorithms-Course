# Activity 1 - Fibonacci Series
a,b = 0,1
for i in range(10):
    print(a,end=" ")
    a,b = b,a+b

# Activity 2 - Factorial
n = int(input("\nEnter number: "))
fact = 1
for i in range(1,n+1):
    fact *= i
print("Factorial =", fact)

# Activity 3 - Armstrong Number Check
num = int(input("Enter number: "))
s = sum(int(d)**3 for d in str(num))
print("Armstrong" if s==num else "Not Armstrong")