# 1. decorator 꾸며진 함수
def print_hello():
    print("안녕하세요!")


def add_print_to(original): # decorator function
    def wrapper():
        print("함수 시작")
        original()
        print("함수 끝")
    return wrapper


#add_print_to(print_hello)
#add_print_to(print_hello)()    # https://www.codeit.kr/community/threads/8720
print_hello = add_print_to(print_hello)
print_hello()

# none값이 뜨지 않은 건 wrapper 함수가 실행되지 않았기 때문이다.
