#BOJ, 3273

# < 틀린 코드 >
# length = int(input())
# lists = list(map(int,input().split()))
# num = int(input())
# cnt = 0 
# for i in range (len(lists)):
#     #print("i:",i)
#     for j in range (len(lists)):
#         if i == j:
#             continue
#         #print("j",j)

#         sum = lists[i]+lists[j]
#         if sum == num:
#             cnt += 1
    
# print(int(cnt/2))
# 입력수가 100000이라면 완전탐색(이중 반복문)으로 구현시 당연히 시간초과가 난다. (On^2 이라서..)
# 또한 중복을 간과해서 프린트할 때 2를 나눠주어야 하는 나쁜 코드였다.

#< 정답 코드 >
#lists를 sort 해서 투포인터로 푸는 방법으로 해결

length = int(input())
lists = list(map(int,input().split()))
lists.sort()
num = int(input())
left = 0
right = length -1
cnt = 0

while left < right:
        sum = lists[left]+lists[right]
        if num == sum:
            cnt += 1
            left += 1
        if sum > num:
            right -= 1
        if sum < num:
            left += 1

print(cnt)
    
