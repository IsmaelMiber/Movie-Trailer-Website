#This for include or import webbrowser library to use it in open a link in webbrowser window
import webbrowser

#This is class called Movie
class Movie():

#This is initialize function to initialize the parameters of __init__ function by pass arguments from instance of the class
    def __init__(self, movieTitle, moviePoster, movieTrailer):
        self.title = movieTitle
        self.poster_image_url = moviePoster
        self.trailer_youtube_url = movieTrailer   
    
