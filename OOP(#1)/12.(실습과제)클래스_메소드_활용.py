class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    @classmethod
    def from_string(cls, string_params):
        # 유저 인스턴스를 생성해서 리턴하다.
        parameter_string = string_params.split(",")
        name = parameter_string[0]
        email = parameter_string[1]
        password = parameter_string[2]
        # younghoon = cls(name, email, password)

        return cls(name, email, password)
        # return younghoon
        # 클래스 메소드의 첫번째 파라미터 cls로  User 클래스가 자동 전달된다고 배웠습니다.
        # cls(...) == User(...)

    @classmethod
    def from_list(cls, list_params):
        # 유저 인스턴스를 생성해서 리턴하다.
        #parameter_list = list(list_params)
        name = list_params[0]
        email = list_params[1]
        password = list_params[2]
        # yoonsoo = cls(name, email, password)

        return cls(name, email, password)
        # return yoonsoo
        # 클래스 메소드의 첫번째 파라미터 cls로  User 클래스가 자동 전달된다고 배웠습니다.
        # cls(...) == User(...)


# 유저 생성 및 초기값 설정
younghoon = User.from_string("강영훈,younghoon@codeit.kr,123456")
yoonsoo = User.from_list(["이윤수", "yoonsoo@codeit.kr", "abcdef"])

print(younghoon.name, younghoon.email, younghoon.password)
print(yoonsoo.name, yoonsoo.email, yoonsoo.password)

# 잘 출력되네요, 이번 과제처럼 인스턴스를 생성하는 클래스 메소드를 클래스 속에 작성하는 것은 실제로 개발자들이
# 자주 사용하는 방식입니다. 깔끔한 코드로 인스턴스를 생성할 수 있는 방식이니까 기억해두세요.
