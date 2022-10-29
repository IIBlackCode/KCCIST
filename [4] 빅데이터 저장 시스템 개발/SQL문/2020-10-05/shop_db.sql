show databases;
create database test;
show tables;

#2020-10-05 수업 SQL

#DB 생성
CREATE DATABASE shop_db;

#database 지정
USE shop_db; 

#테이블 생성
create table shop_db.user_table (
	user_id 	CHAR(8) NOT NULL,
    user_name CHAR(5) NOT NULL,
    user_age 	INT,
    PRIMARY KEY(user_id)
);

#데이터 입력
INSERT INTO user_table VALUES('AAA','홍길동', 20);
INSERT INTO user_table VALUES('BBB','이순신', 21);

#데이터 출력
SELECT * FROM user_table;
SELECT user_name, user_age FROM user_table;
SELECT * FROM user_table WHERE user_name = '홍길동';
SELECT * FROM user_table WHERE user_age >= 23 ;

#테이블 지정
USE shop_db;

#데이터베이스 목록 보기
SHOW DATABASES;

#테이블 목록 보기
SHOW TABLES;

#데이터 삭제
DROP TABLE user_table;

#DB 삭제
DROP DATABASE shop_db;
