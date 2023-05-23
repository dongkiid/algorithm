#BOJ, 10808
arr = input()
cnt = [0] * 26 # 알파벳 개수만큼 배열 초기화
for i in arr:
    cnt[ord(i)-97] += 1 #요소를 아스키 코드로 변환하고, A의 아스키 코드인 97을 마이너스해 cnt의 인덱스와 일치시킴

print(*cnt) # *cnt? => 파이썬의 Unpacking 기능 : cnt리스트의 각 요소를 공백으로 구분해 개별적으로 출력