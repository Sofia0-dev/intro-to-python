# bmi calc

# Below 18.5	Underweight
# 18.5 to 24.9	Healthy / Normal Weight
# 25.0 to 29.9	Overweight
# 30.0 to 34.9	Class 1 Obesity
# 35.0 to 39.9	Class 2 Obesity
# 40.0 or greater	Class 3 Obesity (Severe Obesity)

weight = input("please enter your weight in kgs: ")
height = input("please enter your height in m: ")

w = float(weight)
h = float(height)

bmi = w / h ** 2  # 10**3 math.pow(h,2) h*h


#age==19
if bmi < 18.5:
    print("you are underweight")
elif bmi >= 18.5 and bmi <= 24.9:
    print("you are normal")
elif bmi >= 25.0 and bmi <= 29.9:
    print("you are obese")
elif bmi >= 30 and bmi <= 34.9:
    print("you are thundering")
elif bmi >= 35 and bmi <= 39.9:
    print("you are thovering")
else:
    print("you are overweight")

