from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        for i in range(4):  # 현재 위치로부터 상,하,좌,우 확인
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1: # 해당 노드를 처음 방문하는 경우에만 기록
                graph[nx][ny] = graph[x][y] + 1 # 이전 노드의 값에 +1 한 값을 저장
                queue.append((nx, ny))
    # 가장 오른쪽 아래 값 (=최단 거리)를 반환
    return graph[n - 1][m - 1]

n, m = map(int, input().split())
graph = [list(map(int,input())) for _ in range(n)]

# 이동 방향 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0, 0))