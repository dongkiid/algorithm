from collections import deque

n,k = map(int,input().split())
circle = deque(range(1,n+1))
result = []

while circle:
    #k 앞에 있는 사람들을 뒤로 보냄
    circle.rotate(-(k-1))
    #k 삭제
    result.append(str(circle.popleft()))
print('<' + ', '.join(result) + '>')