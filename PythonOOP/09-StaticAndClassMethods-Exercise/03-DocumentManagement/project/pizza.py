class Pizza:
    def __init__(self, name, dough, topping_capacity):
        self.name = name
        self.dough = dough
        self.toppings_capacity = topping_capacity
        self.toppings = {}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value:
            self.__name = value
            return
        raise ValueError("The name cannot be an empty string")
    
    @property
    def dough(self):
        return self.__dough
    
    @dough.setter
    def dough(self, value):
        if value:
            self.__dough = value
            return
        raise ValueError("You should add dough to the pizza")

    @property
    def toppings_capacity(self):
        return self.__toppings_capacity

    @toppings_capacity.setter
    def toppings_capacity(self, value):
        if value > 0:
            self.__toppings_capacity = value
            return
        raise ValueError("The topping's capacity cannot be less or equal to zero")

    def add_topping(self, topping):
        if len(self.toppings) < self.__toppings_capacity:
            topping_type = topping.topping_type
            topping_weigh = topping.weight

            if topping_type not in self.toppings:
                self.toppings[topping_type] = topping_weigh
            else:
                self.toppings[topping_type] += topping_weigh

            return

        raise ValueError("Not enough space for another topping")

    def calculate_total_weight(self):
        return self.dough.weight + self.__calculate_total_toppings_weight()

    def __calculate_total_toppings_weight(self):
        toppings_weight = 0
        for topping_weight in self.toppings.values():
            toppings_weight += topping_weight
        return toppings_weight

