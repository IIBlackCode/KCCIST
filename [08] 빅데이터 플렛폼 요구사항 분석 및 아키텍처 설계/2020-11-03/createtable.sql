DROP TABLE grade;
DROP TABLE member;
DROP TABLE dept;

CREATE TABLE dept
    ( dept_id    NUMBER(4)
    , dept_name  VARCHAR2(30)
    , loc_id      NUMBER(4)
    ,CONSTRAINT deptid_pk
       		 PRIMARY KEY (dept_id));

CREATE TABLE member 
    ( member_id    NUMBER(6)
    , name      VARCHAR2(25) NOT NULL
    , hire      DATE
    , jikwi     VARCHAR2(10)	
    , sal   NUMBER(8,2)
    , bonus NUMBER(5)
    , mgr     NUMBER(6)
    , dept_id  NUMBER(4)
    ,CONSTRAINT     member_member_id_pk
                     PRIMARY KEY (member_id)
    ,CONSTRAINT     member_deptid_fk
                     FOREIGN KEY (dept_id)
                      REFERENCES dept) ;


INSERT INTO dept VALUES (10,'총무부',100);
INSERT INTO dept VALUES (20,'인사부',200);
INSERT INTO dept VALUES (30,'영업부',300);
INSERT INTO dept VALUES (40,'감사팀',400);
INSERT INTO dept VALUES (50,'전산팀',500);


INSERT INTO member VALUES(100,'배기수', TO_DATE('1987-05-04', 'yyyy-mm-dd'),'사장', 54000, 40, NULL,10);
INSERT INTO member VALUES(101,'홍길동', TO_DATE('1990-06-17', 'yyyy-mm-dd'),'부장', 12000, 30, 100,20);
INSERT INTO member VALUES(102,'차승호', TO_DATE('2001-06-03', 'yyyy-mm-dd'),'부장', 11000, 10, 100,30);
INSERT INTO member VALUES(103,'김주부', TO_DATE('2000-01-01', 'yyyy-mm-dd'),'과장', 14000, NULL, 102,30);
INSERT INTO member VALUES(104,'황기훈', TO_DATE('2001-01-15', 'yyyy-mm-dd'),'과장', 30000, NULL, 101,20);
INSERT INTO member VALUES(105,'정수미', TO_DATE('2003-12-10', 'yyyy-mm-dd'),'대리', 24000, NULL, 104,20);
INSERT INTO member VALUES(106,'권민수', SYSDATE,'사원', 4000, NULL, NULL, 50);
INSERT INTO member VALUES(107,'김지희', SYSDATE,'사원', 5000, NULL, 105, NULL);

CREATE TABLE grade
(grade_level VARCHAR2(3),
 lowest_sal  NUMBER,
 highest_sal NUMBER);

INSERT INTO grade
VALUES ('A', 1000, 2999);

INSERT INTO grade
VALUES ('B', 3000, 5999);

INSERT INTO grade
VALUES('C', 6000, 9999);

INSERT INTO grade
VALUES('D', 10000, 14999);

INSERT INTO grade
VALUES('E', 15000, 24999);

INSERT INTO grade
VALUES('F', 25000, 40000);

