# 내 windows 로컬과 연동 성공 !
import pymysql
conn = pymysql.connect(host='localhost', user='root', password ='root', db='test_orm',port =3306, charset='utf8')
print(1)
name = "jjj"
math = 80
english = 20
try: # 자원을 할당해주고 해제해주지 않으면 close해도 에러난다.
    with conn.cursor() as curs:
    
        query = """Insert into test_table VALUES ( %s, %s, %s)"""
        curs.execute(query, (name, math, english,))
        conn.commit()
finally:
    conn.close()