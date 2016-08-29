# -*- coding: utf-8 -*-

import webbrowser

class Video():
    """
    Parent Class
    """
    def __init__(self, title, runtime):
        """
        Create an instance of Video with tile and runtime proprties
        """
        self.title = title
        self.runtime = runtime

class Movie(Video):
    """
    Child class of Video
    """
    def __init__(self, movie_title, movie_duration,
                 movie_storyline, poster_image, trailer_youtube):
        """
        Create an instance of Movie with proprties:
        title, duration, storyline, poster, trailer
        """
        Video.__init__(self, movie_title, movie_duration)
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url= trailer_youtube

    def show_trailer(self):
        """
        Open youtube trailer
        """
        webbrowser.open(self.trailer_youtube_url)
