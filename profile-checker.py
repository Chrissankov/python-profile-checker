# Getting input from the user 
print("**** Waiting for User Information ****")
name = input("Enter your name: ").strip()
age = int(input("Enter your age: "))
gpa = float(input("Enter your GPA(0.0 -> 5.0): "))
interest = input("Enter your field of interest: ").strip()
graduated = input("Are you graduated: 'Yes' or 'No'? ").strip().lower()

# Printing the user input in a neat format (First Part)
print("\n**** Displaying User Information ****")
print("Name:", name)
print("Age:", age)
print("GPA:", gpa)
print("Field of Interest:", interest)
print("Graduated:", graduated.capitalize(), end="\n\n")

# Eligible for ... (Part 2)
if age < 25 and gpa >= 3.5 and graduated == "yes":
    print("You are eligible for a scholarship.")
elif age < 30 and gpa >= 2.5:
    print("You are eligible for an internship.")
else:
    print("You are not eligible at this time. Please apply again later.")