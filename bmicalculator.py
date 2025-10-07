def calculate_bmi(weight, height):
    #Calculate the Body Mass Index (BMI) given weight (in kg) and height (in meters).

    if height <= 0:
        raise ValueError("Height must be greater than zero.")
    if weight < 0:
        raise ValueError("Weight cannot be negative.")
    return weight / (height ** 2)

def classify_bmi(bmi):
   # Classify the BMI into health categories.
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def get_float_input(prompt):
    #Get a float input from the user and handle potential errors.
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")

def main() -> None:
    print("BMI Calculator")
    print("----------------")

    # Get user input for weight
    while True:
        weight = get_float_input("Enter your weight in kilograms: ")
        if weight >= 0:
            break
        else:
            print("Weight cannot be negative. Please try again.")

    # Get user input for height
    while True:
        height = get_float_input("Enter your height in meters: ")
        if height > 0:
            break
        else:
            print("Height must be greater than zero. Please try again.")

    try:
        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)

        print(f"\nYour BMI is: {bmi:.2f}")
        print(f"Your BMI category is: {category}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
