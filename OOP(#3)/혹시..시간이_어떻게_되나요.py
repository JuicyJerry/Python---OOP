# 기능
# 1. 현재 시간을 설정할 수 있다.
# 2. 현재 시간을 변경할 수 있다.
# 3. 현재 시간에 1초씩 더할 수 있다.

# 위 코드처럼 작동하는 Clock 클래스를 작성한다고 할 때, 어떤 속성과 기능(행동)을, 어떻게 넣어야 할까요?
# 다음 레슨의 설명을 듣기 전에 꼭 스스로 이 부분에 대해 고민해보세요!

# 1시 30분 48초인 시계 인스턴스 생성
clock = Clock(1, 30, 48)

# 13초를 늘린다
for i in range(13):
    clock.tick()

# 시계의 현재 시간 출력
print(clock)

# 2시 3분 58초로 시계 세팅
clock.set(2, 3, 58)

# 5초를 늘린다
for i in range(5):
    clock.tick()

# 시계의 현재 시간 출력
print(clock)

# 23시 59분 57초로 세팅
clock.set(23, 59, 57)

# 5초를 늘린다
for i in range(5):
    clock.tick()

# 시계의 현재 시간 출력
print(clock)
