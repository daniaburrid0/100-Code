import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
def main() -> None:
    response = requests.get(URL)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    movie_tags = soup.find_all(name="h3", class_="title")
    movie_titles = [movie.getText() for movie in movie_tags]
    movies = movie_titles[::-1]

    with open("movies.txt", encoding="UTF-8" ,mode="w") as file:
        for movie in movies:
            file.write(f"{movie}\n")

    print("Done")

if __name__ == '__main__':
    main()