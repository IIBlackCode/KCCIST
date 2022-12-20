import pymysql;

##전역 변수 선언부
conn,cur = None, None

##메인 코드부
#1. (1) DB서버 Connection 정보
conn = pymysql.connect(host='127.0.0.1',user='root',password='1234',db='hanbitDB', charset='utf8');

#1. (2) Connection
cur = conn.cursor();

#2. Ready to SQL
sql = "CREATE TABLE IF NOT EXISTS user_table(uid CHAR(8), uname CHAR(5),"
sql += "uemail CHAR(20), byear INT)"

while True :
    uid, uname, uemail, byear = None, None, None, None
    uid = input('아이디-->')
    if uid == "" or uid ==None :
        break
    uname = input('이름-->')
    uemail = input('메일-->')
    byear = int(input('생년-->'))
    sql = "INSERT INTO user_table VALUES('" + uid + "', '"
    sql += uname + "', '" + uemail + "', " + str(byear) + ")"

    #3. Execute SQL
    cur.execute(sql);
    conn.close()
    print('OK')
