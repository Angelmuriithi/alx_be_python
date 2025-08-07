def get_user_input():
    task = input("Enter your task: ").strip()
    
    while True:
        priority = input("Priority (high/medium/low): ").strip().lower()
        if priority in ['high', 'medium', 'low']:
            break
        else:
            print("Please enter a valid priority: high, medium, or low.")

    while True:
        time_bound = input("Is it time-bound? (yes/no): ").strip().lower()
        if time_bound in ['yes', 'no']:
            break
        else:
            print("Please enter 'yes' or 'no'.")

    return task, priority, time_bound

def generate_reminder(task, priority, time_bound):
    match priority:
        case "high":
            message = f"Reminder: '{task}' is a high priority task"
        case "medium":
            message = f"Note: '{task}' is a medium priority task"
        case "low":
            message = f"Note: '{task}' is a low priority task"

    if time_bound == "yes":
        message += " that requires immediate attention today!"
    else:
        message += ". Consider completing it when you have free time."

    print("\n" + message)


if __name__ == "__main__":
    task, priority, time_bound = get_user_input()
    generate_reminder(task, priority, time_bound)
    print("\n✅ Well done on completing this project! Let the world hear about this milestone achieved.")
