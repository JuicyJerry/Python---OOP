# 인스턴스 메소드, 클래스 메소드
# 정적 메소더(static method)
class User:
    count = 0

    def __init__(self, name, email, pw):
        self.name = name
        self.email = email
        self.pw = pw

        User.count += 1

    def say_hello(self):
        print("안녕하세요! 저는 {}입니다!".format(self.name))


    # 인스턴스 메소드 __str__는 인스턴스 변수인 self.name, self.email을 사용한다.
    def __str__(self):
        return "사용자: {}, 이메일: {}, 비밀번호: ******".format(self.name, self.email)

    # 클래스 메소드 number_of_user는 클래스 변수인 cls.count를 사용한다.
    @classmethod
    def number_of_users(cls):
        print("총 유저 수는: {}입니다".format(cls.count))

    # is_valid_email 메소드에선 아무 변수도 사용하고 있지 않다.
    #인스턴스 변수나 클래스 변수 중 아무것도 사용하지 않을 메소드라면 정적 메소드로 만들면 됩니다.
    # 그러니까 어떤 속성을 다루지 않고, 단지 기능(행동)적인 역할만 하는 메소드를 정의할 때 정적 메소드로 정의하면 됩니다.
    @staticmethod
    def is_valid_email(email_address):
        return "@" in email_address

# 같은 자동 전달되는 파라미터가 없습니다.
# 그리고 정적 메소드는 아래 코드처럼 인스턴스, 클래스 두 가지 모두를 통해 사용 가능합니다.
print(User.is_valid_email("taehosung"))
print(User.is_valid_email("taehosung@codeit.kr"))

#print(user1.is_valid_email("taehosung"))
#print(user1.is_valid_email("taehosung@codeit.kr"))

# 인스턴스 메소드
def __str__(self):
    return "사용자: {}, 이메일: {}, 비밀번호: ******".format(self.name, self.email)

# 클래스 메소드
@classmethod
def number_of_users(cls):
    print("총 유저 수는: {}입니다".format(cls.count))

# 정적 메소드
@staticmethod
def is_valid_email(email_address):
    return "@" in email_address
