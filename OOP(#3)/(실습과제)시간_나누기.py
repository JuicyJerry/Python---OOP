# 자, 이제 가이드를 드리겠습니다. 시계는 결국 시간을 나타내는 기능이 핵심이고 시간은 시, 분, 초로 구성되어 있습니다.
# 시, 분, 초 이 3가지는 모두 하나의 클래스로 표현 가능합니다. 이 하나의 클래스는 다음과 같은 속성과 행동을 가져야 합니다.
#
# 속성
# 시, 분, 초는 각각 자기의 “값”을 속성으로 갖습니다. 예를 들면 4시 54분 12초에서는 4, 54, 12가 각각 시, 분, 초의 값이 되죠.
# 시, 분, 초 모두 “최댓값”이 있습니다. 분과 초는 각각 59, 그리고 시는 23이라는 최댓값을 가집니다.
#
# 행동
# 값 1 증가시키기:
# 시간이 흐르는 동작 즉 1초, 1분, 1시가 증가하는 동작을 할 수 있어야 합니다.
# 이렇게 시간이 흐를 때 시, 분, 초는 각자의 최댓값에 도달하면 그 값을 0으로 바꾸고 그 위의 단위를 1 증가시켜야 합니다. 예를 들어 59초에서 60초가 되면 초를 다시 0으로 바꿔주고 분을 1분 늘리는 것처럼요.
# 값 설정하기: 가끔씩 잘 되던 시계에 오차가 생기거나 시간대가 다른 나라로 여행을 가면 현재 시간을 변경해야 합니다. 이렇게 하려면 시, 분, 초를 바로 세팅할 수 있어야겠죠? 이 기능도 추가하겠습니다.
#
# 이처럼 같은 속성과 행동을 갖는 시, 분, 초를 하나의 클래스로 나타내봅시다. 시, 분, 초의 주된 동작은 "0 또는 시작값"에서 "최댓값"까지 숫자를 증가시키는 것이니까 클래스 이름을 Counter로 해서 작성해봅시다.

class Counter:
    """
    시계 클래스의 시,분,초를 각각 나타내는데 사용될 카운터 클래스
    """

    def __init__(self, limit):
        """
        인스턴스 변수 limit(최댓값), value(현재까지 카운트한 값)을 설정한다.
        인스턴스를 생성할 때 인스턴스 변수 limit만 파라미터로 받고, value는 초깃값 0으로 설정한다.
        """
        self.limit = limit
        self.value = 0


    def set(self, new_value):
        """
        파라미터가 0 이상, 최댓값 미만이면 value에 설정한다.
        아닐 경우 value에 0을 설정한다.
        """
        if new_value >= 0:
            if new_value < self.limit:
                self.value = new_value
                #new_value == self.value  # #37과 차이
        else:
            self.value = 0


    def tick(self):
        """
        value를 1 증가시킨다.
        카운터의 값 value가 limit에 도달하면 value를 0으로 바꾼 뒤 True를 리턴한다.
        value가 limit보다 작은 경우 False를 리턴한다.
        """
        self.value += 1

        if self.value == self.limit:
        #if self.value <= self.limit: #50과의 차이는?
            self.value = 0
            return True
        elif self.value < self.limit:
            return False

    def __str__(self):
        """
        value를 최소 두 자릿수 이상의 문자열로 리턴한다.
        일단 str 함수로 숫자형 변수인 value를 문자열로 변환하고 zfill 메소드를 호출한다.
        """
        return str(self.value).zfill(2)


# 최대 30까지 셀 수 있는 카운터 인스턴스 생성
counter = Counter(30)

# 0부터 5까지 센다
print("1부터 5까지 카운트하기")
for i in range(5):
    counter.tick()
    print(counter)

# 타이머 값을 0으로 바꾼다
print("카운터 값 0으로 설정하기")
counter.set(0)
print(counter)

# 카운터 값 27로 설정
print("카운터 값 27로 설정하기")
counter.set(27)
print(counter)

# 카운터 값이 30이 되면 0으로 바뀌는지 확인
print("카운터 값이 30이 되면 0으로 바뀝니다")
for i in range(5):
    counter.tick()
    print(counter)
