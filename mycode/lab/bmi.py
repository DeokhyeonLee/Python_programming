
def print_bmi(name, height_cm, weight):
    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)

    print(f'{name} BMI is {bmi:.1f}')