class Shop:
    def __init__(self, name, store_type, capacity):
        self.name = name
        self.type = store_type
        self.capacity = capacity
        self.items = {}

    @classmethod
    def small_shop(cls, name, store_type):
        small_shop_capacity = 10
        return cls(name, store_type, small_shop_capacity)

    def add_item(self, item_name):
        if item_name not in self.items:
            self.items[item_name] = 0
        if sum(self.items.values()) < self.capacity:
            self.items[item_name] += 1
            return f"{item_name} added to the shop"
        return "Not enough capacity in the shop"

    def remove_item(self, item_name, amount):
        if item_name in self.items and self.items[item_name] >= amount:
            self.items[item_name] -= amount
            return f"{amount} {item_name} removed from the shop"
        return f"Cannot remove {amount} {item_name}"

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"