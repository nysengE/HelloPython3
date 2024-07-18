#모듈
#특정 기능을 수행하는 코드들의 모음
#코드 재사용: 한번 작성한 코드를 여러 번 사용 가능
#코드 관리: 큰 프로젝트를 작은 모듈로 나눠 관리 가능
#협업: 여러 개발자가 각각 모듈을 개발하고 함꼐 사용
#표준 모듈: 파이썬에서 기본적으로 제공하는 모듈, 바로 사용 가능
#외부 모듈: 다른 조직 혹은 개발자가 만든 모듈, 별도 설치 필요
#사용자 정의 모듈: 직접 만든 모듈

#모듈 사용 방법
#import 모듈명
#import 모듈명 as 별칭
#from 모듈명 import 함수명 as 별칭

#난수 생성
import random
import random as rnd

#1~10 사이 임의의 난수 생성
print(random.randint(1, 10))

print(rnd.sample(range(1, 46), 6))

#홀수 / 짝수
num = input('정수를 입력 하세요 : ')

if num % 2 == 0:
    print('짝수 입니다.')
elif num % 2 == 1:
    print('홀수 입니다.')
else:
    print('정수가 아닙니다.')

#pass
#조건문이나 다른 문에서 실행문이 정해지지 않은 경우
#임시로 작성하는 명령문

if num % 2 == 0:
    pass
else:
    pass

#마일리지 사용하기
mileage = 1200

# if mileage >= 1000:
#     print('마일리지 사용 가능')
# else:
#     print('마일리지 사용 불가능')

# result = ''
# if mileage >= 1000:
#     result = '마일리지 사용 가능'
# else:
#     result = '마일리지 사용 불가능'

result = '마일리지 사용 불가능'

if mileage >= 1000:
    result = '마일리지 사용 가능'


# 속도 위반 경고 프로그램
# 입력: 현재 속도를 입력 받으면 제한 속도와 비교하여 경고 메시지를 출력함
# 제한 속도: 60km/h
# 예: 현재 속도: 75, 경고 메시지: 속도 위반! 속도를 줄이세요.

current_speed = int(input('현재 속도를 입력하세요 (km/h) : '))
speed_limit = 60

if current_speed > speed_limit:
    print('속도 위반! 속도를 줄이세요.')
else:
    print('정상 속도입니다.')

# 자동 온도 조절 장치
# 입력: 현재 온도를 입력 받으면 설정 온도와 비교하여 조치 메시지를 출력함
# 설정 온도: 22도
# 예: 현재 온도: 18, 메시지: 난방을 켭니다.

current_temp = int(input('현재 온도를 입력하세요 (도) : '))
set_temp = 22

if current_temp < set_temp:
    print('난방을 켭니다.')
elif current_temp > set_temp:
    print('냉방을 켭니다.')
else:
    print('적정 온도입니다.')

# 자동 주문 시스템
# 입력: 주문할 음료를 입력 받으면 재고를 확인하여 주문 가능 여부를 출력함
# 재고: 커피: 10, 차: 5, 주스: 3
# 예: 주문할 음료: 커피, 메시지: 주문이 완료되었습니다.

inventory = {
    '커피': 10,
    '차': 5,
    '주스': 3
}

order = input('주문할 음료를 입력하세요 (커피, 차, 주스) : ')

if order in inventory and inventory[order] > 0:
    inventory[order] -= 1
    print(f'''
    주문이 완료되었습니다. 
    주문한 음료: {order}, 남은 재고: {inventory[order]}
    ''')
else:
    print('재고가 부족합니다.')

# 국가 재난 지원금 출력
# 입력: 가족 수를 입력 받으면 지원금을 계산하여 출력함
# 1인당 지원금: 50000원
# 예: 가족 수: 4, 총 지원금: 200000원

family_count = int(input('가족 수를 입력하세요 : '))
support_per_person = 50000

total_support = family_count * support_per_person
print(f'총 지원금은 {total_support}원 입니다.')

