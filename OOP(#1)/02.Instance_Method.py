# 객체: 속성(=> 변수), 행동(=>함수; 메소드) 나타냄
# 메소드의 종류: 1. 인스턴스 메소드, 클래스 메소드, 정적 메소드
# 1. 인스턴스 메소드: 인스턴스 변수를 사용하거나, 인스턴스 변수에 값을 설정하는 메소드

class User:
    def say_hello(some_user):
    # 인사 메시지 출력 메소드
        print("안녕하세요! 저는 {}입니다.!".format(some_user.name))



# 각 변수가 각자 개인적으로 가지고 있는 변수를 인스턴스 변수라고 한다. (name, email, password)
user1 = User()
user2 = User()
user3 = User()

user1.name = "김대위"
user1.email = "captain@codeit.kr"
user1.password = "12345"

user2.name = "강영훈"
user2.email = "strong@codeit.kr"
user2.password = "65433"

user3.name = "홍명보"
user3.email = "myeongbo@codeit.kr"
user3.password = "123444"


# 인스턴스 메소드 사용법 / 클래스 이름.메소드 이름(인스턴스)
User.say_hello(user1)
User.say_hello(user2)
User.say_hello(user3)

# 인스턴스 메소드 또다른 사용법 / 인스턴스이름.메소드 이름()
User.say_hello(user1) == user1.say_hello()
#User.say_hello(user1, user1)

class User:
    def say_hello(some_user):
    # 인사 메시지 출력 메소드
        print("안녕하세요! 저는 {}입니다.".format(some_user.name))

    def login(some_user, my_email, my_password):
        # 로그인 메소드
        if (some_user.email == my_email and some_user.password == my_password):
            print("로그인 성공, 환영합니다.")
        else:
            print("로그인 실패, 없는 아이디이거나 잘못된 비밀번호입니다.")

user1 = User()

user1.name = "김대위"
user1.email = "captain@codeit.kr"
user1.password = "12345"

#user1.login(user1, "captain@code.kr", "12345")
user1.login("captain.codeit.kr", "12345")
