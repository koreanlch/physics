import re

compiled = re.compile(r'([0-9]*)(N|kg|m|s|m\/s)')

def prt_result(b, c):
    관계식을 여기에 입력하면 코드는 완성

def split_exec(obj):
    a = compiled.search(obj)
    if a != None:
        b = a.group(1)
        c = a.group(2) 
        prt_result(b,c)
    else:
        print('올바른 값이 아닙니다. 올바른 값을 입력하세요.')

print('주어진 값 : ',end="")
received = input().split()

for obj in received:
    split_exec(obj)