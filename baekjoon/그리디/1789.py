'''
[수들의 합]

참고) 
질문 게시판 :
서로 다른 19개의 자연수의 합으로 200을 표현하는 것은 가능하지만, (1+2+3+4+5+6+7+8+9+10+11+12+13+14+15+16+17+18+29 = 200)
서로 다른 20개의 자연수의 합으로 200을 표현하는 것은 불가능하므로 예제 입력에 대한 답은 19입니다.
'''

s = int(input())

for n in range(1, s+1):
    if n*(n+1) > 2*s:
        print(n-1)
        break
    if n*(n+1) == 2*s:
        print(n)
        break
        

