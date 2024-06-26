SELECT A.FLAVOR
FROM FIRST_HALF AS A
#7월 아이스크림 총주문량을 구하기
JOIN (SELECT FLAVOR, SUM(TOTAL_ORDER) AS JULY_TOTAL_ORDER
     FROM JULY
     GROUP BY FLAVOR) B
     ON A.FLAVOR = B.FLAVOR
ORDER BY TOTAL_ORDER + JULY_TOTAL_ORDER DESC
LIMIT 3;