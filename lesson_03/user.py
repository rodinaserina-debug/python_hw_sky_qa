class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def say_name(self):
        return f"Имя: {self.first_name}"

    def say_surname(self):
        return f"Фамилия: {self.last_name}"

    def say_name_surname(self):
        return f"Мои фамилия и имя: {self.last_name} {self.first_name}"