drop table emp;

-- emp 테이블 생성
create table emp (
                     empid integer primary key ,
                     fname varchar(30) not null ,
                     lname varchar(30) not null ,
                     email varchar(100) not null ,
                     phone varchar(15) not null ,
                     hdate date not null ,
                     jobid varchar(20) not null ,
                     sal integer not null ,
                     comm decimal(5,2) ,
                     mgrid integer ,
                     depid integer
);

-- 데이터 추가
insert into emp (empid, fname, lname, email, phone,
                 hdate, jobid, sal, comm, mgrid, depid)
values (100, 'Steven', 'King', 'SKING', '515.123.4567',
        '2003-06-17', 'AD_PRES', 24000, null, null, 90);

-- 데이터 조회 1 - 리스트
select empid, fname, email, jobid, depid from emp;

-- 데이터 조회 2 - 상세
select * from emp where empid = 100;