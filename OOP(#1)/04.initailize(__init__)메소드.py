class User:
    def initialize(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
# https://thebook.io/006888/partxt/xa/04/

user1 = User() # 유저 생성
user1.initialize("Young", "young@codeit.kr", "123456") # 유저 인스턴스 초기값 설정

user2 = User()
user2.initialize("Yoonsoo", "yoonsoo@codeit.kr", "abcdef")

user3 = User()
User.initialize(user3, "Taeho", "taeho@codeit.kr", "123abc")

user4 = User()
User.initialize(user4, "Lisa", "lisa@codeit.kr", "abc123")



print(user1.name, user1.email, user1.password)
print(user2.name, user2.email, user2.password)
print(user3.name, user3.email, user3.password)
print(user4.name, user4.email, user4.password)


# magic method(특수 메소드: 특정 상황에서 자동으로 호출되는 메소드)
# __init__ : 인스턴스가 생성될 때 자동으로 호출
class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
# https://thebook.io/006888/partxt/xa/04/

user1 = User("Youn g","young@codeit.kr", "123456")
# 1. User 인스턴스 생성
# 2. __init__ 메소드 자동 호출
# 2-1. self <- User인스턴스
# 2-2. 나머지 파라미터들이 순서대로 들어간다.
# 2-3. 인스턴스 변수들의 초깃값 설정


user2 = User("Yoonsoo", "yoonsoo@codeit.kr", "abcdef")

user3 = User("Taeho", "taeho@codeit.kr", "123abc")

user4 = User("Lisa", "lisa@codeit.kr", "abc123")

print(user1.name, user1.email, user1.password)
print(user2.name, user2.email, user2.password)
print(user3.name, user3.email, user3.password)
print(user4.name, user4.email, user4.password)
