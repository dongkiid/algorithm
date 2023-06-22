
import sys
from collections import deque
n = int(input())
result= deque()
for _ in range(n):
    data = sys.stdin.readline().split()
    #1. push와 push 아닌 경우 구분
    if len(data) == 1:
        #2.큐에 데이터가 있을 때와 비어있는 경우 구분
        if len(result) >= 1:
            
            if data[0] == 'pop_front':
                print(result.popleft())
            elif data[0] == 'pop_back':
                print(result.pop())
            elif data[0] == 'front':
                print(result[0])
            elif data[0] == 'back':
                print(result[-1])
            elif data[0] == 'size':
                print(len(result))
            elif data [0] == 'empty':
                print(0)
            elif data[0] == 'size':
                    print(len(result))
            elif data[0] == 'print':
                 print(result)
        else:
            if data[0] == 'size':
                print(0)
            elif data[0] == 'empty':
                print(1)
            else:
                print(-1)         
    else:
         if data[0] == 'push_front':
                result.appendleft(int(data[1]))
         else:
                result.append(int(data[1]))

