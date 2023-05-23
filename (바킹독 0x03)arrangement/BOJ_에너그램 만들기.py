#BOJ, 1919
#collections 모듈을 사용해 해결한 문제

from collections import Counter

str1 = input()
str2 = input()

#collections 모듈의 Counter = 각 데이터의 빈도수를 계산
freq1 = Counter(str1)
freq2 = Counter(str2)

#print(freq1,freq2)

#두 문자열 요소들의 빈도수 차이를 구할 수 있음
diff = (freq1-freq2) + (freq2-freq1)
#Counter 함수는 데이터를 딕셔너리 형태로 저장하므로, value들의 합을 result에 추가  
result = sum(diff.values())
print(result)
