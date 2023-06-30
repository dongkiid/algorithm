from collections import deque

def bfs(n,k):

    queue = deque()
    queue.appendleft(n)
    visited[n] = 0

    while queue:
        start = queue.popleft()
        
        if start == k:
            return visited[k] 
        
        for i in(start*2, start-1, start+1):
            if 0 <= i <= 100000 and visited[i] == -1:
                if i == start*2:
                    visited[i] = visited[start] #순간 이동 0초 소요되므로 +1 안해줘도 됨
                    queue.appendleft(i) # 순간 이동의 가중치가 가장 적기에 최대한 먼저 처리해주기 위해 appendleft
                else:
                    visited[i] = visited[start] + 1
                    queue.append(i)
                

n,k = map(int,input().split())
# 카운트가 필요할 때 방문배열을 0으로 초기화해준다면 나중에 값을 반환할 때 -1해주어야 함
#
visited = [-1]*100001

print(bfs(n,k)) 
