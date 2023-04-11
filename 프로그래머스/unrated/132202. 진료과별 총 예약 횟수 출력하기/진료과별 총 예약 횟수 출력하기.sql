-- 코드를 입력하세요
SELECT MCDP_CD as 진료과코드, count(APNT_NO) as 5월예약건수
FROM APPOINTMENT
WHERE APNT_YMD LIKE '2022-05%'
GROUP BY MCDP_CD -- '진료과코드 별' 조회이므로
ORDER BY 2 ASC , 1 ASC