import math
print('하고 싶은 계산은?',end='')
d=input()
if(d=='거속시'):
    print('거리, 속력, 시간 계산기입니다')
    print('거리(m) = ', end='')
    a=input()
    print('속도(m/s) = ', end='')
    b=input()
    print('시간(s) = ', end='')
    c=input()
    if(a==''):
        result=float(b)*float(c)
        print('거리 = '+ str(result)+'m')
    elif(b==''):
        result=float(a)/float(c)
        print('속도 = '+ str(result)+'m/s')
    elif(c==''):
        result=float(a)/float(b)
        print('시간 = '+ str(result)+'s')
if(d=='가속도'):
    print('가속도 계산기입니다')
    print('시간(s) = ',end='')
    a=input()
    print('처음 속도(m/s) = ',end='')
    b=input()
    print('나중 속도(m/s) = ',end='')
    c=input()
    result=(float(c)-float(b))/float(a)
    print('가속도 = '+str(result)+'m/s²')
