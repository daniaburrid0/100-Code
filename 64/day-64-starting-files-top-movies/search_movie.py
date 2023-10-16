import requests
import tmdbsimple as tmdb

def get_list_of_movies(title) -> list:
    tmdb.API_KEY = ''
    
    search = tmdb.Search()
    response = search.movie(query=title)
    
    # List to store movies
    movie_list = []
    
    # Iterate over the search results
    for s in search.results:
        movie_data = {
            "title": s['title'],
            "id": s['id']
        }
        movie_list.append(movie_data)
    
    return movie_list

def finde_movie_by_id(id):
    tmdb.API_KEY = ''
    
    movie = tmdb.Movies(id)
    response = movie.info()
    
    # Dictionary to store specific movie details
    movie_details = {
        'Title': response['title'],
        'Image URL': f"https://image.tmdb.org/t/p/original{response['poster_path']}",
        'Year': response['release_date'].split('-')[0],
        'Description': response['overview']
    }
    
    return movie_details