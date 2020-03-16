# 객체
# 가변 타입 객체: 한 번 생성한 인스턴스의 속성 변경 가능
    # 리스트 클래스 / list, dict, 직접 작성하는 클래스(로 만든 인스턴스)

# 불변 타입 객체: 한 번 생성한 인스턴스의 속성 변경 불가
    # 튜플 클래스 / bool, int, float, str, tuple

# 어떤 타입이냐에 따라 같은 상황에서도 다른 결과!

mutable_object = [1, 2, 3]
immutable_object = (1, 2, 3)

# 불가변 타입
#mutable_object[0] = 4
#print(mutable_object)

#immutable_object[0] = 4
#print(immutable_object) # error, but 객체 자체는 바꿀 수는 있다.

tuple_x = (6, 4)
tuple_x = (4, 1)
tuple_x = (4, 1, 7)

print(tuple_x)


# 가변 타입
list_x = []
list_x.append(4)
list_x.append(1)
list_x.append(3)

print(list_x)

# 인스턴스는 먼저 만들고 이후에 정의해도 된다 (x) => 클래스를 미리 정의해놓지 않으면 해당 클래스의 인스턴스를 만들 수 없습니다.

# 파이썬은 순수 객체 지향 언어이다.
# 클래스는 인스턴스를 만드는 틀의 역할을 한다.
# 파이썬으로 코드를 쓰면 의도하지 않았어도 기본적으로 객체 지향 프로그래밍을 하게 된다.
# type 함수를 사용하면 인스턴스의 클래스를 확인할 수 있다.
