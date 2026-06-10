# Activity 1 - Prime Check
n = int(input("Enter number: "))
flag = True
for i in range(2,n):
    if n%i==0:
        flag = False
        break
print("Prime" if flag and n>1 else "Not Prime")

# Activity 2 - Reverse Number
num = input("Enter number: ")
print(num[::-1])

# Activity 3 - Count Digits
num = input("Enter number: ")
print("Digits:", len(num))