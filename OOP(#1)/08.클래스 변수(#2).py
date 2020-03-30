# 인스턴스 자신만의 속성을 나타내는 변수는 인스턴스 변수
# 여러 인스턴스들이 공유하는 속성은?
class User:
    count = 0 # 클래스 변수

    def __init__(self, name, email, pw):
        self.name = name
        self.email = email
        self.pw = pw

        User.count += 1

user1 = User("강영훈", "younghoon@codeit.kr", "123456")
user2 = User("이윤수", "yoonsoo@codeit.kr", "1q2w3e4e")
user3 = User("훈영강", "hyk@codeit.kr", "12d345d6")

#user1.count = 5
User.count = 5

print(User.count)
print(user1.count) # 같은 이름의 클래스 변수(User.count) vs 같은 이름의 인스턴스 변수(user1.count) ; 후자
# 헷갈리기 때문에 클래스 변수에 값을 설정할때는 클래스 이름으로만 해야 한다.
print(user2.count)
print(user1.count)

# callee: 피호출인
# 한 클래스의 모든 인스턴스가 공유하는 속성이며 클래스 변수를 사용하면 됩니다.
# 클래스 변수의 값 읽는 법? (1. 클래스 이름.클래스 변수 이름, 2. 인스턴스 이름.클래스 변수 이름)
# 클래스 변수의 값 설정하기? (꾝! 클래스 이름.클래스 변수 이름), 2은 해당 인스턴스의 값이 바뀌는 것에 해당함므로 클래스 범위에서 값을 설정하는게 안정적임

# 클래스 변수와 인스턴스 변수 둘 다 쓴다면?
# 인스턴스 메소드는 인스턴스 변수, 클래스 변수 모두 사용 가능!
# 클래스 메소드는 인스턴스 변수 사용 불가!

# 인스턴스 없이도 필요한 정보가 있다면?
# 클래스 메소드 number_of_users
# user.count -> 인스턴스(클래스 메소드 number_of_users)가 하나도 없더라도 필요!

