from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

archive = response.text

soup = BeautifulSoup(archive, 'html.parser')

movies = soup.find_all(name="h3", class_="title")

movies_txt = 'movies.txt'

movies_list = []

for movie in movies:
    movie_name = movie.getText()
    movies_list.append(movie_name)

movies_list.reverse()

with open("movies.txt", "w") as file:
    for item in movies_list:
        file.write('%s\n' % item)