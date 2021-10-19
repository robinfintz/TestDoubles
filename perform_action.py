import database_mongo

def do_insert_customer(db, customer_data):
    return database_mongo.insert_customer(db, customer_data)

def do_insert_order(db, order_data):
    return database_mongo.insert_order(db, order_data)

def do_retrieve_customers(db):
    return database_mongo.retrieve_all_customers(db)

