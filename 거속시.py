import math
print('거리, 속력, 시간 계산기 입니다')
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
