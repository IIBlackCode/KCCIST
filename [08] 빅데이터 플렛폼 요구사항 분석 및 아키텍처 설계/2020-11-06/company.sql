--���̺� ����
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
values('1111','ȫ�浿','����');

--����Ŭ�� ����, ����, ������ commit �ʼ�
commit;
select * from customers;

--
insert into customers --(customer_id,customer_name,customer_address) ������ ������ insert ����
values('1111','ȫ�浿','����');

--�⺻Ű �ִ� ���̺� ����
create table customers2
(
    customer_id number(10) null,
    customer_name varchar2(50) not null,
    customer_address varchar2(255) not null,
    --�⺻Ű ����
    constraint customers2_pk PRIMARY KEY(customer_id)
);
--�⺻Ű �ִ� ���̺� ������ ����
insert into customers2(customer_id,customer_name,customer_address)
values('1111','ȫ�浿','����');
commit;

--�Ȱ��� ���̺� ���Խ� �⺻Ű �ߺ����� ���� �߻�
insert into customers2(customer_id,customer_name,customer_address)
values('1111','ȫ�浿','����');
commit;

--���̺� ������ ���ÿ� �����͸� �ִ� ���
create table customers3

    --������ �ִ� ���̺����� �о� ���̺� ����
    as (select * from customers2)
;
select *from customers3;
--
