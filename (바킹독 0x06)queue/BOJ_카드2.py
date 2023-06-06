# n = int(input())
# cards = [ i for i in range(1,n+1)]
# if len(cards) > 1:
#     while len(cards) > 1:
#         cards.pop(0)
#         cards.append(cards.pop(0))   
#     print(''.join(str(cards[0])))

# 역시나 큐로 풀면 시간초과가 나서 데크로 변경해서 풀었다.

# from collections import deque

# n = int(input())
# cards = deque(i for i in range(1,n+1))

# if len(cards) > 1:
#     while len(cards) > 1:
#         cards.popleft()
#         cards.rotate(-1)

# print(cards[0])

# 위 코드는 조건 안에 while문이 들어있고, 204ms 만에 수행이 완료되는데
# 아래와 같이 while문 안에 조건을 넣는 방식으로 수정하면 176ms로 16% 정도 시간 절약이 된다.

from collections import deque

n = int(input())
cards = deque(i for i in range(1,n+1))

while True:
    if len(cards) == 1:
        break;
    
    cards.popleft()
    cards.rotate(-1)

print(cards[0])