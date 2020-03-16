# 절차 지향 프로그래밍이 등장하기 이전에 절차 지향 프로그래밍이 있었다.
# 절차 지향 프로그래밍은 객체라는 개념이 없다.
# 대신 함수라는 개념은 있다.
# 함수는 순서대로 특정 명령어들을 실행하는 부분을 하나로 묶은 것이다.

# 절차 지향 프로그래밍
# 반복적으로 사용하는 코드를 함수로 정의한다
def print_person_info(person_name, person_age, person_gender):
    # 사람의 이름, 나이, 성별을 파라미터로 받으면 받은 정보를 이해할 수 있는 문자열로 출력해주는 함수
    print("사람 한 명을 소개합니다")
    print("{}님은 {}살이고 {}입니다".format(person_name, person_age, person_gender))

def is_underage(person_age):
    # 사람의 나이를 파라미터로 받아서 미성년자인지를 리턴해주는 함수
    return person_age < 20

# 영훈이의 정보
young_name = "영훈"
young_age = 10
young_gender = "남자"

# 윤수의 정보
yoonsoo_name = "윤수"
yoonsoo_age = 20
yoonsoo_gender = "남자"

# 영훈/윤수 정보 출력
print_person_info(young_name, young_age, young_gender)
print_person_info(yoonsoo_name, yoonsoo_age, yoonsoo_gender)

# 영훈/윤수가 미성년자인지 출력
print(is_underage(young_age))
print(is_underage(yoonsoo_age))

# print_person_info 함수와 is_underage 함수가 있네요. 이렇게 프로그램에 필요한 동작을 함수라는 단위로 묶어서
# 사용하는 것이 절차 지향 프로그래밍입니다. 같은 프로그램을 객체 지향 프로그래밍으로 작성하면 다음과 같습니다.


# 객체 지향 프로그래밍
# 속성과 행동을 갖는 객체들이 행동을 하는 방식으로 작성한다
class Person:
    # 사람을 나타내는 클래스
    def __init__(self, name, age, gender):
        # 사람은 이름, 나이, 성별을 속성으로 갖는다
        self.name = name
        self.age = age
        self.gender = gender

    def print_info(self):
        # 자신의 정보를 출력하는 메소드
        print("사람 한 명을 소개합니다")
        print("{}님은 {}살이고 {}입니다".format(self.name, self.age, self.gender))

    def is_underage(self):
        # 사람의 나이를 파라미터로 받아서 미성년자인지를 리턴해주는 메소드
        return self.age < 20

# 영훈/윤수을 나타내는 객체 생성
young = Person("영훈", 10, "남자")
yoonsoo = Person("윤수", 20, "남자")

# 영훈/윤수 정보 출력
young.print_info()
yoonsoo.print_info()

# 영훈/윤수가 미성년자인지 출력
print(young.is_underage())
print(yoonsoo.is_underage())

# 객체 지향 프로그래밍은 필요한 동작 뿐만 아니라 아예 연관된 데이터도 객체로 묶어서 하나의 클래스로 나타냅니다. 즉,
# 절차 지향 프로그래밍에서는 프로그램 안에서 서로 관련된 동작들만을 묶어서 관리하는데
# 객체 지향 프로그래밍에서는 관련된 동작들을 관련된 데이터와도 함께 묶어서 관리하는 거죠.

# 절차 지향 프로그래밍이 객체 지향 프로그래밍과 다른 점은 크게 2가지입니다.
#
#
# 절차 지향 프로그램은 프로그램에 필요한 데이터를 관련있는 함수와 묶어서 관리하기 힘듭니다.
# 그렇다면 객체 지향 프로그래밍은? 서로 관련있는 데이터와 함수를 객체로 묶어서 사용할 수 있습니다. 클래스라는 것이 있으니까요!
# 절차 지향 프로그래밍은 프로그램을 단지 명령어들을 순서대로 실행하는 것으로 봅니다. 그렇다면 객체 지향 프로그래밍은?
# 프로그램을 객체 간의 소통으로 봅니다. 즉, 객체가 프로그램의 기본 단위가 되고 이 객체 속을 들여다보면
# 서로 관련된 데이터(객체의 속성)와 동작(객체의 행동)이 모여있습니다. 그리고 프로그램을 이 객체들이 순서대로 소통하는 과정으로 간주합니다.


# 절차 지향 프로그래밍
# 프로그램을 만들 때 데이터와 함수를 합칠 수 없다. / 프로그램을 명령어들을 순서대로 실행하는 것으로 본다.

# 객체 지향 프로그래밍
# 프로그램을 만들 때 데이터와 함수를 합칠 수 있다. / 프로그램을 객체들이 순서대로 소통하는 과정으로 본다.

# 두 방식 중 어느 한 가지가 더 좋다고 할 수는 없습니다. 프로그램의 용도에 따라 적합한 방식이 다르기 때문입니다.
# 만약 데이터와 동작의 연관성이 높고 이걸 객체라는 단위로 묶는 것이 낫겠다는 생각이 들면 객체 지향 프로그래밍을
# 하는 것이 좋습니다. 보통 복잡한 프로그램일수록 객체 지향 프로그래밍으로 하는 것이 더 나은 경우가 많습니다.


