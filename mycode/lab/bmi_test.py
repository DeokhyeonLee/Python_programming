"""
이름, 키, 몸무게를 입력받기
heigth_m = height_cm / 100
bmi = weight / (height**2)
"""

print("input your name")
name = input()

print("input your height(cm)")
heigth_cm = int(input())
heigth_m = heigth_cm / 100

print(heigth_m)

print("input your weight")
weight = int(input())

bmi = weight / (heigth_m ** 2)

print(f'{name}BMI is {bmi:.1f}')