import sys
from collections import deque

def bfs (x,y):
    cnt = 0
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                queue.append((nx,ny)) # 이 시점에서 이어지는 게 있는 지 확인하기 위해
                graph[nx][ny] = 0 #첫 방문시에만 방문처리
                cnt += 1          
    return cnt


n, m = map(int,input().split())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
paint = [] #이어지는 노드의 갯수(cnt값)를 append, 그리고 그 이어진 갯수를 값으로
dx = [1,-1,0,0]
dy = [0,0,1,-1]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            paint.append(bfs(i,j))

if paint:
    if max(paint) == 0: #연결된 노드가 없는 지점이 0으로 출력하는 것에 대한 예외처리를 해줌
        print(len(paint))
        print(1)
    else:
        print(len(paint))
        print(max(paint))
else:
    print(0)
    print(0)
