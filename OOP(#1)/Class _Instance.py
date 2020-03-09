class User:
    pass

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

# 각 변수가 각자 개인적으로 가지고 있는 변수를 인스턴스 변수라고 한다. (name, email, password)
print(user1.name)
print(user2.password)
print(user1.age)
