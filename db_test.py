import unittest
from unittest import mock
import mongomock

import perform_action

class TestMongo(unittest.TestCase):
    #mock
    def test_insert_customer(self):
        mongo_client = mongomock.MongoClient()
        dbNames = mongo_client.database_names
        db = mongo_client.get_database(dbNames)
        db.create_collection("Customers")
        customer_data = {"id": 200, "name": "Borislava", "totalGoodsPurchased": 6}
        perform_action.do_insert_customer(db, customer_data)
        self.assertTrue(db.get_collection("Customers").count_documents({"name": 'Borislava'}) == 1, "Did not insert customer Borislava")
        if(db.get_collection("Customers").count_documents({"name": 'Borislava'}) == 1):
            print("Customer inserted")
    
    #mock
    def test_insert_order(self):
        mongo_client = mongomock.MongoClient()
        dbNames = mongo_client.database_names
        db = mongo_client.get_database(dbNames)
        db.create_collection("Orders")
        order_data = {"customer_id": 102, "goodsPurchased": 25}
        perform_action.do_insert_order(db, order_data)
        self.assertTrue(db.get_collection("Orders").count_documents({"customer_id": 102}) == 1, "Did not insert order with customer id 102")
        if(db.get_collection("Orders").count_documents({"customer_id": 102}) == 1):
            print("Order inserted")

    #mock
    def test_retrieve_customers(self):
        mongo_client = mongomock.MongoClient()
        dbNames = mongo_client.database_names
        db = mongo_client.get_database(dbNames)
        db.create_collection("Customers")
        customer_data_1 = {"id": 200, "name": "Slava", "totalGoodsPurchased": 1}
        customer_data_2 = {"id": 201, "name": "Igor", "totalGoodsPurchased": 2}
        customer_data_3 = {"id": 202, "name": "Igor", "totalGoodsPurchased": 3}
        perform_action.do_insert_customer(db, customer_data_1)
        perform_action.do_insert_customer(db, customer_data_2)
        perform_action.do_insert_customer(db, customer_data_3)
        res = [customer_data_1, customer_data_2, customer_data_3]
        self.assertTrue(db.get_collection("Customers").count_documents({"name": "Slava"}) == 1, "Missing customer: Slava")
        self.assertTrue(db.get_collection("Customers").count_documents({"name": "Igor"}) == 2, "There are not two Igors in this customer dataset")
        print("Retrieved all customers")

myTest = TestMongo()
myTest.test_insert_customer()
myTest.test_insert_order()
myTest.test_retrieve_customers()
