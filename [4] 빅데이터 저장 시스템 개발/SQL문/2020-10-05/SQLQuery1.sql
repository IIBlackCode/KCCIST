--DB 생성
CREATE DATABASE shop_db;

--database 지정
USE shop_db; 

drop table user_table;

--테이블 생성
create table user_table (
	user_id 	CHAR(8) NOT NULL,
	--CQurry Server에서 한글자씩 취급하는 함수 NCHAR
    user_name NCHAR(5) NOT NULL,
    user_age 	INT,
    PRIMARY KEY(user_id)
);

--데이터 입력
INSERT INTO user_table VALUES('AAA','홍길동', 20);
INSERT INTO user_table VALUES('BBB','이순신', 21);

--데이터 출력
SELECT * FROM user_table;
SELECT user_name, user_age FROM user_table;
SELECT * FROM user_table WHERE user_name = '홍길동';
SELECT * FROM user_table WHERE user_age >= 23 ;

--테이블 지정
USE shop_db;

--데이터 삭제
DROP TABLE user_table;

--DB 삭제
USE TEMPDB;
DROP DATABASE shop_db;