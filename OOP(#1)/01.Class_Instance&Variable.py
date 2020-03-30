# user 객체에 속성, 행동이 존재
# class instance / class는 객체의 틀, 객체 = 인스턴스
# 클래슬 객체를 만든다. 클래스로 인스턴스를 만든다.
class User:
    pass

user1 = User()
user2 = User()
user3 = User()

# instance variable 인스턴스 변수 (user1.name, user1.email, user1.password)
user1.name = "김대위"
user1.email = "captain@codeit.kr"
user1.password = "12345"

user2.name = "강영훈"
user2.email = "strong@codeit.kr"
user2.password = "65433"

user3.name = "홍명보"
user3.email = "myeongbo@codeit.kr"
user3.password = "123444"

# 각 변수가 각자 개인적으로 가지고 있는 변수를 인스턴스 변수라고 한다. (name, email, password)
print(user1.name)
print(user2.password)
print(user1.age)
