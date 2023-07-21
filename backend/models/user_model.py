# user_model.py
class User:
    def __init__(self, name, age, email, mobile, password, username):
        self.name = name
        self.age = age
        self.email = email
        self.mobile = mobile
        self.password = password
        self.username = username

    def to_dict(self):
        return {
            'name': self.name,
            'age': self.age,
            'email': self.email,
            'mobile': self.mobile,
            'password': self.password,
            'username': self.username,
        }
