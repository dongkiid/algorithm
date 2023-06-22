import sys
from collections import deque

def bfs (a,b,c):
    queue = deque()
    queue.append((a,b))
    #queue = deque((a,b)) 사용하면 cannot unpack non-iterable int object 에러 남
    visited[a][b] = True

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[nx][ny]:
                continue
            if c == graph[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx,ny))
    return

def weak_bfs (a,b,c):
    queue = deque()
    queue.append((a,b))
    visited[a][b] = True

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[nx][ny]:
                continue
            # 적록색약의 색 구분법 : RGB중 B가 아닌 것 / 그 외
            # 또 다른 구분법 : 그래프에 있는 R을 G로 바꿔주기 
            if c != 'B' and graph[nx][ny] != 'B' :
                visited[nx][ny] = True
                queue.append((nx,ny))
            elif c == 'B' and graph[nx][ny] == 'B':
                visited[nx][ny] = True
                queue.append((nx,ny))
    return

n = int(sys.stdin.readline())
graph = []
normal_cnt = 0
weak_cnt = 0

graph = [list(sys.stdin.readline().strip()) for _ in range(n)]

visited = [[False]*n for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in range(n):
    for j in range(n):
        color = graph[i][j]
        if not visited[i][j]:
            bfs(i,j,color)
            normal_cnt += 1

visited = [[False]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        color = graph[i][j]
        if not visited[i][j]:
            weak_bfs(i,j,color)
            weak_cnt += 1

print(normal_cnt)
print(weak_cnt)
