# 모듈(module)이란 변수, 함수, 클래스 등을 모아놓은 파일입니다.
# 이런 모듈은 다른 곳에서 가져다 쓸 수 있습니다.

# from 모듈의 이름 import 불러올 변수/함수/클래스 이름

#from calculator import sum
from calculator import * # 모듈 안에 정의된 모든 변수/함수/클래스를 사용할 수 있다.

print(sum(3, 5))
print(difference(3, 5))
print(product(3, 5))
print(square(3))

# randint, uniform 함수

from random import randint
# 1 <= N <= 20를 만족하는 랜덤한 정수(난수) N을 리턴한다.
x = randint(1, 20)
print(x)

from random import uniform
# 0 <= N <= 1을 만족하는 랜덤한 소수(난수) N을 리턴한다.
x = uniform(0, 1)
print(x)
