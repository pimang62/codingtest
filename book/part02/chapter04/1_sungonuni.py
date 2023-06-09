"""
8x8 크기의 게임판에서 체스를 진행하려고 한다. 
게임판에서 행 위치를 표현할 때는 1~8로 표현하며, 열 위치를 표현할 때는 a~h로 표현한다.
게임판 내 임의의 한 칸에 나이트가 서있다. 나이트는 다음 2개의 법칙에 따라 움직일 수 밖에 없다.
1. 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기
2. 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하기

이처럼 나이트의 최초 좌표가 주어졌을 때, 나이트가 이동할 수 있는 경우의 수를 출력하는 프로그램을 작성하시오

입력 예시:
a1 

절차:
a1에서 상기 두 가지 법칙으로 움직일 수 있는 경우의 수는
1. 우측으로 한 칸 이동 후 아래측으로 두 칸 이동하기
2. 아래측으로 두 칸 이동 후 우측으로 한 칸 이동하기
이 두 개 밖에 없다.

출력:
2
"""


# 입력받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0]) - int(ord('a'))) + 1


# 움직임 정의

moving_type = [(-1, -2), (-1, 2), (1, -2), (1, 2), (-2, -1), (-2, 1), (2, -1), (2, 1)]

result = 0
# 모든 움직임들을 하나씩 나열해보며
for move in moving_type:

    # 움직인 후 좌표 도출
    nx = row + move[0]
    ny = column + move[1]

    # 만약 움직인 후 좌표가 범위 내에 존재한다면 
    if nx >= 1 and ny >= 1 and nx <= 8 and ny <= 8:
        # 경우의 수 카운트
        result += 1


print(result)
