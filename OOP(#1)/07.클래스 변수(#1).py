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

print(user1)
print(User.count)


# callee: 피호출인
# __init__을 __int__로 써놓고 나온 에러 때문에 고생했음..
