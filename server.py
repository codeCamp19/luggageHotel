from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
from orders_db import OrdersDB
import json

class MyRequestHandler(BaseHTTPRequestHandler):

  def do_OPTIONS(self):
    self.send_response(200)
    self.send_header("Access-Control-Allow-Origin", "*")
    self.send_header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS")
    self.send_header("Access-Control-Allow-Headers", "Content-Type")
    self.end_headers()

  def do_GET(self):
    if self.path == "/luggage":
      self.handleluggageRetrieveCollection()
    elif self.path.startswith("/luggage/"):
      self.handleluggageRetrieveMember()
    else:
      self.handleNotFound()

  def do_POST(self):
    if self.path == "/luggage":
      self.handleluggageCreate()
    else:
      self.handleNotFound()

  def do_DELETE(self):
    if self.path.startswith("/luggage/"):
      self.handleluggageDelete()
    else:
      self.handleNotFound()

  def do_PUT(self):
    if self.path.startswith("/luggage/"):
      self.handleluggageUpdate()
    else:
      self.handleNotFound()

  def handleNotFound(self):
    self.send_response(404)
    self.end_headers()
    self.wfile.write(bytes("Not found.", "utf-8"))

  def handleluggageRetrieveMember(self):
    parts = self.path.split("/")
    luggage_id = parts[2]
    db = luggageDB()
    luggage = db.retrieveOneluggage(luggage_id)
    if luggage != None:
      self.send_response(200)
      self.send_header("Content-Type", "application/json")
      self.send_header("Access-Control-Allow-Origin", "*")
      self.end_headers()
      self.wfile.write(bytes(json.dumps(luggage), "utf-8"))
    else:
      self.handleNotFound()

  def handleluggageDelete(self):
    parts = self.path.split("/")
    luggage_id = parts[2]
    # retrieve one luggage from the DB by ID
    db = luggageDB()
    luggage = db.retrieveOneluggage(luggage_id)
    if luggage != None:
      db.deleteOneluggage(luggage_id)
      self.send_response(200)
      self.send_header("Content-Type", "application/json")
      self.send_header("Access-Control-Allow-Origin", "*")
      self.end_headers()
      self.wfile.write(bytes(json.dumps(luggage), "utf-8"))
    else:
      self.handleNotFound()

  def handleluggageUpdate(self):
    parts = self.path.split("/")
    luggage_id = parts[2]
    length = self.headers["Content-Length"]
    body = self.rfile.read(int(length)).decode("utf-8")
    print("BODY (string):", body)

    parsed_body = parse_qs(body)
    print("BODY (parsed):", parsed_body)

    airport = parsed_body["airport"][0]
    bagAmount = parsed_body["bagAmount"][0]
    pickUpDate = parsed_body["pickUpDate"][0]
    comment = parsed_body["comment"][0]
    db = luggageDB()
    order_id = db.retrieveOneluggage(luggage_id)
    if luggage != None:
      luggage = db.UpdateOneluggage(airport, bagAmount, pickUpDate, dropOffDate, order_id)
      self.send_response(200)
      self.send_header("Content-Type", "application/json")
      self.send_header("Access-Control-Allow-Origin", "*")
      self.end_headers()
      self.wfile.write(bytes(json.dumps(luggage), "utf-8"))
    else:
      self.handleNotFound()

  def handleluggageRetrieveCollection(self):
    self.send_response(200)
    self.send_header("Content-Type", "application/json")
    self.send_header("Access-Control-Allow-Origin", "*")
    self.end_headers()

    db = luggageDB()
    luggage = db.retrieveluggage()
    self.wfile.write(bytes(json.dumps(luggage), "utf-8"))

  def handleluggageCreate(self):
    length = self.headers["Content-Length"]
    body = self.rfile.read(int(length)).decode("utf-8")
    print("BODY (string):", body)

    parsed_body = parse_qs(body)
    print("BODY (parsed):", parsed_body)

    airport = parsed_body["airport"][0]
    bagAmount = parsed_body["bagAmount"][0]
    pickUpDate = parsed_body["pickUpDate"][0]
    comment = parsed_body["comment"][0]
    db = luggageDB()
    db.insertluggage(airport, bagAmount, pickUpDate, dropOffDate, comment)

    self.send_response(201)
    self.send_header("Access-Control-Allow-Origin", "*")
    self.end_headers()

def run():
  listen = ("127.0.0.1", 8080)
  server = HTTPServer(listen, MyRequestHandler)
  print("Listening...")
  server.serve_forever()
run()

