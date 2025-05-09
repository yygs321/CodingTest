-- 코드를 입력하세요
SELECT P1.ID, P1.NAME, P1.HOST_ID
FROM PLACES P1
JOIN (SELECT *
    FROM PLACES
    GROUP BY 3
    HAVING COUNT(*)>1) AS P2
ON P1.HOST_ID = P2.HOST_ID
ORDER BY 1 ASC