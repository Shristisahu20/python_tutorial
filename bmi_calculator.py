def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi


def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def main():
    print("Welcome to the BMI Calculator!")
    
    # Prompt user for weight and height
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
    except ValueError:
        print("Please enter valid numerical values for weight and height.")
        return
    
    # Calculate BMI
    bmi = calculate_bmi(weight, height)
    
    # Classify BMI and display result
    category = classify_bmi(bmi)
    
    print("\nBMI Result:")
    print("Your BMI is: {:.2f}".format(bmi))
    print("Category: {}".format(category))


if __name__ == "__main__":
    main()
