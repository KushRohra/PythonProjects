from bs4 import BeautifulSoup as bs
import requests
import json


def get_content_value(row_data):
    if row_data.find("li"):
        return [str(li.get_text(" ", strip=True)).replace("\xa0", " ") for li in row_data.find_all("li")]
    else:
        return str(row_data.get_text(" ", strip=True)).replace("\xa0", " ")


def get_movie_details(movie_url):
    r = requests.get(movie_url)
    soup = bs(r.content, features='lxml')

    movie_info = {}

    info_box = soup.find(class_="infobox vevent")
    info_rows = info_box.find_all("tr")
    for index, row in enumerate(info_rows):
        if index == 0:
            movie_info['title'] = row.find("th").get_text(" ", strip=True)
        elif index == 1:
            continue
        else:
            content_key = str(row.find("th").get_text(" ", strip=True))
            content_value = get_content_value(row.find("td"))
            movie_info.update({content_key: content_value})

    return movie_info


if __name__ == "__main__":
    r = requests.get("https://en.wikipedia.org/wiki/List_of_Walt_Disney_Pictures_films")
    soup = bs(r.content, features='lxml')

    base_path = "https://en.wikipedia.org/"
    movie_info_list = []
    movie_info_errors = []

    movies = soup.select(".wikitable.sortable i a")
    for index, movie in enumerate(movies):
        try:
            full_path = base_path + movie['href']
            movie_name = movie.get_text()
            movie_info_list.append(get_movie_details(full_path))
        except Exception as e:
            movie_info_errors.append({'movie_name': movie.get_text()})

    with open('movie_data.json', encoding='utf-8') as f:
        json.dump(movie_info_list, f, ensure_ascii=False, indent=2)

    with open('movie_info_error.json', encoding='utf-8') as f:
        json.dump(movie_info_errors, f, ensure_ascii=False, indent=2)
