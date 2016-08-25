import webbrowser

class Video():
    def __init__(self, title, runtime):
        #print("Video Constructor Called")
        self.title = title
        self.runtime = runtime

class Movie(Video):
    def __init__(self, movie_title, movie_duration,
                 movie_storyline, poster_image, trailer_youtube):
        #print("Movie Constructor Called")
        Video.__init__(self, movie_title, movie_duration)
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url= trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
