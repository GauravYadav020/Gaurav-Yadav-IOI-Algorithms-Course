from datetime import datetime

# Activity 1 - Voting Eligibility
age = int(input("Enter age: "))
if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")

# Activity 2 - Current Date and Time
print(datetime.now())

# Activity 3 - Greeting Based on Time
hour = datetime.now().hour
if hour < 12:
    print("Good Morning")
else:
    print("Good Evening")