# max, min 함수 (최댓값, 최솟값)
# sum 함수 (list, tuple, dict에 있는 숫자형 요소들의 합을 리턴, dict를 파라미터로 넘기면 key들의 합을 리턴)
# ternary expression : 게 불린(Boolean) 값에 따라 다른 값을 리턴하는 구문을 ternary expression이라고 한다.
# list comprehension
#1
for x in int_list:
    squares.append(x**2)

print(squares)
#1 : [] 안에 원하는 값을 리턴하는 식 (x**2) 뒤에

#2
int_list = [1, 2, 3, 4, 5, 6]
squares = [x**2 for x in int_list]

print(squares)
#2 : for문을 써줍니다(for x in int_list).


# zfiil 메소드
# 이 메소드는 문자열을 최소 몇 자리 이상을 가진 문자열로 변환시켜줍니다.
# 이때 만약 모자란 부분은 왼쪽에 “0”을 채워주는데요.

print("1".zfill(6))
print("333".zfill(2))
print("a".zfill(8))
print("ab".zfill(8))
print("abc".zfill(8))
