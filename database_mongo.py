import pymongo
from pymongo import MongoClient

#Using MongoDB database, IP: 0.0.0.0/0, password: customerAccounting, https://www.mongodb.com/try/download/community
def find_data():
    CONNECTION_STRING = "mongodb+srv://robinfintz:customerAccounting@cluster0.szon0.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    myCluster = MongoClient(CONNECTION_STRING)
    return myCluster["Accounting"]


def insert_customer(db, data):
    customers = db["Customers"]
    customersPost = data
    customers.insert_one(customersPost)
    return customers.find_one(customersPost)

def insert_order(db, data):
    orders = db["Orders"]
    ordersPost = data
    orders.insert_one(ordersPost)
    return orders.find_one(ordersPost)
    

def retrieve_all_customers(db):
    customers = db["Customers"]
    return customers.find({})