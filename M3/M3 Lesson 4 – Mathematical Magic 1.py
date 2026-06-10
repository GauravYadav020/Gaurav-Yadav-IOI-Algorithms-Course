# Activity 1 - Check Even or Odd
num = int(input("Enter a number: "))
print("Even" if num%2==0 else "Odd")

# Activity 2 - Sum of First N Numbers
n = int(input("Enter n: "))
print(n*(n+1)//2)

# Activity 3 - Multiples of 5
for i in range(1,51):
    if i % 5 == 0:
        print(i)