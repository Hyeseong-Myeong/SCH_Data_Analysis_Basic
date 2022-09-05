import math

a = 10
print(a)

#float() => 정수를 실수형으로 변환
#명시적 변환
a = float(10)
print(a)


a = 10
b = 3
#실수형으로 a / b를 출력
#묵시적 변환
print(a / b)

#input_value = input("input num:")
#input은 항상 문자열로 인식
#input_value = int(input("input_num:"))
#print(input_value)

a = 10.7
print(a)
print(int(a))
print(math.floor(a))

a = 100
b = 10
print(a + b)
print(str(a + b))
print(str(a) + str(b))
#print(type(a))
