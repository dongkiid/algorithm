from collections import deque

def bfs(n,k):

    queue = deque()
    queue.appendleft(n)
    visited[n] = 1

    while queue:
        start = queue.popleft()
        
        if start == k:
            return visited[k]-1 # 시작 지점을 카운트에서 빼주기 위해 -1
        
        for i in(start*2, start-1, start+1):
            if 0 <= i <= 100000 and visited[i] == 0:
                if i == start*2:
                    visited[i] = visited[start] # 순간 이동 0초 소요되므로 +1 안해줘도 됨
                    queue.appendleft(i) # 순간 이동의 가중치가 가장 적기에 먼저 처리해주기 위해 appendleft
                else:
                    visited[i] = visited[start] + 1
                    queue.append(i)
                
    
n,k = map(int,input().split())
visited = [0]*100001

print(bfs(n,k)) 