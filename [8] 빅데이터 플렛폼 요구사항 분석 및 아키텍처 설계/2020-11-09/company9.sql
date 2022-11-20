select * from member;
select * from member where dept_id > all(10, 20, 30);
select * from member where dept_id > 10 and
dept_id > 20 and dept_id > 30;
select * from member where dept_id > any(10, 20, 30);
select * from member where dept_id > 10 or
dept_id > 20 or dept_id > 30;
select * from member where dept_id > any(
select dept_id from dept where dept_id > 10);
select * from member where dept_id > all(
select dept_id from dept where dept_id > 10);
select * from member where 
exists (select * from dept where member.dept_id = dept.dept_id);
select * from member, dept
where member.dept_id = dept.dept_id;

select name, dept_id, sal from member where (sal, dept_id) in 
(select sal, dept_id from member where bonus is not null);

select name, jikwi, sal from member
where sal > ALL(select sal from member where jikwi = '°úÀå');

select s.name, s.sal, s.dept_id, t.dept_avg from member s,  
(select dept_id, avg(sal) dept_avg from member group by dept_id) t
where s.dept_id = t.dept_id
and s.sal > t.dept_avg;

insert into dept(dept_id, dept_name, loc_id)
values(60, '±³À°ÆÀ', 600);
commit;
select * from dept;
update member set sal = 6000 where name = '±èÁöÈñ';
commit;
select * from member;
delete from member where name = '±èÁöÈñ';
rollback;
select member_id, name from member
where sal > (select avg(sal) from member);


