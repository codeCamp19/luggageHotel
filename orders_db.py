import sqlite3

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d



class OrdersDB:
    def __init__ (self):
        self.connection = sqlite3.connect("orders_db.db")
        self.connection.row_factory = dict_factory
        self.cursor = self.connection.cursor() # cursor is itterator 

    def insertOrder(self, airport, bagAmount, pickUpDate, dropOffDate, comment):
        data = [airport, bagAmount, pickUpDate, dropOffDate, comment]
        self.cursor.execute("INSERT INTO orders (airport, bagAmount, pickUpDate, dropOffDate, comment ) VALUES (?,?,?,?,?)", data)    
        self.connection.commit()

    def getOrders(self):
        self.cursor.execute("SELECT * FROM orders") # gives list of tuples which is not usable. 
        result = self.cursor.fetchall()
        return result


    def getOneOrder(self, order_id):
        data = [order_id]
        self.cursor.execute("SELECT * FROM orders WHERE id = ?", data)
        result = self.cursor.fetchone()
        return result


    def deleteOneOrder(self, order_id):
        data = [order_id]
        self.cursor.execute("DELETE FROM orders WHERE id = ?", data)
        self.connection.commit()


    def updateOneOrder(self, airport, bagAmount, pickUpDate, dropOffDate, order_id):
        data = [airport, bagAmount, pickUpDate, dropOffDate, order_id]
        self.cursor.execute("UPDATE orders SET airport = ?, bagAmount = ?, pickUpDate = ?, dropOffDate = ? WHERE id = ?", data)
        self.connection.commit()



    # REGISTER 
    def registerUser(self, name, email, phoneNumber, password):
        data = [name, email, phoneNumber, password]
        self.cursor.execute("INSERT INTO users (name, email, phoneNumber, password) VALUES (?,?,?,?)", data)
        self.connection.commit()
