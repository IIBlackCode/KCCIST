import pymysql;


##전역 변수 선언부
conn,cur = None, None

##메인 코드부
#1. (1) 서버와 교량을 연결, 빈 트럭 준비
conn = pymysql.connect(host='127.0.0.1',user='root',password='1234',db='hanbitDB', charset='utf8');

#1. (2) SQL 준비
cur = conn.cursor();
sql = "SELECT * FROM user_table"
cur.execute(sql)

row = cur.fetchone();
uid = row[0]
uname = row[1]
uemail = row[2]
byear = row[3]

print(uid, uname, uemail, byear);

cur.execute(sql);
conn.close()
print('OK')
