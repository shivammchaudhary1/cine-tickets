class Movie:
    def __init__(self, title, Vposter, Hposter, director, genre, language, duration, year, rating, desc):
        self.title = title
        self.Vposter = Vposter
        self.Hposter = Hposter
        self.director = director
        self.genre = genre
        self.language = language
        self.duration = duration
        self.year = year
        self.rating = rating
        self.desc = desc

    def to_dict(self):
        return {
            'title': self.title,
            'Vposter': self.Vposter,
            'Hposter': self.Hposter,
            'director': self.director,
            'genre': self.genre,
            'language': self.language,
            'duration': self.duration,
            'year': self.year,
            'rating': self.rating,
            'desc': self.desc,
        }
