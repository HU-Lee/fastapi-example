-- 접속
-- psql -U postgres

-- test라는 DB를 만든다
create database test owner postgres;

-- test DB 전환
-- \c test postgres

create sequence seq_kor;

create table tb_covidkor (
    id int not null default nextval('seq_kor'),
    date varchar(20) not null,
    detected int,
    death int
);

create sequence seq_inter;

create table tb_covidinter (
    id int not null default nextval('seq_inter'),
    date varchar(20) not null,
    jap int,
    usa int
);