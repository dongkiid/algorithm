from collections import deque

def bfs(a,b):

    queue = deque()
    queue.append((a,b))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if graph[nx][ny] == 1:
                queue.append((nx,ny)) 
                graph[nx][ny] = 0      
    return

tc = int(input())
dx = [0,0,-1,1]
dy = [-1,1,0,0]

for _ in range(tc): #테케 갯수만큼
    result = 0
    n,m,k = map(int,input().split())
    graph = [[0]*m for _ in range(n)]
    for _ in range(k): #배추 갯수만큼
        x,y = map(int,input().split())
        graph[x][y] = 1
    #만들어진 그래프 내부에서 BFS 수행
    for i in range(n):
            for j in range(m):
                if graph[i][j] == 1:
                    graph[i][j] = 0
                    result += 1
                    bfs(i,j)
                    
    print(result)
    
