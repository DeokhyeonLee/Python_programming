"""
파이썬 모듈안에는 함수와 클래스를 선언할 수 있다.
"""


def add(n1, n2):
    #pass
    #함수 선언을 했지만 body 작성을 안했을 때, 말 그대로 내용 pass

    return n1 + n2

print(add(10,20))

#add(10,20)
print(add)

add2 = lambda n1, n2 : n1 + n2          # :을 기준으로 왼쪽이 parameter, 오른쪽이 Value
print(type(add2))
print(add2(100,200))


#class 선언
class User:
    # 생성자 선언
    def __init__(self, name):
        self.name = name            #self는 자바의 this!!

    #toString()
    def __str__(self):
        return self.name

#객체 생성
user = User("파이썬")
print(user)

#문자열 타입 list 선언
cat_list = list('cat')
print(cat_list)

