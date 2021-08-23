class Vehicle:
    def __init__(self,car_type,model,price):
        self.type = car_type
        self.model = model
        self.price = int(price)
        self.owner = None
    def buy(self,money,owner):
        if self.owner is None and int(money) >= self.price:
            self.owner = owner
            return f"Successfully bought a {self.type}. Change: {float(money) - self.price:.2f}"
        elif int(money) < self.price:
            return "Sorry, not enough money"
        elif self.owner is not None:
            return "Car already sold"
    def sell(self):
        if self.owner is None:
            return "Vehicle has no owner"
        else:
            self.owner = None
    def __repr__(self):
        if self.owner is None:
            return f"{self.model} {self.type} is on sale: {self.price}"
        else:
            return f"{self.model} {self.type} is owned by: {self.owner}"
