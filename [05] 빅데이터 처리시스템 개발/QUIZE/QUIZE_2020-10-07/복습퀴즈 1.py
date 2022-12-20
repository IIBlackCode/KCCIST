import pymysql

##전역 변수 선언부##
conn, cur = None, None #교량과 트럭

##메인 코드부##
#1. 서버와 교량을 연결
conn = pymysql.connect(host='127.0.0.1',user='root',password='1234',db='school',charset='utf8')
cur = conn.cursor() #빈 트럭 준비

#2. 물건(SQL) 준비 + 트럭에 실어서 부어 넣기
sql = "SELECT * FROM student a, department b WHERE a.student_num = b.stu_num"
cur.execute(sql)

#3. 돌아온 트럭(cur)에서 하나씩 꺼내기
while True:
    row = cur.fetchone()
    if row == None or row == "":
        break
    student_num	 = row[0]
    student_name = row[1]
    student_addr = row[2]
    student_tel	= row[3]
    dep_code = row[4]
    stu_num	 = row[5]
    dep_year = row[6]
    Semester = row[7]
    dep_score= row[8]
    dep_rank = row[9]
    print(student_num,student_name,student_addr,student_tel,dep_code,stu_num,dep_year,Semester,dep_score,dep_rank)

# 끝. 정리하기
cur.close()
conn.close()
