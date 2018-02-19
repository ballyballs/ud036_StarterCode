import media
import fresh_tomatoes

class movie():
   big_lebowski  = media.Movie("big Lebowski", "https://www.youtube.com/watch?v=cd-go0oBF4Y"
,"2hr20", "https://www.hygienic.org/wp-content/uploads/2017/08/big-lebowski.jpg", "1999", "Jeff Bridges", "Heather Graham")
   movies = [big_lebowski]

   fresh_tomatoes.open_movies_page(movies)    
