# Luggage Hotel
## Resource

**LUGGAGE**


![Image of Yaktocat](https://github.com/dsu-cit-csweb3200/f19-resourceful-ferus2306/blob/master/images/example.jpg)

Attributes:

## USER REGISTRATION
* name (string)
* email (string)
* phone (string)
* password (string)

## CREATE ORDER
* airport (string)
* bagAmount (string)
* pickUpDate (string)
* dropOffDate (string)

# Schema

## REGISTRATION
```sql
CREATE TABLE users (
id INTEGER PRIMARY KEY,
name TEXT,
email TEXT,
phone TEXT,
password TEXT;
```
## CREATE ORDER
```sql
CREATE TABLE orders (
id INTEGER PRIMARY KEY,
bagAMount TEXT,
pickUpDate TEXT,
dropOffDate TEXT,
comment TEXT;
```

## REST Endpoints

Name                           | Method | Path
-------------------------------|--------|------------------
Retrieve  collection | GET    | /orders
Retrieve order member     | GET    | /orders/*\<id\>*
Create order member       | POST   | /orders/
Update order member       | PUT    | /orders/*\<id\>*
Delete order member       | DELETE | /orders/*\<id\>*





