--1. 다음과 같이 [학생성적 테이블]을 설계한다.
--		테이블 개수는 1개 또는 여러개 관계없다.
-- 	학번, 이름, 주소, 연락처, 학과, 입학연도, 과목명, 수강학기, 점수, 과목석차 
--		학생 테이블 : 학번, 이름, 주소, 연락처, 

CREATE DATABASE school;
USE school;

DROP TABLE student;
CREATE TABLE student (
	student_num		INT 			NOT NULL AUTO_INCREMENT,	##학번
	student_name 	CHAR(5) 		NOT NULL,						##이름
	student_addr	VARCHAR(30)	NULL,								##주소
	student_tel		INT			NULL,								##연락처
	student_year	SMALLINT 	NOT NULL,						##입학년도
	PRIMARY KEY(student_num)
);

-- 학과 테이블 : 학과,학생코드(FK), 입학연도, 과목명, 수강학기, 점수, 과목석차
DROP TABLE department;
CREATE TABLE department (
	dep_code			INT		NOT NULL,	##학과
	stu_num			INT		NULL,			##학생코드(FK)
	dep_sub			CHAR(10)	NOT NULL,	##과목명
	Semester			CHAR(10) NOT NULL,	##수강학기
	dep_score		INT		NOT NULL,	##점수
	dep_rank			INT 		NOT NULL,	##과목석차
	PRIMARY KEY(dep_code),
	FOREIGN KEY(stu_num) REFERENCES student(student_num)
);

SELECT * FROM department;

--2. 위 테이블을 MySQL Server에 만들고 학생2명을 각 3과목씩 입력한다.

INSERT INTO student VALUES(0, '이승기', '서울', '011111111',2007);
INSERT INTO student VALUES(2, '한가인', '인천', '010222222',2008);

INSERT INTO department VALUES(1, 1,  '교육심리학개론','1학기',70,10);
INSERT INTO department VALUES(2, 1,  '범죄심리학개론','2학기',80,5);
INSERT INTO department VALUES(3, 1,  '죄형법정주의'	 ,'2학기',90,3);

INSERT INTO department VALUES(4, 2,  '교육심리학개론','1학기',91,5);
INSERT INTO department VALUES(5, 2,  '범죄심리학개론','1학기',92,4);
INSERT INTO department VALUES(6, 2,  '죄형법정주의'	 ,'2학기',93,2);

SELECT * FROM student a, department b
WHERE a.student_num = b.stu_num;



--3. 입력된 데이터 조회하는 Python 코드를 작성한다.
