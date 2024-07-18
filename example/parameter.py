#
def print_args(*args):
    print(args)
print_args(1,2,3)
print_args('a','b','c','d','e')
#
def print_kwargs(**kwargs):
    print(kwargs)
print_kwargs(a=1,b=2,c=3)
print_kwargs(name='일지매', kor=99, eng=89, mat=94)

#언패킹
#리스트/문자열 언패킹
a, b, c = [1, 2, 3]
print(a, b, c)
x, y, z = 'xyz'
print(x, y, z)
#dict 언패킹
member = {'userid': 'abc123', 'passwd': ' 987xyz'}
uid, pwd = member.values()
print(uid, pwd)
uid, pwd = member.keys()
print(uid, pwd)
uid, pwd = member.items()
print(uid, pwd)
#가변 인수 언패킹
mylist = [1, 2, 3]
mydict = {'a': 4, 'b': 5, 'c':6}
print_args(*mylist)
print_kwargs(**mydict)
def print_args2(a, b, c):
    print(a, b, c)
print_args2(*mylist)
print_kwargs(**mydict)
#매개변수 기본값
def sayHello(name='unknown', say='Hello'):
    print(f'{name}, {say}')
sayHello('홍길동', '안녕')
sayHello('일지매', '하이')
sayHello('박세리')
sayHello()

#제곱값을 계산하는 함수
def squr(x):
    print(f'{x} => {x**2}')
squr(2)
squr(10)
#제곱값을 계산하는 함수2
def squr2(x):
    print(f'2 => {squr2(2)}')
    print(f'10 => {squr2(10)}')
#제곱값을 계산하는 함수3 - 인수가 음수인 경우 함수 실행 중지
def squr3(x):
    if x < 0: return
    return x**2
squr3(50)
squr3(-1)