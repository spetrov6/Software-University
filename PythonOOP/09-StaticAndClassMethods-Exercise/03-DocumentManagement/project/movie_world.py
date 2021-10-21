class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        movieworld_dvd_capacity = 15
        return movieworld_dvd_capacity

    @staticmethod
    def customer_capacity():
        movieworld_customer_capacity = 10
        return movieworld_customer_capacity

    def add_customer(self, customer):
        if len(self.customers) < MovieWorld.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if len(self.dvds) < MovieWorld.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        customer = [customer for customer in self.customers if customer.id == customer_id][0]
        dvd = [dvd for dvd in self.dvds if dvd.id == dvd_id][0]

        if not dvd.is_rented:
            if customer.age >= dvd.age_restriction:
                customer.rented_dvds.append(dvd)
                dvd.is_rented = True
                return f"{customer.name} has successfully rented {dvd.name}"

            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"

        return "DVD is already rented"

    def return_dvd(self, customer_id, dvd_id):
        customer = [customer for customer in self.customers if customer.id == customer_id][0]
        dvd = [dvd for dvd in self.dvds if dvd.id == dvd_id][0]

        if dvd in customer.rented_dvds:
            customer.rented_dvds.remove(dvd)
            dvd.is_rented = False
            return f"{customer.name} has successfully returned {dvd.name}"

        return f"{customer.name} does not have that DVD"

    def __repr__(self):
        result = [f"{repr(customer)}\n" for customer in self.customers]
        result += [f"{repr(dvd)}\n" for dvd in self.dvds]
        return "".join(result)

