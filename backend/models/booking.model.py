class Booking:
    def __init__(self, user_id, event_id, theater_id, num_tickets):
        self.user_id = user_id
        self.event_id = event_id
        self.theater_id = theater_id
        self.num_tickets = num_tickets

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'event_id': self.event_id,
            'theater_id': self.theater_id,
            'num_tickets': self.num_tickets,
        }
