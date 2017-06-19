import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story 3",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=ZZv1vki4ou4")

#print(toy_story.storyline)


avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

#print(avatar.storyline)

arrival = media.Movie("Arrival",
                      "A linguistics professor takes a chance that could threaten her life and quite possibly all of mankind",
                      "https://upload.wikimedia.org/wikipedia/en/d/df/Arrival%2C_Movie_Poster.jpg",
                      "https://www.youtube.com/watch?v=tFMo3UJ4B4g")

martian = media.Movie("The Martian",
                      "When astronauts blast off from the planet Mars, they leave behind Mark Watney (Matt Damon), presumed dead after a fierce storm. With only a meager amount of supplies, the stranded visitor must utilize his wits and spirit to find a way to survive on the hostile planet.",
                      "https://upload.wikimedia.org/wikipedia/en/c/cd/The_Martian_film_poster.jpg",
                      "https://www.youtube.com/watch?v=ej3ioOneTy8")
thor = media.Movie("Thor 3: Ragnarok ",
                   "Imprisoned on the other side of the universe, the mighty Thor finds himself in a deadly gladiatorial contest that pits him against the Hulk, his former ally and fellow Avenger. Thor's quest for survival leads him in a race against time to prevent the all-powerful Hela from destroying his home world and the Asgardian civilization.",
                   "https://upload.wikimedia.org/wikipedia/en/f/fc/Thor_poster.jpg",
                   "https://www.youtube.com/watch?v=OctRQoCodVw")

justice_league = media.Movie("Justice League",
                             "Fueled by his restored faith in humanity and inspired by Superman's (Henry Cavill) selfless act, Bruce Wayne (Ben Affleck) enlists newfound ally Diana Prince to face an even greater threat. Together, Batman and Wonder Woman work quickly to recruit a team to stand against this newly awakened enemy. ",
                             "https://upload.wikimedia.org/wikipedia/en/3/31/Justice_League_film_poster.jpg",
                             "https://www.youtube.com/watch?v=3cxixDgHUYw")


movies = [toy_story, avatar, arrival, martian, thor, justice_league]
fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
#print(media.Movie.__doc__)






