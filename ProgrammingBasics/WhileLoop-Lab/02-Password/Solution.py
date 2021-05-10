user_name = input()
user_password = input()
password = input()
while password != user_password:
    password = input()
print(f"Welcome {user_name}!")