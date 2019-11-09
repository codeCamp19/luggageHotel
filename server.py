from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
from orders_db import OrdersDB
import json
from passlib.hash import bcrypt
from http import cookies


# Subclassing
class MyRequestHandler(BaseHTTPRequestHandler):

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods","GET, POST,PUT, DELETE, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Control-Type")
        self.end_headers()
        

    def do_DELETE(self):
        if self.path.startswith("/orders/"):
            self.handleOrderDelete()
        else:
            self.handleNotFound()


    def do_GET(self):
        print("The Path is: ",self.path)
        if self.path == "/orders":
            self.handleOrdersRetrieve()
        elif self.path.startswith("/orders/"):
            self.handleOrderRetrieve() 
        else:
            self.handleNotFound()

    def do_PUT(self):
        if self.path.startswith("/orders/"):
            self.handleOrderEdit()
        else:
            self.handleNotFound()


    def do_POST(self):
        if self.path == "/orders":
            self.handleOrderInsert()
        elif self.path == "/users":
            self.handleUserRegister()
        else:
            self.handleNotFound()

    def handleUserRegister(self):
        length = self.headers["Content-length"]
        body = self.rfile.read(int(length)).decode("utf-8")

        print("BODY This is what I pass via POST:", body)
        # TODO: parse the body string into a dictionary using pasts_qs()
        parsed_body = parse_qs(body) # the code is automatically decoded. 
        # TODO: save the restautnat into our list of restauants. 
        print("PARSED BODY:", parsed_body)
        # use if else statement to check if the key value exists. 
        name = parsed_body["name"][0] 
        email = parsed_body["email"][0]
        phoneNumber = parsed_body["number"][0]
        password = parsed_body["password"][0]

        # Need to run hashing algorithm on the inserted password. 
        # hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
        hashed_password = bcrypt.hash(password)

        # instantiate your class and insert
        db = OrdersDB()
        db.registerUser(name,email,phoneNumber,hashed_password)
        
        #respond to the client 
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()


# SUPPORTING FUNCTIONS
    def handleOrderInsert(self):
        length = self.headers["Content-length"]
        body = self.rfile.read(int(length)).decode("utf-8")

        print("BODY This is what I pass via POST:", body)
        # TODO: parse the body string into a dictionary using pasts_qs()
        parsed_body = parse_qs(body) # the code is automatically decoded. 
        # TODO: save the restautnat into our list of restauants. 
        print("PARSED BODY:", parsed_body)
        # use if else statement to check if the key value exists. 
        airport = parsed_body["airport"][0] 
        bagAmount = parsed_body["bagAmount"][0]
        pickUpDate = parsed_body["pickUpDate"][0]
        dropOffDate = parsed_body["dropOffDate"][0]
        comment = parsed_body["comment"][0]


        # instantiate your class and insert
        db = OrdersDB()
        db.insertOrder(airport, bagAmount, pickUpDate, dropOffDate, comment)
        
        #respond to the client 
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()


    def handleOrderEdit(self):
        parts = self.path.split("/")
        order_id = parts[2]

        db = OrdersDB()
        order = db.getOneOrder(order_id)
        if order != None:
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            length = self.headers["Content-length"]
            body = self.rfile.read(int(length)).decode("utf-8")
            parsed_body = parse_qs(body) # the code is automatically decoded. 

            airport = parsed_body["airport"][0] 
            bagAmount = parsed_body["bagAmount"][0]
            pickUpDate = parsed_body["pickUpDate"][0]
            dropOffDate = parsed_body["dropOffDate"][0]

            db.updateOneOrder(airport, bagAmount, pickUpDate, dropOffDate, order_id)
        else:
            self.handleNotFound()
            self.wfile.write(bytes("Record doesn't exist", "utf-8")) 

    def handleOrderDelete(self):
        parts = self.path.split("/")
        order_id = parts[2]

        db = OrdersDB()
        order = db.getOneOrder(order_id)
        if order != None:
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            db.deleteOneOrder(order_id)
            self.wfile.write(bytes(json.dumps(order), "utf-8")) 
        else:
            self.handleNotFound()
            self.wfile.write(bytes("Record doesn't exist", "utf-8")) 


    def handleNotFound(self):
        self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes("Not found here.", "utf-8"))

    def handleOrdersRetrieve(self):
        self.send_response(200)
        self.send_header("Content-Type", "application/json") 
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        # send a body
        db = OrdersDB()
        orders = db.getOrders()
        self.wfile.write(bytes(json.dumps(orders), "utf-8")) 

    def handleOrderRetrieve(self):
        parts = self.path.split("/")
        order_id = parts[2]

        db = OrdersDB()
        order = db.getOneOrder(order_id)


        if order != None:
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(bytes(json.dumps(order), "utf-8"))

        else:
            self.handleNotFound()
            self.wfile.write(bytes("You want a order with ID: " + order_id, "utf-8"))
        

def run():
    listen = ("127.0.0.1", 8080)

    #you can't run any ports under 1024 without root access. 
    server = HTTPServer(listen, MyRequestHandler)

    #start the server. Runs until it stops. 
    #This method never returns anything. 
    print("Listening...")
    server.serve_forever()

run()
