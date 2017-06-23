import fresh_tomatoes
import media

logan = media.Movie("Logan", 
                    "https://upload.wikimedia.org/wikipedia/en/3/37/Logan_2017_poster.jpg",
                    "https://youtu.be/Div0iP65aZo"
                    )

rangers = media.Movie("Power Rangers",
                      "https://upload.wikimedia.org/wikipedia/en/7/78/Power_Rangers_%282017_Official_Theatrical_Poster%29.png",
                      "https://youtu.be/Q-C4qqsgs8w"
                      )

kong = media.Movie("Kong: Skull Island",
                   "https://upload.wikimedia.org/wikipedia/en/3/34/Kong_Skull_Island_poster.jpg",
                   "https://youtu.be/AP0-9FBs2Rs"
                   )

johnWick = media.Movie("John Wick: Chapter 2",
                       "https://upload.wikimedia.org/wikipedia/en/3/31/John_Wick_Chapter_Two.png",
                       "https://youtu.be/nMqETeQrgqU"
                       )

tarzan = media.Movie("The Legend of Tarzan",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/e/e5/The_Legend_of_Tarzan_poster.jpg/220px-The_Legend_of_Tarzan_poster.jpg",
                     "https://youtu.be/qDzP3Dn4irc"
                     )

movies = [logan, rangers, kong, johnWick, tarzan]

fresh_tomatoes.open_movies_page(movies)
