# This is a simple Python script that demonstrates the use of variables and their data types. It defines several variables related to personal information, prints them out, and then displays the data type of each variable.

name = "Jannah Elizabeth Delan"
age = 24
height_cm = 160.02
is_a_college_graduate = True
current_job = None

print("About Me")
print("Full Name:", name)
print("Age:", age)
print("Height:", str(height_cm) + "cm")
print("Is a College Graduate:", is_a_college_graduate)
print("Current Job:", current_job) 

print()

print("Variables and Data Types")
print("name = (" + str(type(name)) + ")")
print("age = (" + str(type(age)) + ")")
print("height_cm = (" + str(type(height_cm)) + ")")
print("is_a_college_graduate = (" + str(type(is_a_college_graduate)) + ")")
print("current_job = (" + str(type(current_job)) + ")")