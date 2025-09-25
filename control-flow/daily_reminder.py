# Prompt for a Single Task
task = input("Enter task description: ")
priority = input("Enter task priority (high, medium, low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        reminder = f"{task} is a high priority task."
    case "medium":
        reminder = f"{task} is a medium priority task."
    case "low":
        reminder = f"{task} is a low priority task."
    case _:
        reminder = f"{task} is a task with unspecified priority."

if time_bound == "yes":
    reminder += " - that requires immediate attention today!"

print(f"Reminder: {reminder}")


