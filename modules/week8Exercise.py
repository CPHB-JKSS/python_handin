def getShakesBySize(con, size):
    query = "SELECT * FROM milkshakes WHERE size = " + str(size)
    ResultProxy = con.execute(query)
    return ResultProxy.fetchall()


def addNewShakeSQLALCH(con, flavor, size, price):
    query = "INSERT INTO milkshakes (flavor, size, price) VALUES (%s, %s, %s)"
    ResultProxy = con.execute(query, (flavor, size, price))


def addNewShake(cnx, flavor, size, price):
    cur = cnx.cursor(prepared=True)

    query = "INSERT INTO milkshakes (flavor, size, price) VALUES (%s, %s, %s)"
    cur.execute(query, (flavor, size, price))

    cnx.commit()
    cur.close()

def removeShake(con, id):
    query = "DELETE FROM milkshakes WHERE id = %s"
    con.execute(query, (id))

def changeShakePrice(con, id, price):
    query = "UPDATE milkshakes SET price = %s WHERE id = %s"
    con.execute(query, (price, id))
