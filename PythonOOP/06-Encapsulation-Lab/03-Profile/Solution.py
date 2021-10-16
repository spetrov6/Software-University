class Profile:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if 5 <= len(value) <= 15:
            self.__username = value
            return
        raise ValueError("The username must be between 5 and 15 characters.")

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if self.__check_password_for_upper_letter(value) and self.__check_password_for_number(value) \
                and self.__check_password_length(value):
            self.__password = value
            return
        raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

    def __check_password_length(self, password):
        return len(password) >= 8

    def __check_password_for_upper_letter(self, password):
        return True if [x for x in password if x.isupper()] else False

    def __check_password_for_number(self, password):
        return True if [x for x in password if x.isdigit()] else False

    def __str__(self):
        return f'You have a profile with username: "{self.__username}" and password: {"*" * len(self.__password)}'