# 개선 BMI 지수
# 입력: 체중과 키를 입력 받으면 BMI를 계산하고 상태를 출력함
# BMI = 체중(kg) / (키(m) * 키(m))
# 예: 체중: 70kg, 키: 1.75m, BMI: 22.9, 상태: 정상

weight = float(input('체중을 입력하세요 (kg) : '))
height = float(input('키를 입력하세요 (cm) : '))

bmi = weight / ((height / 100) ** 2)

status = ""
if bmi >= 30:
    status = "비만"
elif bmi >= 25:
    status = "과체중"
elif bmi >= 18.5:
    status = "정상"
else:
    status = "저체중"

print(f'BMI 지수는 {bmi:.1f}입니다. 상태는 {status}입니다.')

# 버스 전용차로 단속
# 입력: 현재 시간을 입력 받으면 버스 전용차로 단속 시간인지 출력함
# 단속 시간: 7:00 ~ 9:00, 17:00 ~ 19:00
# 예: 현재 시간: 8:30, 메시지: 버스 전용차로 단속 시간입니다.

current_time = float(input('현재 시간을 입력하세요 (24시간 형식, 예: 8.5) : '))

if (7 <= current_time < 9) or (17 <= current_time < 19):
    print('버스 전용차로 단속 시간입니다.')
else:
    print('단속 시간이 아닙니다.')

# 마스크 구매 가능 요일 출력
# 입력: 주민등록번호 뒷자리 첫 숫자를 입력 받으면 마스크 구매 가능 요일을 출력함
# 1, 6: 월요일, 2, 7: 화요일, 3, 8: 수요일, 4, 9: 목요일, 5, 0: 금요일
# 예: 주민등록번호 뒷자리 첫 숫자: 3, 메시지: 마스크 구매 가능 요일은 수요일입니다.







# 차량 2부제
# 입력: 차량 번호 마지막 숫자를 입력 받으면 운행 가능 여부를 출력함
# 홀수: 월, 수, 금 운행 가능, 짝수: 화, 목 운행 가능
# 예: 차량 번호 마지막 숫자: 3, 메시지: 운행 가능 요일은 월, 수, 금입니다.

car_last_digit = int(input('차량 번호 마지막 숫자를 입력하세요 : '))

match car_last_digit % 2:
    case 0:
        print('운행 가능 요일은 화, 목, 토 입니다.')
    case 1:
        print('운행 가능 요일은 월, 수, 금 입니다.')

# 생존율 출력
# 입력: 생존자 수와 총 인원 수를 입력 받으면 생존율을 계산하여 출력함
# 예: 생존자 수: 70, 총 인원 수: 100, 메시지: 생존율은 70.0%입니다.

try:
    survivors = int(input('생존자 수를 입력하세요 : '))
    total_people = int(input('총 인원 수를 입력하세요 : '))

    if total_people == 0:
        raise ValueError('총 인원 수는 0일 수 없습니다.')

    survival_rate = (survivors / total_people) * 100

    match survival_rate:
        case rate if rate >= 100:
            print('생존율은 100%입니다. 모두 생존했습니다.')
        case rate if rate > 0:
            print(f'생존율은 {survival_rate:.1f}%입니다.')
        case 0:
            print('생존율은 0%입니다. 생존자가 없습니다.')
except ValueError as e:
    print(f'입력 오류: {e}')

## 전기요금 계산서
# 입력: 사용량을 입력 받으면 요금을 계산하여 출력함
# 기본요금: 1000원, 1kWh당 200원
# 예: 사용량: 350kWh, 메시지: 총 전기요금은 80000원입니다.

try:
    usage = int(input('전기 사용량을 입력하세요 (kWh) : '))

    if usage < 0:
        raise ValueError('사용량은 0 이상이어야 합니다.')

    basic_fee = 1000
    usage_fee = 200
    total_cost = basic_fee + (usage * usage_fee)

    match usage:
        case 0:
            print('사용량이 0입니다. 기본요금은 1000원입니다.')
        case _:
            print(f'총 전기요금은 {total_cost}원입니다.')
except ValueError as e:
    print(f'입력 오류: {e}')
