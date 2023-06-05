# 10845 큐 문제와 다른 점 : 주어지는 테스트 케이스의 크기 

# 10845 문제는 주어지는 명령의 수가 100만개 였던 반면, 
# 18258 문제는 주어지는 명령의 수가 200만개다.
# => 조건이 같다고 같은 식을 복붙해서 썼는데 큐2 문제에서 시간 초과가 발생했다.
# 데크를 적용해 pop(0)하던 부분을 pop.left로 바꾸어 해결했다.

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
            if data[0] == 'pop':
                print(result.popleft())
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
        else:
            if data[0] == 'size':
                print(0)
            elif data[0] == 'empty':
                print(1)
            else:
                print(-1)         
    else:
         result.append(int(data[1]))

