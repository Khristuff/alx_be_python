age = int(input("What's your age? "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")

score = int(input("Enter your score: "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print("Your grade is:", grade)

#Madlibs game
adjective_1 = input("Enter an adjective ")
adjective_2 = input("Enter an adjective ")
adjective_3 = input("Enter an adjective ")
adjective_4 = input("Enter an adjective ")

print(f"On a beautiful {adjective_1} day, I went to the zoo. I saw a funny {adjective_2} monkey swinging from the trees. Then, I spotted a majestic {adjective_3} lion lounging in the sun. What a wild and {adjective_4} experience!")

