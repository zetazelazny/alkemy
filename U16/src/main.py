from customer import Customer
from database import Database

if __name__ == '__main__':
    customer = Customer("Matias", 23, "mz@gmail.com", "Mi casa", "1111")
    db = Database()
    # db.saveData(customer)
    # db.fetchByQuery('public.customer')
    db.fetchUserByName()
