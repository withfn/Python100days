from bs4 import BeautifulSoup
import requests

movies = []
response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")
movie_names = soup.find_all(name="h3", class_="title")
for movie in movie_names:
    movies.insert(0,movie.getText())

with open("movie_list.txt", mode='a', encoding='utf-8') as file:
    file.write('\n'.join(movies))