'''
[치즈]
공기와 접촉된 칸은 한 시간이 지나면 녹아 없어짐!

- 치즈가 모두 녹아 없어지는 데까지 걸리는 시간?
- 모두 녹기 한 시간 전에 남아 있는 치즈 조각의 칸 개수?

Q : 덩어리 속 공기 구멍을 제외한 가장자리를 어떻게 판별..?
A : BFS 탐색으로 visited 기록하면 자연스럽게 (구멍 제외) 테두리만 찾아짐

Q : 한 덩어리의 테두리를 전부 찾아내고 싶다면?
A : 현재 0인 자리에서 주변부가 1일때를 기록하면 됨

13 12
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1 1 0 0 0
0 1 1 1 0 0 0 1 1 0 0 0
0 1 1 1 1 1 1 0 0 0 0 0
0 1 1 1 1 1 0 1 1 0 0 0
0 1 1 1 1 0 0 1 1 0 0 0
0 0 1 1 0 0 0 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
'''
from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 1, 0, -1]  # 동남서북
dy = [1, 0, -1, 0] 

def in_range(a, b):
    if 0 <= a < n and 0 <= b < m:
        return True
    return False

def bfs():
    q =  deque([(0, 0)])
    visited = [[0]*m for _ in range(n)]
    visited[0][0] = 1
    
    cnt = 0  # 녹지 않은 치즈 부분
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if not in_range(nx, ny) or visited[nx][ny]:
                continue
            # 이 부분이 치즈를 녹이는 핵심 파트
            if graph[nx][ny] != 1:  # 0 또는 2 : 공기
                visited[nx][ny] = 1
                q.append((nx, ny))
            else : # if graph[nx][ny] == 1:
                graph[nx][ny] = 2  # 녹은 부분
                visited[nx][ny] = 1
                cnt += 1
    return cnt

time = 0  # 전부 없어질 때까지 걸린 시간
answer = 0  # 바로 직전 치즈 블록 수
while True:
    melt = bfs()  # cnt
    if melt == 0:
        break
    answer = melt
    time += 1
        
print(time, answer, end='\n')

"""
# if graph[x][y] == 0 and graph[nx][ny] == 1:
#     graph[nx][ny] = 2  # 녹은 부분
#     visited[nx][ny] = 1
# if graph[nx][ny] != 1:
#     visited[nx][ny] = 1
#     q.append((nx, ny))
>>>
[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0], 
 [0, 2, 2, 2, 0, 0, 0, 2, 2, 0, 0, 0], 
 [0, 2, 1, 1, 2, 2, 2, 0, 0, 0, 0, 0], 
 [0, 2, 1, 1, 1, 2, 0, 2, 2, 0, 0, 0], 
 [0, 2, 1, 1, 2, 0, 0, 2, 2, 0, 0, 0], 
 [0, 0, 2, 2, 0, 0, 0, 2, 2, 0, 0, 0], 
 [0, 0, 2, 1, 2, 2, 2, 1, 2, 0, 0, 0], 
 [0, 0, 2, 1, 1, 1, 1, 1, 2, 0, 0, 0], 
 [0, 0, 2, 1, 1, 1, 1, 1, 2, 0, 0, 0], 
 [0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0], 
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

# if graph[nx][ny] != 1:
#     visited[nx][ny] = 1
#     q.append((nx, ny))
# if graph[x][y] == 0 and graph[nx][ny] == 1:
#     graph[nx][ny] = 2  # 녹은 부분
#     visited[nx][ny] = 1
>>>
[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0], 
 [0, 2, 2, 2, 0, 0, 0, 2, 2, 0, 0, 0], 
 [0, 2, 1, 1, 2, 2, 2, 0, 0, 0, 0, 0], 
 [0, 2, 1, 1, 1, 1, 0, 2, 2, 0, 0, 0], 
 [0, 2, 1, 1, 1, 0, 0, 1, 2, 0, 0, 0], 
 [0, 0, 2, 1, 0, 0, 0, 1, 2, 0, 0, 0], 
 [0, 0, 2, 1, 1, 1, 1, 1, 2, 0, 0, 0], 
 [0, 0, 2, 1, 1, 1, 1, 1, 2, 0, 0, 0], 
 [0, 0, 2, 1, 1, 1, 1, 1, 2, 0, 0, 0], 
 [0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0], 
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
"""