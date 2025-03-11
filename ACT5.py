age = int(input("What is your age"))

if age < 0:
    print("Invalid age entered.")
elif age <= 12:
    print("Child")
elif age <= 19:
    print("Teen")
elif age <= 64:
    print("Adult")
else:
    print("Senior")
