import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "About toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

star_wars = media.Movie("Star Wars",
                        "Awesome space adventures",
                        "https://upload.wikimedia.org/wikipedia/en/8/87/StarWarsMoviePoster1977.jpg",
                        "https://www.youtube.com/watch?v=1g3_CFmnU7k")

muppets_christmas = media.Movie("Muppets Christmas Carole",
                        "A christmas classic",
                        "https://upload.wikimedia.org/wikipedia/en/9/95/Muppet_christmas_carol.jpg",
                        "https://www.youtube.com/watch?v=dhpu2tq9GG4")

movies = [toy_story, star_wars, muppets_christmas]

fresh_tomatoes.open_movies_page(movies)