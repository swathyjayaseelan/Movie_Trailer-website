class Movie():
    def __init__(
        self, movie_title, movie_storyline, movie_image, movie_trailer):
        ''' The constructor method which is called when instances are instantiated
        will take as inputs the title of the movie, story line, poster image
        and youtube trailer which are passed as arguments when the instances
        are created and sets the value of the current (this) object'''
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_image
        self.trailer_youtube_url = movie_trailer

