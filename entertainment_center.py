import fresh_tomatoes
import media

"""
Movie Attributes:
    attr1: title
    attr2: runtime
    attr3: storyline
    attr4: poster image
    attr5: trailer_youtube
"""

# Released on June 22, 2016
movie_1 = media.Movie("Independence Day: Resurgence",
                      "2h 0m",
                      "We always knew they were coming back.",
                      "https://image.tmdb.org/t/p/w300_and_h450_bestv2/9KQX22BeFzuNM66pBA6JbiaJ7Mi.jpg",
                      "https://youtu.be/LbduDRH2m2M")

# Relased on June 9, 2016
movie_2 = media.Movie("Warcraft",
                      "2h 3m",
                      "The peaceful realm of Azeroth stands on the brink of war"
                      " as its civilization faces a fearsome race of invaders:"
                      " orc warriors fleeing their dying home to colonize another.",
                      "https://image.tmdb.org/t/p/w300_and_h450_bestv2/ckrTPz6FZ35L5ybjqvkLWzzSLO7.jpg",
                      "https://youtu.be/2Rxoz13Bthc")

# Relased on March 24, 2016
movie_3 = media.Movie("Batman v Superman: Dawn of Justice",
                      "2h 31m",
                      "Fearing the actions of a god-like Super Hero left unchecked,"
                      " Gotham City’s own formidable, forceful vigilante takes on"
                      " Metropolis’s most revered, modern-day savior, while the world"
                      " wrestles with what sort of hero it really needs.",
                      "https://image.tmdb.org/t/p/w300_and_h450_bestv2/cGOPbv9wA5gEejkUN892JrveARt.jpg",
                      "https://youtu.be/0WWzgGyAH6Y")

# Releasd on March 4, 2016
movie_4 = media.Movie("Zootopia",
                      "1h 48m",
                      "Determined to prove herself, Officer Judy Hopps,"
                      " the first bunny on Zootopia's police force, jumps at"
                      " the chance to crack her first case - even if it means"
                      " partnering with scam-artist fox Nick Wilde to solve the mystery.",
                      "https://image.tmdb.org/t/p/w300_and_h450_bestv2/sM33SANp9z6rXW8Itn7NnG1GOEs.jpg",
                      "https://youtu.be/bY73vFGhSVk")

movies = [movie_1, movie_2, movie_3, movie_4]

fresh_tomatoes.open_movies_page(movies)
                        
