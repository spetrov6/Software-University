class Customer:
    __customers_id = 0

    def __init__(self, name, address, email):
        self.name = name
        self.address = address
        self.email = email
        self.id = Customer.get_next_id()

    @staticmethod
    def get_next_id():
        Customer.__customers_id += 1
        return Customer.__customers_id

    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"
