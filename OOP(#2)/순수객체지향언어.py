# 파이썬으로 객체 지향 프로그래밍을 배우는 이유?
# 파이썬이 "순수 객체 지향 언어"라서 => 파이썬의 모든 것이 객체라는 뜻!

class User:
    count = 0

    def __init__(self, name, email, pw):
        self.name = name
        self.email = email
        self.pw = pw

        User.count += 1

    def say_hello(self):
        print("안녕하세요! 저는 {}입니다!".format(self.name))

user1: User = User("Young", "youn@codeit.com", "1234")

print(type(user1)) # 순수객체지향언아.py의 속성
print(type("user1"))
print(type([]))
print(type({}))
print(type(()))

def print_hello():
    print("안녕하세요.")

print(type(print_hello))

in_list = []
in_list.append(1)
in_list.append(3)
in_list.append(5)

print(in_list)
print(type(in_list))


# 파이썬의 모든 것들은 특정 클래스의 인스턴스로 생성된다는 것을 알 수 있다.
