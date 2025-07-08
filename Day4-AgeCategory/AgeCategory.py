# AgeCategory.py

def determine_age_category(age):
    if age < 0:
        return "Invalid age"
    elif age < 13:
        return "Child"
    elif age < 20:
        return "Teenager"
    elif age < 60:
        return "Adult"
    else:
        return "Senior"

def main():
    try:
        age = int(input("Enter your age: "))
        category = determine_age_category(age)
        print(f"You are a {category}.")
    except ValueError:
        print("Please enter a valid integer for age.")

if __name__ == "__main__":
    main()
