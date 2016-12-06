# -*-encoding: utf-8-*-
import MySQLdb

db = MySQLdb.connect("localhost", "ljy", "1qaz2wsx", "ljy")

cursor = db.cursor()
#
# # 如果数据表已经存在使用 execute() 方法删除表。
# cursor.execute("DROP TABLE IF EXISTS COUPON")
#
#
#
# # 创建数据表SQL语句
# sql = """CREATE TABLE COUPON (
#          COUPON_ID  MEDIUMINT NOT NULL,
#          COUPON_LEVEL TINYINT,
#          DESCRIPTION TEXT,
#          PRIMARY KEY (COUPON_ID))"""
# cursor.execute(sql)
#
# for i in range(0, 20):
#     insert = """INSERT INTO COUPON (
#                 COUPON_ID, COUPON_LEVEL, DESCRIPTION)
#                 VALUES (%d, 20, "Congratulations!")
#                 """ %i
#     cursor.execute(insert)
# try:
#     db.commit()
# except:
#     db.rollback()
# db.close()

sql = """SELECT COUPON_ID FROM COUPON \
          WHERE COUPON_ID > 10"""

try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for coupon in results:
        cid = coupon[0]
        level = coupon[1]
        des = coupon[2]
        print cid, level, des
except:
    print
finally:
    db.close()
