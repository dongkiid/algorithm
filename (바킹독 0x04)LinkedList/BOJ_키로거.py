#조건에 and를 사용했더니 출력값에 오류가 남.
#그냥 조건 안에 조건으로 해결

# import sys
# n = int(sys.stdin.readline())

# for _ in range(n):
#     password_input = input()
#     left = []
#     right = []
#     #print(left,right)
#     for i in password_input:
#         #print(i)
#         if i == '<' and left:
#             right.append(left.pop())
#         elif i == '>' and right:
#             left.append(right.pop())
#         elif i == '-' and left:
#             left.pop()
#         else:
#             left.append(i)
#         print(left,right)
#     right.reverse()
#     print(''.join(left+right))

import sys
n = int(sys.stdin.readline())

for _ in range(n):
    password_input = input()
    left = []
    right = []
    #print(left,right)
    for i in password_input:
        #print(i)
        if i == '<':
            if left:
                right.append(left.pop())
        elif i == '>':
            if right:
                left.append(right.pop())
        elif i == '-':
            if left:
                left.pop()
        else:
            left.append(i)
        #print(left,right)
    right.reverse()
    print(''.join(left+right))