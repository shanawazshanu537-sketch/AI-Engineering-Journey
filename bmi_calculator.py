def calculate_bmi(weight, height):
    bmi = weight / (height ** 2) #bodymassindex(bmi) formula
    return bmi

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "underweight"    
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "overweight"
    else: return "obese"

weight = float(input("your weight(kg): "))
height = float(input("your height(m): "))

bmi = calculate_bmi(weight , height)
category = get_bmi_category(bmi)

print(f"Your BMI is {bmi}")
print(f"Category: {category}")

