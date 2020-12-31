#BMI calculator by Bartosz Golonka

height = int(input("What's your height in cm: "))
height = height/100
weight = int(input("What's your weight in kg: "))

BMI = weight/(height**2)
BMI = int(BMI)

if BMI < 8.5:
    print("Your BMI index is " + str(BMI) + " and it's critical. You are underweight.")
elif 8.5 < BMI < 18.5:
    print("Your BMI index is " + str(BMI) + ". You are underweight.")
elif 19 < BMI <25:
    print("Your BMI index is " + str(BMI) + ". Your weight is normal.")
elif 25.5 < BMI < 30:
    print("Your BMI index is " + str(BMI) + ". You are overweight")
else:
     print("Your BMI index is " + str(BMI) + " and it's critical. You are overweight.")
