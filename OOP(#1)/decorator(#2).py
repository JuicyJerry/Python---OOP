def add_print_to(original): # decorator function
    def wrapper():
        print("함수 시작")
        original()
        print("함수 끝")
    return wrapper

@add_print_to # "@" '함수명'을 꾸며주라는 의미 / 데코레이터: 기존의 함수에 새로운 기능 추가!
def print_hello():
    print("안녕하세요!")

print_hello()


# 데코레이터
#  메인 구문이 있고, 여기에  부가적인 구문을 추가하고 싶을때 말이다. 그리고 이 부가적인 구문을 반복해서 사용하고 싶은 경우도 있다. 이때 부가적인(그리고 반복적인) 작업을 decorator 로 선언해서 자유롭게 사용이 가능하다는 것이다.
# 출처: https://bluese05.tistory.com/30 [ㅍㅍㅋㄷ]
