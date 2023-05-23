-- MEMBER_PROFILE 테이블에서 
-- 생일이 3월인 여성 회원의 ID, 이름, 성별, 생년월일을 조회하는 SQL문을 작성해주세요. 
-- 이때 전화번호가 NULL인 경우는 출력대상에서 제외시켜 주시고,
-- 결과는 회원ID를 기준으로 오름차순 정렬해주세요

-- <실행 결과 예시>
--      MEMBER_ID	  MEMBER_NAME	GENDER	DATE_OF_BIRTH
-- seoyeons@naver.com    박서연	        W	   1993-03-16

SELECT MEMBER_ID, MEMBER_NAME, GENDER, DATE_FORMAT(DATE_OF_BIRTH,'%Y-%m-%d') as DATE_FORMAT
FROM MEMBER_PROFILE
WHERE MONTH(DATE_OF_BIRTH) = 3 
    AND GENDER ="W"
    AND TLNO IS NOT NULL  
ORDER BY MEMBER_ID

