import media
import fresh_tomatoes

# Toy Story Movie: movie title, storyline, poster image and youtube trailer
toy_story = media.Movie("Toy Story",
                        "About toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",  # noqa
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

# Star Wars Episode IV Movie: movie title, storyline, poster image and youtube trailer
star_wars = media.Movie("Star Wars",
                        "Awesome space adventures",
                        "https://upload.wikimedia.org/wikipedia/en/8/87/StarWarsMoviePoster1977.jpg",  # noqa
                        "https://www.youtube.com/watch?v=1g3_CFmnU7k")

# Muppets Christmas Carol Movie: movie title, storyline, poster image and youtube trailer
muppets_christmas = media.Movie("Muppets Christmas Carol",
                                "A christmas classic",
                                "https://upload.wikimedia.org/wikipedia/en/9/95/Muppet_christmas_carol.jpg",  # noqa
                                "https://www.youtube.com/watch?v=dhpu2tq9GG4")

movies = [toy_story, star_wars, muppets_christmas]

fresh_tomatoes.open_movies_page(movies)
