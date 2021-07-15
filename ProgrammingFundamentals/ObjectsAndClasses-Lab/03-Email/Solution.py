class Email:
    def __init__(self,sender,receiver,message,is_sent = False):
        self.sender = sender
        self.receiver = receiver
        self.message = message
        self.messages = []
        self.is_sent = is_sent
    def send(self):
        self.is_sent = True
    def get_info(self):
        print(f"{self.sender} says to {self.receiver}: {self.message}. Sent: {self.is_sent}")
list_of_messages = []
messages = input()
while messages != "Stop":
    list_of_messages.append(messages)
    messages = input()
indices = list(map(int,input().split(", ")))
for i in range(len(list_of_messages)):
    sen, rec, mes = list_of_messages[i].split()
    email = Email(sen, rec, mes)
    if i in indices:
        email.send()
    email.get_info()