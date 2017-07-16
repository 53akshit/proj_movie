import fresh_tomatoes
import media  
# imports the file media and fresh_tomatoes

dumb_and_dumber = media.Movie(
                              "Dumb and Dumber",
                              "love can be found anywhere and anytime",
                              "https://upload.wikimedia.org/wikipedia/en/thumb/6/64/Dumbanddumber.jpg/220px-Dumbanddumber.jpg",
                              "https://www.youtube.com/watch?v=l13yPhimE3o")                             
wolf_of_wall_street = media.Movie(
                                  "The Wolf of WALL STREET",
                                  "love can be found anywhere and anytime",
                                  "https://upload.wikimedia.org/wikipedia/en/1/1f/WallStreet2013poster.jpg", 
                                  "https://www.youtube.com/watch?v=pabEtIERlic")
lunchbox = media.Movie(
                       "Lunchbox",
                       "love can be found anywhere and anytime",
                       "https://upload.wikimedia.org/wikipedia/en/thumb/8/81/The_Lunchbox_poster.jpg/220px-The_Lunchbox_poster.jpg",
                       "https://www.youtube.com/watch?v=sK3R0rvnlPs")
dark_knight = media.Movie(
                          "Dark Knight",
                          "love can be found anywhere and anytime",
                          "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
                          "https://www.youtube.com/watch?v=EXeTwQWrcwY")
dazed_and_confused = media.Movie(
                                "dazed and confused",
                                "love can be found anywhere and anytime",  
                                "https://upload.wikimedia.org/wikipedia/en/a/af/Dazed_and_Confused_%281993%29_poster.jpg", 
                                "https://www.youtube.com/watch?v=3aQuvPlcB-8")
high_fidelity = media.Movie(
                            "High Fidelity", 
                            "love can be found anywhere and anytime", 
                            "https://upload.wikimedia.org/wikipedia/en/thumb/8/8f/High_Fidelity_poster.jpg/220px-High_Fidelity_poster.jpg",
                            "https://www.youtube.com/watch?v=6P4dXJ_Tvns")
dumb_and_dumber = media.Movie( 
                              "Dumb and Dumber",
                              "love can be found anywhere and anytime",
                              "https://upload.wikimedia.org/wikipedia/en/thumb/6/64/Dumbanddumber.jpg/220px-Dumbanddumber.jpg", 
                              "https://www.youtube.com/watch?v=l13yPhimE3o")
ZNMD = media.Movie(
                   "Zindagi na Milegi Dobara", 
                   "a movie of a boy and his toys which come to life",
                   "https://upload.wikimedia.org/wikipedia/en/thumb/3/3d/Zindaginamilegidobara.jpg/220px-Zindaginamilegidobara.jpg", 
                   "https://www.youtube.com/watch?v=FJrpcDgC3zU")

# print(toy_story.storyline)
# print(lunchbox.storyline)

# lunchbox.show_trailer()

Movies = [
          dumb_and_dumber,
          lunchbox, dark_knight,
          dazed_and_confused,
          high_fidelity,
          ZNMD, 
          wolf_of_wall_street] # stores the name in array
fresh_tomatoes.open_movies_page(Movies) # used to open the page in the browser

# print(media.Movie.VALID_RATINGS)
# print(media.Movie.__doc__)
