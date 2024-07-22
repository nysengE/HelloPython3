#모듈

#모듈 불러오기 - import
import Joseph.Hello
Joseph.Hello.sayHello()
#-----------------------
from Joseph import Hello
Hello.sayHello()
from Joseph2 import Hello2
Hello2.sayHello()

#모듈 사용하기 1
import Joseph.calc
val = Joseph.calc.add(10, 5)
print(val)
#모듈 사용하기 2 - 함수 명
from Joseph.calc import add
from Joseph.calc import div
val = add(10, 5)
print(val)
val = div(10, 5)
print(val)
# *기호 사용하기
from Joseph.calc import *
val = mul(10, 5)
print(val)
val = minus(10, 5)
print(val)
#모듈 사용하기 3 - 별칭
import Joseph.calc as zc
val = zc.add(10, 5)
print(val)


#단위 환산 (convertUnit/readUnit/printUnits)
def convertUnit():
    readUnit = int(input('길이(mm)를 입력하세요. '))
    print(f'''
    {readUnit}mm --> {readUnit / 10} cm
    {readUnit}mm --> {readUnit / 1000} m
    {readUnit}mm --> {readUnit / 25.4:.5f} inch
    {readUnit}mm --> {readUnit / 304.8:.6f} ft
    ''')

#할인된 상품 가격표 출력 (discountPrice/readDiscount/printPrices)
def discountPrice():
    discountTable = {
        '쌀': 9900,

        '상추': 1900,
        '고추': 2900,
        '마늘': 8900,
        '통닭': 5600,
        '햄': 6900,
        '치즈': 3900
    }
    print(f'''    
    ---------------------------------------
    -- 한빛마트 오늘의 할인 가격표 출력 시스템 --
    ---------------------------------------
    ''', end='')
    readDiscount = int(input('오늘의 할인율을 입력하세요. '))
    for item, price in discountTable.items():
        printPrices = price - (price * (readDiscount / 100))
        print(f'{item}\t: {price} 원 {readDiscount} %DC -> {printPrices} 원')
    print('---------------------------------------')

#주민번호 유효성 체크 (checkJumin/readJumin/printJumin)
def checkJumin():
    readJumin = input("주민등록번호를 입력하세요 (예: 1234561234567): ")
    # 1. 주민등록번호 길이가 13자리인지 확인
    if len(readJumin) != 13 or not readJumin.isdigit():
        print("유효하지 않은 주민등록번호입니다. (길이 또는 숫자 형식 오류)")
        return
    # 2. 뒤 7자리 중 첫 번째 숫자가 1, 2, 3, 4 중 하나인지 확인
    gender = int(readJumin[6])
    if gender not in [1, 2, 3, 4]:
        print("유효하지 않은 주민등록번호입니다. (성별 코드 오류)")
        return
    # 3. 뒤 7자리 중 첫 번째 숫자를 제외한 나머지 6자리가 유효한 값인지 확인
    number = int(readJumin[7:])
    if not (0 <= number <= 899999):
        print("유효하지 않은 주민등록번호입니다. (순서 코드 오류)")
        return
    # 4. 주민등록번호 유효성 검사 공식에 따라 계산한 결과가 맞는지 확인
    checker = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]
    sum_value = sum(int(readJumin[i]) * checker[i] for i in range(12))
    remainder = sum_value % 11
    printJumin = (11 - remainder) % 10
    if printJumin == int(readJumin[-1]):
        print("유효한 주민등록번호입니다.")
    else:
        print("유효하지 않은 주민등록번호입니다.")