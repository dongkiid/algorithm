# n = int(input())
# cards = [ i for i in range(1,n+1)]
# if len(cards) > 1:
#     while len(cards) > 1:
#         cards.pop(0)
#         cards.append(cards.pop(0))   
#     print(''.join(str(cards[0])))

# 역시나 큐로 풀면 시간초과가 나서 데크로 변경해서 풀었다.

from collections import deque

n = int(input())
cards = deque(i for i in range(1,n+1))

if len(cards) > 1:
    while len(cards) > 1:
        cards.popleft()
        cards.rotate(-1)

print(cards[0])