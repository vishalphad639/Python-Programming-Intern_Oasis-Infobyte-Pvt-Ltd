def calculate_bmi(weight, height):
    """Calculate BMI based on weight and height."""
    return weight / (height ** 2)

def classify_bmi(bmi):
    """Classify BMI into categories."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def get_user_input():
    """Get weight and height from the user with input validation."""
    while True:
        try:
            weight = float(input("Enter your weight in kg: "))
            if weight <= 0:
                raise ValueError("Weight must be positive.")
            height = float(input("Enter your height in meters: "))
            if height <= 0:
                raise ValueError("Height must be positive.")
            return weight, height
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")

def main():
    print("Welcome to the BMI Calculator!")
    weight, height = get_user_input()
    bmi = calculate_bmi(weight, height)
    category = classify_bmi(bmi)
    print(f"Your BMI is: {bmi:.2f}")
    print(f"Category: {category}")

if __name__ == "__main__":
    main()
def main():
    print("Welcome to the BMI Calculator!")
    weight, height = get_user_input()
    bmi = calculate_bmi(weight, height)
    print(f"Debug: Weight = {weight}, Height = {height}, BMI = {bmi:.2f}")  # Debug print
    category = classify_bmi(bmi)
    print(f"Your BMI is: {bmi:.2f}")
    print(f"Category: {category}")


# to running this programme use following command in your terminal:- python bmi_calculator.py
