SELECT * FROM BOOK;
SELECT BOOKID, BOOKNAME FROM BOOK;
SELECT PUBLISHER, PRICE FROM BOOK
WHERE BOOKNAME LIKE '축구의%';

SELECT * FROM CUSTOMER
WHERE NAME='김연아';

USE SAKILA;

SELECT CUSTOMER_ID, FIRST_NAME
FROM CUSTOMER
WHERE LAST_NAME = 'SMITH';

SELECT * FROM LANGUAGE;

SELECT LANGUGUAGE_ID, LAST_UPDATE, NAME
FROM LANGUAGE;

SELECT NAME FROM LANGUAGE;

CREATE OR REPLACE VIEW VLANGUAGE AS -- OR REPLACE 덮어쓰기문
SELECT UPPER(NAME) UPPER_NAME, 
LANGUAGE_ID*3.14 LANG_PI_VALUE
FROM LANGUAGE;

SELECT *FROM VLANGUAGE;

SELECT TITLE FROM FILM
WHERE RATING = 'G' AND RENTAL_DURATION >=7;

SELECT TITLE FROM FILM
WHERE RATING = 'G' OR RENTAL_DURATION >=7;

-- G등급이고 7일이상 이거나 PG13이고 3일이하인 영화
SELECT TITLE, RATING, RENTAL_DURAYION 
FROM FILM
WHERE (RATING = 'G' AND RENTAL_DURATION >=7) 
OR (RATING = 'PG-13' AND RENTAL_DURATION <=3);

-- 40편이상의 영화를 대여한 모든 고객
SELECT * 
FROM CUSTOMER
INNER JOIN RENTAL
ON CUSTOMER.CUSTOMER_ID = RENTAL.CUSTOMER_ID; -- CUSTOMER_ID가 서로 같다

SELECT CUSTOMER.FIRST_NAME, CUSTOMER.LAST_NAME
FROM CUSTOMER
INNER JOIN RENTAL
ON CUSTOMER.CUSTOMER_ID = RENTAL.CUSTOMER_ID; -- CUSTOME_ID로 통합한 테이블에서 이름만 불러옴

SELECT CUSTOMER.FIRST_NAME, CUSTOMER.LAST_NAME, RENTAL_ID
FROM CUSTOMER
INNER JOIN RENTAL
ON CUSTOMER.CUSTOMER_ID = RENTAL.CUSTOMER_ID; -- CUSTOME_ID로 통합한 테이블에서 이름과 렌탈아이디 불러옴

SELECT CUSTOMER.FIRST_NAME, CUSTOMER.LAST_NAME, RENTAL_ID, COUNT(*) -- 그룹화로 묶은 개수 카운트
FROM CUSTOMER
INNER JOIN RENTAL
ON CUSTOMER.CUSTOMER_ID = RENTAL.CUSTOMER_ID
GROUP BY CUSTOMER.FIRST_NAME, CUSTOMER.LAST_NAME -- 그룹화로 같은 이름 모아줌
HAVING COUNT(*) >= 40; -- 그룹으로 묶인 식은 HAVING문 사용 (WHERE문은 SELECT에서만 사용)

-- 2005년 6월 14일에 영화를 대여한 모든 고객 목록
SELECT CUSTOMER.FIRST_NAME, CUSTOMER.LAST_NAME, RENTAL.RENTAL_DATE
FROM CUSTOMER
INNER JOIN RENTAL
ON CUSTOMER.CUSTOMER_ID = RENTAL.CUSTOMER_ID
WHERE DATE(RENTAL.RENTAL_DATE) = '2005-06-14';

SELECT CUSTOMER.FIRST_NAME, CUSTOMER.LAST_NAME, TIME(RENTAL.RENTAL_DATE) -- 렌탈날짜를 시간으로 나타냄
FROM CUSTOMER
INNER JOIN RENTAL
ON CUSTOMER.CUSTOMER_ID = RENTAL.CUSTOMER_ID
WHERE DATE(RENTAL.RENTAL_DATE) = '2005-06-14'
ORDER BY CUSTOMER.LAST_NAME; -- 이름정렬

-- 부속질의
-- 가격이 10000에서 20000원 책
SELECT * FROM BOOK
WHERE PRICE >=10000 AND PRICE <= 20000;
SELECT * FROM BOOK
WHERE PRICE BETWEEN 10000 AND 20000;

-- IN NOTIN 구문
SELECT * FROM BOOK
WHERE PUBLISHER IN ('굿스포츠', '대한미디어');
SELECT * FROM BOOK
WHERE PUBLISHER NOT IN ('굿스포츠', '대한미디어');

-- LIKE 구문
SELECT BOOKNAME, PUBLISHER FROM BOOK
WHERE BOOKNAME LIKE '%의 %';

SELECT * FROM BOOK
ORDER BY PRICE DESC, PUBLISHER ASC;

-- 집계함수
SELECT SUM(SALEPRICE) AS TOTAL
 FROM ORDERS
WHERE CUSTID=2; -- 김연아의 주문금액

SELECT * FROM ORDERS;

SELECT SUM(SALEPRICE) AS TOTAL,
AVG(SALEPRICE) AS AVERAGE,
MIN(SALEPRICE) AS MININUM,
MAX(SALEPRICE) AS MAXINUM
FROM ORDERS;

SELECT COUNT(*)
FROM ORDERS; -- 행 개수 확인

-- 고객별 총수량, 총판매액
SELECT CUSTID, COUNT(*) AS 도서수량,
SUM(SALEPRICE) AS 총액
FROM ORDERS
GROUP BY CUSTID;

-- 8000원 이상 구입한 사람 중 2권이상 산사람
SELECT CUSTID, COUNT(*)
FROM ORDERS
WHERE SALEPRICE >= 8000
GROUP BY CUSTID
HAVING COUNT(*) >= 2;

USE SAKILA;
SELECT CUSTOMER_ID, COUNT(*)
FROM RENTAL
GROUP BY CUSTOMER_ID -- GROUP문에는 WHERE 못씀 HAVING 써야함
ORDER BY 2 DESC; -- 2는 COUNT(*)를 의미함

SELECT CUSTOMER_ID, COUNT(*)
FROM RENTAL
-- WHERE COUNT(*) >=40 은 안됨
GROUP BY CUSTOMER_ID 
HAVING COUNT(*) >=40
ORDER BY 2 DESC; 

DESCRIBE PAYMENT; -- PAYMENT 정보보기
SELECT *
FROM PAYMENT;

SELECT COUNT(CUSTOMER_ID), -- 구매건수
COUNT(distinct CUSTOMER_ID) -- 중복제거 따라서 고객명수로 볼수있음
FROM PAYMENT;

-- 날짜 빼기 (일 수 구하기)
DESC RENTAL; -- DESCRIBE = DESC
SELECT DATEDIFF(RETURN_DATE, RENTAL_DATE)
FROM RENTAL;

SELECT MAX(DATEDIFF(RETURN_DATE, RENTAL_DATE))
FROM RENTAL;





