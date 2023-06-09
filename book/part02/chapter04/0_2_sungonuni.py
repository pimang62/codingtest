"""
입력으로 정수 N을 받는다. 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 경우의 수를 구하는 프로그램을 작성하시오.

예를 들어 N이 1이라면,
00시 00분 00초 ~ 01시 59분 59초까지의 범위 중에서 다음의 시각은 카운트 되어야 한다.
00시 13분 30초, 00시 31분 31초 ...

예시:
N = 5

출력:
11475
"""

# 입력 받기

n = int(input())


# 3중 For 문

result = 0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                result += 1

print(result)