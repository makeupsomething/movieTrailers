import webbrowser


class Movie:

    """This class creates a movie object"""

    def __init__(self,
                 movie_title,
                 movie_storyline,
                 poster_image,
                 trailer_youtube
                 ):
        """
        Must be initialized with the following
        movie title - the title of the movie
        storyline - a brief description of the plot
        image_url - a url to the movie's poster
        trailer url - a link to the trailer on youtube
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """When this function is called the default web browser will open and direct to the youtube_trailer_url"""
        webbrowser.open(self.trailer_youtube_url)
