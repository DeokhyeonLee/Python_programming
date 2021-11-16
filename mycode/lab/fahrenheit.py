
#섭씨를 화씨로 변환하는 함수
def fah_convert(celsius):
    pass
    return ((9/5) * float(celsius)) + 32

print("변환하고 싶은 섭씨 온도를 입력하세요")
user_input = input()
print(type(user_input), user_input)
fah  = fah_convert(user_input)

#print("섭씨온도 : " + user_input)   #파이썬은 같은 타입일 경우만 + 가능! JAVA와 차이점임!!
print("섭씨온도 : ",float(user_input))
print(f"섭씨온도 : {user_input}") #f를 사용하면 정적, 동적 문자열을 같이 사용할 수 있음.
print("화씨온도 : {0:.2f}".format(fah))  #format 사용법 : {}안에다가 fah를 넣어라
print(f"화씨온도 : {round(fah,2)}")