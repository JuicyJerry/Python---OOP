# __str__ method
# double underscore => dunder method 
class User:
    def __init__(self, name, email, pw): # dunder str이라고 부름, 원하는 인스턴스 값을 출력하기 위해서 dunder str를 사용한다.
        # 유저 인스턴스의 모든 변수를 지정해주는 메소드
        self.name = name
        self.email = email
        self.pw = pw


user1 = User("강영훈", "younghoon@codeit.kr", "123456")
user2 = User("이윤수", "yoonsoo@codeit.kr", "1q2w3e4e")

print(user1)
print(user2)
