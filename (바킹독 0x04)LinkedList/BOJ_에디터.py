#BOJ, 1406

# 커서를 기준으로 양옆에 스택을 만듦
# L = left에서 pop해서 right에 append
# D = right에서 pop해서 left에 append
# B = left에서 pop만 해주기 
# P $ = [0]이 P면 [1]을 left에 append

# !!! 문제 !!!
# 처음에는 입력받아야 하는 값들을 input()으로 받아서 구현했는데,
# 그렇게 짠 코드를  python3으로 제출 했을 때는 시간초과 나왔고, pypy3으로 돌려야만 정답 처리가 되었다.

# ===> 해결 방법 : sys.stdin.readline().rstrip()
# input()으로 입력받던 것을 
# sys 모듈의 stdin객체로 입력값을 받는 코드로 수정해서
# 코드를 python3으로 돌려도 정답 처리가 되도록 했다.

# input()은 한 번에 한 줄씩 입력을 받지 않고, 사용자로부터 개행 문자가 입력될 때까지 대기하는 반면
# sys.stdin.readline()은 한 번에 한 줄씩 입력을 읽어들이기 때문에 대용량 입력에 성능적 이점을 갖고 있다.
# sys.stdin.readline() 뒤에 붙인 rstrip()은 개행 문자를 제거하는 기능이다.


import sys

left = list(sys.stdin.readline().rstrip())
num = int(sys.stdin.readline().rstrip())
right = []
for _ in range (num):
    type = sys.stdin.readline().rstrip().split()
    if type[0] == 'L' and left:
        right.append(left.pop())
    elif type[0] == 'D' and right:
        left.append(right.pop())
    elif type[0] == 'B' and left:
        left.pop()
    elif type[0] == 'P':
        left.append(type[1])
    else:
        continue
print(left,right)
right.reverse()
print(''.join(left+right))    
