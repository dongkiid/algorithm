#BOJ, 11328

# 틀린 답
#3중 for문 ㄷ ㄷ ㄷ 
# 역시나 시간초과가 떴다. 왜 생각이 이렇게 밖에 안될까?

# num = int(input())
# for n in range(num):
#     result = [] #결과를 담을 배열
#     str1,str2 = map(str,input().split())
#     arr1 = list(str1)
#     arr2 = list(str2)
#     for i in arr1:
#         for j in arr2:
#             if i == j:
#                 result += i
#     if arr1 == result:
#         print("Possible")
#     else:
#         print("Impossible")

N = int(input())
 
for i in range(N):
    str1,str2 = input().split()
    # 문자열을 정렬한 뒤 같은 위치에 있는 문자들을 비교하여 가능 여부를 TF로 판단하면, O(logN) 이어서 삼중 for문 보다 효율적임
    # sorted()는 내용을 정렬 후 리스트 형태로 반환. 하여 ''.join으로 다시 문자열로 만들어주는 것임
    str1 = ''.join(sorted(str1)) 
    str2 = ''.join(sorted(str2))
    
    if len(str1) != len(str2):
        print("Impossible")
        continue

    for i in range(len(str1)):
        if str1[i] != str2[i]:
            flag = False
            break
        else:
            flag = True
    if flag:
        print("Possible")
    else:
        print("Impossible")
