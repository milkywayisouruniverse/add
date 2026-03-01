class Movie:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating

    def display_details(self):
        print("Movie:", self.name)
        print("Rating:", self.rating, "/ 5")


# Example
movie = Movie("Inception", 4.8)
movie.display_details()