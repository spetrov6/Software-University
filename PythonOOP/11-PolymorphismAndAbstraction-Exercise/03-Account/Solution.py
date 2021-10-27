class Account:
    def __init__(self, owner, amount=0, transactions=None):
        self.owner = owner
        self.amount = amount
        if not transactions:
            self._transactions = []
        else:
            self._transactions = transactions

    @property
    def transactions(self):
        return self._transactions

    @property
    def balance(self):
        return sum(self.transactions) + self.amount

    def add_transaction(self, amount):
        if isinstance(amount, int):
            self.transactions.append(amount)
            return
        raise ValueError("please use int for amount")

    @staticmethod
    def validate_transaction(account, amount_to_add):
        if account.balance + amount_to_add > 0:
            account.transactions.append(amount_to_add)
            return f"New balance: {account.balance}"
        raise ValueError("sorry cannot go in debt!")

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __repr__(self):
        return f"Account({self.owner}, {self.amount})"

    def __len__(self):
        return len(self.transactions)

    def __getitem__(self, index):
        return self.transactions[index]

    def __iter__(self):
        for trans in self.transactions:
            yield trans

    def __add__(self, other):
        all_transactions = []
        all_transactions.extend(self.transactions), all_transactions.extend(other.transactions)
        return Account(f"{self.owner}&{other.owner}", self.amount + other.amount, all_transactions)

    def __gt__(self, other):
        return self.balance > other.balance

    def __ge__(self, other):
        return self.balance >= other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __le__(self, other):
        return self.balance <= other.balance

    def __eq__(self, other):
        return self.balance == other.balance

    def __ne__(self, other):
        return self.balance != other.balance