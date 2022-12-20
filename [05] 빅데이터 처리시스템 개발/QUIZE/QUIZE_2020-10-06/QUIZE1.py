## 전역 변수 선언부
import pymysql
conn, cur = None, None # 교량과 트럭

## 메인 코드부
#1. 서버와 교량을 연결하고, 빈트럭 준비
conn = pymysql.connect(host='192.168.56.101',user='winUser',password='1234',database='slqDB_KMS', charset='utf8');
cur = conn.cursor() # 빈 트럭 준비

#2. 트럭에 실을 물건(SQL)을 준비
sql = "CREATE TABLE IF NOT EXISTS userTbl_KMS ("
sql += "member_id CHAR(5) NOT NULL,"
sql += "member_name CHAR(5) NOT NULL,"
sql += "member_birth INT NOT NULL,"
sql += "member_loc CHAR(5) NOT NULL,"
sql += "member_gnum	INT NULL,"
sql += "member_tel INT	NULL,"
sql += "member_tall INT	NOT NULL,"
sql += "member_joined DATE NOT NULL,"
sql += "PRIMARY KEY(member_id)"
sql += ")"
cur.execute(sql)

sql = "CREATE TABLE IF NOT EXISTS buyTbl_KMS ("
sql += "buy_num INT AUTO_INCREMENT ,"
sql += "buy_id CHAR(5) NOT NULL,"
sql += "buy_name CHAR(5) NOT NULL,"
sql += "buy_kind CHAR(5) NULL,"
sql += "buy_pri INT NOT NULL,"
sql += "buy_cnt	INT NOT NULL,"
sql += "PRIMARY KEY(buy_num),"
sql += "FOREIGN KEY(buy_id) REFERENCES userTbl_KMS(member_id)"
sql += ")"
cur.execute(sql)

#2. INSERT QUERRY
# member_id, member_name, member_birth, member_loc, member_gnum, member_tel, member_tall, member_joined,= None, None, None, None, None, None, None, None
sql  = "INSERT INTO userTbl_KMS VALUES('LSG', '이승기', 1987, '서울', '011', '1111111', 182, '2008-8-8')"
cur.execute(sql)
sql = "INSERT INTO userTbl_KMS VALUES('KBS', '김범수', 1979, '경남', '011', '2222222', 173, '2012-4-4')"
cur.execute(sql)
sql = "INSERT INTO userTbl_KMS VALUES('KKH', '김경호', 1971, '전남', '019', '3333333', 177, '2007-7-7')"
cur.execute(sql)
sql = "INSERT INTO userTbl_KMS VALUES('JYP', '조용필', 1950, '경기', '011', '4444444', 166, '2009-4-4')"
cur.execute(sql)
sql = "INSERT INTO userTbl_KMS VALUES('SSK', '성시경', 1979, '서울', NULL  , NULL ,186, '2013-12-12')"
cur.execute(sql)
sql = "INSERT INTO userTbl_KMS VALUES('LJB', '임재범', 1963, '서울', '016', '6666666', 182, '2009-9-9')"
cur.execute(sql)
sql = "INSERT INTO userTbl_KMS VALUES('YJS', '윤종신', 1969, '경남', NULL  , NULL ,170, '2005-5-5')"
cur.execute(sql)
sql = "INSERT INTO userTbl_KMS VALUES('EJW', '은지원', 1972, '경북', '011', '8888888', 174, '2014-3-3')"
cur.execute(sql)
sql = "INSERT INTO userTbl_KMS VALUES('JKW', '조관우', 1965, '경기', '018', '9999999', 172, '2010-10-10')"
cur.execute(sql)
sql = "INSERT INTO userTbl_KMS VALUES('BBK', '바비킴', 1973, '서울', '010', '0000000', 176, '2013-5-5')"
cur.execute(sql)

sql = "INSERT INTO buyTbl_KMS VALUES(NULL, 'KBS', '운동화', NULL   , 30,   2)"
cur.execute(sql)
sql = "INSERT INTO buyTbl_KMS VALUES(NULL, 'KBS', '노트북', '전자', 1000, 1)"
cur.execute(sql)
sql = "INSERT INTO buyTbl_KMS VALUES(NULL, 'JYP', '모니터', '전자', 200,  1)"
cur.execute(sql)
sql = "INSERT INTO buyTbl_KMS VALUES(NULL, 'BBK', '모니터', '전자', 200,  5)"
cur.execute(sql)
sql = "INSERT INTO buyTbl_KMS VALUES(NULL, 'KBS', '청바지', '의류', 50,   3)"
cur.execute(sql)
sql = "INSERT INTO buyTbl_KMS VALUES(NULL, 'BBK', '메모리', '전자', 80,  10)"
cur.execute(sql)
sql = "INSERT INTO buyTbl_KMS VALUES(NULL, 'SSK', '책'    , '서적', 15,   5)"
cur.execute(sql)
sql = "INSERT INTO buyTbl_KMS VALUES(NULL, 'EJW', '책'    , '서적', 15,   2)"
cur.execute(sql)
sql = "INSERT INTO buyTbl_KMS VALUES(NULL, 'EJW', '청바지', '의류', 50,   1)"
cur.execute(sql)
sql = "INSERT INTO buyTbl_KMS VALUES(NULL, 'BBK', '운동화', NULL   , 30,   2)"
cur.execute(sql)
sql = "INSERT INTO buyTbl_KMS VALUES(NULL, 'EJW', '책'    , '서적', 15,   1)"
cur.execute(sql)
sql = "INSERT INTO buyTbl_KMS VALUES(NULL, 'BBK', '운동화', NULL   , 30,   2)"
cur.execute(sql)

conn.commit()


# 끝. 정리하기

cur.close()
conn.close()
print('Ok')
