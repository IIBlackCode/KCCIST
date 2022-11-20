--테이블 생성
create table customers
(
    customer_id number(10) null,
    customer_name varchar2(50) not null,
    customer_address varchar2(255) not null
);

--??
desc customers;

--Data Insert
insert into customers(customer_id,customer_name,customer_address)
values('1111','홍길동','서울');

--오라클은 수정, 삭제, 삽입후 commit 필수
commit;
select * from customers;

--
insert into customers --(customer_id,customer_name,customer_address) 순서만 맞으면 insert 가능
values('1111','홍길동','서울');

--기본키 있는 테이블 생성
create table customers2
(
    customer_id number(10) null,
    customer_name varchar2(50) not null,
    customer_address varchar2(255) not null,
    --기본키 생성
    constraint customers2_pk PRIMARY KEY(customer_id)
);
--기본키 있는 테이블에 데이터 삽입
insert into customers2(customer_id,customer_name,customer_address)
values('1111','홍길동','서울');
commit;

--똑같은 테이블 삽입시 기본키 중복으로 에러 발생
insert into customers2(customer_id,customer_name,customer_address)
values('1111','홍길동','서울');
commit;

--테이블 생성과 동시에 데이터를 넣는 방법
create table customers3

    --기존에 있는 테이블결과를 읽어 테이블 생성
    as (select * from customers2)
;
select *from customers3;
--
