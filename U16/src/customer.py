from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

Base = declarative_base()


class Customer():
    """Class to contain the properties of a customer

    :param name: Customer's name
    :type name: String
    :param age: Customer's age
    :type age: int
    :param email: Customer's email
    :type email: String
    :param address: Customer's address
    :type address: String
    :param zip_code: Customer's Zip code
    :type zip_code: String
    """
    __tablename__ = 'customer'
    name = Column(String)
    age = Column(Integer)
    email = Column(String)
    address = Column(String)
    zip_code = Column(String)
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return "<Customer(name='%s', age='%s', email='%s', address='%s', zip_code='%s')>" % (self.name, self.age, self.email, self.address, self.zip_code)

    def __init__(self, name, age, email, address, zip_code):
        self.name = name
        self.age = age
        self.email = email
        self.address = address
        self.zip_code = zip_code

