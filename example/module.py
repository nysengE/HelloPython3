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