import pymysql as pm

try:
    conn = pm.connect(host="localhost", user="root", password="", database="parts")

    if conn:
        print("Connection successfully established\n")

    sql = "Select * from parts_table"
    cur = conn.cursor()
    cur.execute(sql)
    result = cur.fetchall()

    # print(result)

    for row, row_data in enumerate(result):
        print(row, "\t", row_data)
        # for col in enumerate(row_number):
        #     print(col)
    print("\n")
    for row, row_data in enumerate(result):
        for column, col_data in enumerate(row_data):
            print(column, "\t", col_data)

    cur2 = conn.cursor()
    cur3 = conn.cursor()

    parts_number = "SELECT COUNT(Distinct partName) FROM parts_table"
    ref_nbr = "select count(Distinct Reference) from parts_table"

    cur2.execute(parts_number)
    cur3.execute(ref_nbr)

    result2 = cur2.fetchone()

    print(type(result2[0]))



except Exception as e:
    print("Error: " + str(e))
