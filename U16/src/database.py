# Imports

import sqlalchemy as db
from dotenv import load_dotenv, find_dotenv
import os
from sqlalchemy import MetaData, Table, Column
from psycopg2 import Session
from customer import Customer


class Database():
    """Class that handles connection, session and interaction with the database
    """
    load_dotenv(find_dotenv())

    # Import DB configuration from .env file
    user = os.getenv('PG_USER')
    pwd = os.getenv('PG_PWD')
    host = os.getenv('PG_HOST')
    db_name = os.getenv('PG_DB')

    engine = db.create_engine(f"postgresql://{user}:{pwd}@{host}/{db_name}")

    def __init__(self):
        """Constructor
        """
        self.connection = self.engine.connect()
        print("DB Instance created")

    def fetchByQuery(self, query):
        """Prints rows from parameterized table

        :param query: Table to query from
        :type query: String
        """
        fetchQuery = self.connection.execute(f"SELECT * FROM {query}")

        for data in fetchQuery.fetchall():
            print(data)

    def saveData(self, customer):
        """Appends data to table 'customer'

        :param customer: Contains information to append
        :type customer: Customer
        """
        self.connection.execute(f"""INSERT INTO customer(name, age, email
                                , address, zip_code)
                                    VALUES( '{customer.name}',
                                            '{customer.age}',
                                            '{customer.email}',
                                            '{customer.address}',
                                            '{customer.zip_code}')""")

    def updateCustomer(self, customerName, address):
        """Updates customer address

        :param customerName: Customer name to perform filtering
        :type customerName: String
        :param address: New address
        :type address: String
        """
        session = Session(bind=self.connection)
        dataToUpdate = {Customer.address: address}
        customerData = session.query(Customer).filter
        (Customer.name == customerName)
        customerData.update(dataToUpdate)
        session.commit()

    def deleteCustomer(self, customer):
        """Deletes customer

        :param customer: Customer to be deleted
        :type customer: Customer
        """
        session = Session(bind=self.connection)
        customerData = session.query(Customer).filter
        (Customer.name == customer).first()
        session.delete(customerData)
        session.commit()

    def fetchUserByName(self):
        """Fetches column name from table customer
        """
        meta = MetaData()
        customer = Table('customer', meta, Column('name'))
        data = self.connection.execute(customer.select())

        for cust in data:
            print(cust)

    def fetchAllUsers(self):
        """Fetches every row of table customer
        """
        self.session = Session(bind=self.connection)
        customers = self.session.query(Customer).all()
        for cust in customers:
            print(cust)
