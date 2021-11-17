#from bmi import print_bmi
import mycode.lab.bmi as bmi

def main():
    print("input your name")
    name = input()

    print("input your height")
    height_cm = int(input())

    print("input your weight")
    weight = int(input())

    print_bmi(name, height_cm, weight)

print(__name__)
if __name__ == "__main__":
    main()