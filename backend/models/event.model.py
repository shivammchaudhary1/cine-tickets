class Event:
    def __init__(self, name, date, location, description):
        self.name = name
        self.date = date
        self.location = location
        self.description = description

    def to_dict(self):
        return {
            'name': self.name,
            'date': self.date,
            'location': self.location,
            'description': self.description,
        }
