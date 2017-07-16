import webbrowser # import the webrowser which is used to open the the trailer


class Movie(): # used to define the class MOVIE
    """bang bang bangati bang, bang bang bandati bang"""
    VALID_RATINGS = ["1", "2", "3", "4"]
    
    def __init__(self, movie_title, movie_storyline,
                 movie_poster, youtube_trailer):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster = movie_poster
        self.trailer = youtube_trailer
        
    def show_trailer(self): # used to open the trailer
        webbrowser.open(self.trailer)
        
