# Prompt for a Single Task
Task = input("Enter task description: ")
Priority = input("Enter task priority (high, medium, low): ")
Time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        reminder = f"{Task} is a high priority task."
    case "medium":
        reminder = f"{Task} is a medium priority task."
    case "low":
        reminder = f"{Task} is a low priority task."
    case _:
        reminder = f"{Task} is a task with unspecified priority."

if Time_bound == "yes":
    reminder += " - that requires immediate attention today!"

print(f"Reminder: {reminder}")


