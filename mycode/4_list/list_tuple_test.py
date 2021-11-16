 # packing
my_list1 = [20, 30, 40]
 # unpakcing
n1, n2, n3 = my_list1
print(n1, n2, n3)
my_list2 = list()
print(type(n1))

my_list1.append(10)     #맨 마지막에 추가
print(my_list1)
my_list1.extend([50,60])
print(my_list1)
my_list1.insert(0,10)   # 0번째 인덱스에서 원하는 값 input
print(type(my_list1))
print(my_list1)
my_list1[2] = 100
print(my_list1)
#list는 중복 허용!

#set - 중복 허용 X, 순서 유지 X
my_set = set(my_list1)
print(type(my_set))
print(my_set)

my_tuple = (10, 20, 30)
my_tuple2 = tuple()
print(my_tuple)
print(type(my_tuple))
#my_tuple[0] = 50        # tuple은 읽기 전용이라 따로 추가를 해줄 수 없다(read only list)
print(my_tuple)

num1 = (3)      # int
num2 = (3, )    # tuple!!
print(type(num1), type(num2))

#tuple usage
def swap(a, b):
    return (b,a)

a, b = swap(10, 20)
print(a)
print(b)
