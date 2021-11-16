"""
나이 = 현재년도 - 태어난년도 + 1
태어난 년도는 input() 함수 사용
"""

#from 모듈명 import 클래스명 또는 함수명

from datetime import datetime as dt
print(dt.today())
print(dt.today().year)      #year는 메소드지만 ()x/cuz=property _like a getter of java
print(dt.today().month)

current_year = dt.today().year
print("태어난 년도를 입력하세요.")
birth_year = int(input())
#print(current_year, birth_year)
age = current_year - birth_year + 1

if 17 <= age < 20:
    print("고등학생입니다.")
elif 20 <= age < 27:
    print("대학생입니다.")
else:
    print("학생이 아닙니다.")