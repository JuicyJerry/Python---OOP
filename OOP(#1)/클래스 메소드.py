# 인스턴스 메소드: 인스턴스 변수의 값을 읽거나 설정하는 메소드
# 클래스 메소드: 클래스 변수의 값을 읽거나 설정하는 메소드

class User:
    count = 0

    def __init__(self, name, email, pw):
        # 유저 인스턴스의 모든 변수를 지정해주는 메소드
        self.name = name
        self.email = email
        self.pw = pw

        User.count += 1

    def say_hello(self):
        print("안녕하세요! 저는 {}입니다.!".format(self.name))

    def __str__(self):
        return "사용자: {}, 이메일: {}, 비밀번호: ******".format(self.name, self.email)

    #@classmethod
    #def number_of_user(cls):
     #   print("총 유저 수는 : {}입니다.".format(cls.count))

    def number_of_users(self):
        print("총 유저 수는: {}입니다.".format(User.count)) # <- #26, User.count / self 사용 x\


# 인스턴스 메소드 사용:
user1 = User("강영훈", "younghoon@codeit.kr", "123456")
user2 = User("이윤수", "yoonsoo@codeit.kr", "1q2w3e4e")

User.say_hello(user1)
user1.say_hello()   # 인스턴스 자신이 첫 번째 파라티머로 자동 전달!


# vs 클래스 메소드 사용
    @classmethod
    def number_of_users(cls):
        print("총 유저 수는: {}입니다.".format(cls.count)) # cls.count == user.count

User.number_of_users()   # 첫 번째 파라미터로 클래스 자동 전달! 그래서 괄호 안이 비어있음(@classmethod로 만들어줬기 때문)
user1.number_of_users()  # 첫 번째 파라미터로 클래스 자동 전달! 그래서 괄호 안이 비어있음 (@classmethod로 만들어줬기 때문)
