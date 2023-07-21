class User:
    def __init__(self, name, age, email, mobile, password):
        self.name = name
        self.age = age
        self.email = email
        self.mobile = mobile
        self.password = password

    def to_dict(self):
        return {
            'name': self.name,
            'age': self.age,
            'email': self.email,
            'mobile': self.mobile,
            'password': self.password,
        }
