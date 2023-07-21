class Admin:
    def __init__(self, admin_id, username, password):
        self.admin_id = admin_id
        self.username = username
        self.password = password

    def to_dict(self):
        return {
            'admin_id': self.admin_id,
            'username': self.username,
            'password': self.password,
        }
