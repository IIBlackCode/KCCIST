import pymysql

##전역 변수 선언부##
conn, cur = None, None #교량과 트럭

##메인 코드부##
#1. 서버와 교량을 연결
conn = pymysql.connect(host='127.0.0.1',user='root',password='1234',db='company',charset='utf8')
cur = conn.cursor() #빈 트럭 준비

#2. 물건(SQL) 준비 + 트럭에 실어서 부어 넣기
sql = "SELECT * FROM emp a, sal b WHERE a.emp_num = b.empcode;"
cur.execute(sql)

#3. 돌아온 트럭(cur)에서 하나씩 꺼내기
while True:
    row = cur.fetchone()
    if row == None or row == "":
        break
    emp_num	 = row[0]
    emp_name = row[1]
    emp_rank = row[2]
    emp_dep	= row[3]
    emp_tel = row[4]
    emp_account	 = row[5]
    sal_code = row[6]
    empcode = row[7]
    sal_year= row[8]
    sal_month = row[9]
    salary = row[10]
    sal_tax = row[11]
    sal_bonus = row[12]
    print(emp_num,emp_name,emp_rank,emp_dep,emp_tel,emp_account,sal_code,empcode,sal_year,sal_month,salary,sal_tax,sal_bonus)

# 끝. 정리하기
cur.close()
conn.close()
