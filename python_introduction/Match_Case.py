#Match Case
day = input("Enter a day of the week (Monday-Sunday): ").lower()

match day:
    case "monday":
        print("Ugh, Mondays...")
    case "tuesday":
        print("Just another workday...")
    case "wednesday":
        print("We're halfway through the week!")
    case "thursday":
        print("Almost there...")
    case "friday":
        print("TGIF!")
    case "saturday" | "sunday": #Match multiple values with pipe(|)
        print("It's the weekend!")
    case _:
        print("That's not a valid day of the week.")
    
#Using match case to determine the type of a variable
value = input("Enter a value (number or string): ")

match value:
    case int():
        print("You entered an integer.", value)
    case str():
        print("You entered a string.", value)
    case _:
        print("You entered a value of unknown type.", value)
    
#Using match case with guards
"""
age = int(input("Enter your age: "))
match age:
    case 18 | 19: #Match multiple values with pipe(|)
        if age >= 18 and has_id(user): #Guard condition
            print("You are eligible to vote.")
        else:
            print("You need a valid ID to vote.")
    case _:
        print("You are not eligible to vote yet.")
"""
import random
secret_number = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))
match guess:
    case n:
        if n >= 1 or n <= 10: #Guard condition
            print("Congratulations, you guessed it.")
        elif n > 10:
            print("Oops, your guess is too high. Try again.")
        elif n < 1:
            print("Nope, your guess is a bit low. Give it another shot.")
        
        