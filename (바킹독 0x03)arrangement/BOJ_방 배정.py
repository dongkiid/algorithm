#배열 초기화 해놓고 입력값따라 결괏값 만들기
# 성별 당 인원, 학년으로 나뉜 배열 만들기! 

# entire_student, entire_room = list(map(int,input().split()))
# result = [(0,0)]* 6 #여자, 남자 순서로 갯수
# for i in range(entire_student):
#     sex,grade = list(map(int,input().split()))
#     print(result[0])
#     if sex == 0: #여자면
#         result[grade][0] += 1
#     else:
#         result[grade][1] += 1 
#         print(result)       

# 파이썬에서 퓨틀은 immutable한 자료형으로, 
# # 한번 할당된 요소를 수정할 수 없다

# entire_student, max_human = list(map(int,input().split()))
# woman = [0]*6
# man = [0]*6
# woman_cnt = 0
# man_cnt = 0

# for i in range(entire_student):
#     sex,grade = list(map(int,input().split()))
#     if sex == 0: #여자면
#         woman[grade-1] +=1
#     else:
#         man[grade-1] += 1
        
# print(woman,man)
# for i in range(len(woman)):
#     if woman[i] <= max_human:
#         if woman[i] == 0:
#             continue
#         woman_cnt += 1
#         print("woman<=max_human",woman_cnt)
   
#     if woman[i] > max_human:
#         woman_cnt += int(woman[i]%max_human) +1
#         #print("woman>max_human",woman_cnt)

# for i in range(len(man)):
     
#      if man[i] <= max_human:
#         if man[i] == 0:
#             continue
#         man_cnt += 1
#         #print("man<=max_human",man_cnt)
    
#      if man[i] > max_human:
#         man_cnt += int(man[i]%max_human) + 1
#         #print("man>max_human",man_cnt)

# print(int(man_cnt+woman_cnt))

import math
n, room_max = map(int,input().split())
student = [[0,0] for _ in range(6)] 

for _ in range(n):
    sex,grade = map(int,input().split())
    student[grade-1][sex] += 1 #student의 [grade] 위치에 여성이면 [grade][0](튜플 안에 첫번째요소) / 남성이면 [grade][1] (튜플 안에 두번째 요소)  
#print(student)
cnt = 0
for level in student:
    for maleFemale in level:
        cnt += math.ceil(maleFemale / room_max)
print(cnt)