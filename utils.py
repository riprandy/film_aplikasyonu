import requests

class UtilFuncs:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://www.omdbapi.com/"

    def get_movie_info_by_name(self, title, year=None):
        params = {
            "s": title,
            "apikey": self.api_key,
            "r": "json"
        }
        response = requests.get(self.base_url, params=params)
        data = response.json()

        if data.get("Response") == "False":
            print(f"Error: {data.get('Error')}")
            return None

        search_results = data.get("Search", [])
        matched_movie = None

        if year:
            for movie in search_results:
                if movie.get("Year") == str(year):
                    matched_movie = movie
                    break
        else:
            matched_movie = search_results[0] if search_results else None

        if not matched_movie:
            print("No matching movie found with the specified year.")
            return None

        return matched_movie

    def get_movie_info_by_id(self, imdb_id):
        params = {
            "i": imdb_id,
            "apikey": self.api_key,
            "r": "json"
        }
        response = requests.get(self.base_url, params=params)
        data = response.json()

        if data.get("Response") == "False":
            print(f"Error fetching details: {data.get('Error')}")
            return None

        return data

    def get_movie_scores(self, title, year=None):
        movie = self.get_movie_info_by_name(title, year)
        if not movie:
            return None

        imdb_id = movie.get("imdbID")
        if not imdb_id:
            print("IMDb ID not found for the matched movie.")
            return None

        details = self.get_movie_info_by_id(imdb_id)
        if not details:
            return None

        imdb_rating = details.get("imdbRating", "Bilinmiyor")
        rt_score = None
        for rating in details.get("Ratings", []):
            if rating.get("Source") == "Rotten Tomatoes":
                rt_score = rating.get("Value")
                break
        if rt_score is None:
            rt_score = "Bilinmiyor"

        return {
            "imdb_rating": imdb_rating,
            "rotten_tomatoes": rt_score
        }

    def get_movie_genre(self, title, year=None):
        movie = self.get_movie_info_by_name(title, year)
        if not movie:
            return None

        imdb_id = movie.get("imdbID")
        if not imdb_id:
            print("IMDb ID not found for the matched movie.")
            return None

        details = self.get_movie_info_by_id(imdb_id)
        if not details:
            return None

        genre = details.get("Genre", "Bilinmiyor")
        return genre
