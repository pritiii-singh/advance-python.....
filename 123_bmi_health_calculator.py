"""
Project 123: BMI & Caloric Requirement Calculator
Concepts: mathematical formulas, branching conditions, user metrics conversion.
"""
def calculate_bmi(weight_kg, height_m):
    return weight_kg / (height_m ** 2)

def bmi_category(bmi):
    if bmi < 18.5: return "Underweight"
    elif bmi < 25.0: return "Normal weight"
    elif bmi < 30.0: return "Overweight"
    else: return "Obese"

def calculate_bmr(weight_kg, height_cm, age, gender):
    # Mifflin-St Jeor formula
    if gender.lower() == 'm':
        return (10 * weight_kg) + (6.25 * height_cm) - (5 * age) + 5
    else:
        return (10 * weight_kg) + (6.25 * height_cm) - (5 * age) - 161

def main():
    print("=== HEALTH & BMI CALCULATOR ===")
    system = input("Metric (kg, cm) or Imperial (lbs, inches)? (m/i): ").strip().lower()
    if system == 'i':
        lbs = float(input("Weight in lbs: "))
        inches = float(input("Height in inches: "))
        weight_kg = lbs * 0.453592
        height_m = inches * 0.0254
        height_cm = height_m * 100
    else:
        weight_kg = float(input("Weight in kg: "))
        height_cm = float(input("Height in cm: "))
        height_m = height_cm / 100

    age = int(input("Age: "))
    gender = input("Gender (m/f): ").strip().lower()

    bmi = calculate_bmi(weight_kg, height_m)
    category = bmi_category(bmi)
    bmr = calculate_bmr(weight_kg, height_cm, age, gender)

    print(f"\n--- Health Summary ---")
    print(f"BMI: {bmi:.1f} ({category})")
    print(f"Basal Metabolic Rate (BMR): {bmr:.0f} kcal/day")
    print(f"Maintenance Calories (Moderate exercise): {bmr * 1.55:.0f} kcal/day")

if __name__ == "__main__":
    main()
