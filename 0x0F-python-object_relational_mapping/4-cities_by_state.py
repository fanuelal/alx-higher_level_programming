#!/usr/bin/python3
"""a script that lists all cities from the database hbtn_0e_4_usa"""
if __name__ == '__main__':
    import MySQLdb
    import sys
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM cities ORDER BY cities.id ASC")
    datas = cur.fetchall()
    for data in datas:
        print(data)
