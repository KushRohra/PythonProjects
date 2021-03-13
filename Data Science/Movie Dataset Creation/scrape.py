from bs4 import BeautifulSoup as bs
import requests
import json


def get_content_value(row_data):
    if row_data.find("li"):
        return [str(li.get_text(" ", strip=True)).replace("\xa0", " ") for li in row_data.find_all("li")]
    elif row_data.find("br"):
        return [text for text in row_data.stripped_strings]
    else:
        return str(row_data.get_text(" ", strip=True)).replace("\xa0", " ")


def clean_tags(soup):
    # removes references and dates formatted in brackets
    for tag in soup.find_all(["sup", "span"]):
        tag.decompose()


def get_movie_details(movie_url):
    r = requests.get(movie_url)
    soup = bs(r.content, features='lxml')

    clean_tags(soup)

    movie_info = {}

    info_box = soup.find(class_="infobox vevent")
    info_rows = info_box.find_all("tr")
    for index, row in enumerate(info_rows):
        if index == 0:
            movie_info['title'] = row.find("th").get_text(" ", strip=True)
        else:
            header = row.find('th')
            if header:
                content_key = str(row.find("th").get_text(" ", strip=True))
                content_value = get_content_value(row.find("td"))
                movie_info.update({content_key: content_value})

    return movie_info


def minute_to_integer():
    with open('movie_data.json', 'r', encoding='utf-8') as f:
        movie_list = json.load(f)

    for movie in movie_list:
        time = movie.get('Running time', 'NA')
        if type(time) is list:
            time = time[0]
        time = time.split(' ')[0]
        try:
            del movie['Running time']
        except Exception as e:
            pass
        movie.update({'Running time (int)': time})

    with open('movie_data.json', 'w', encoding='utf-8') as f:
        json.dump(movie_list, f, ensure_ascii=False, indent=2)


def clean_data():
    # Cleanup references => remove [1], [2]
    # Split up the long strings

    # Convert running time into integers
    minute_to_integer()

    # Convert dates into datetime objects
    # Convert budget and box office to numbers
    pass


def main():
    r = requests.get("https://en.wikipedia.org/wiki/List_of_Walt_Disney_Pictures_films")
    soup = bs(r.content, features='lxml')

    base_path = "https://en.wikipedia.org/"
    movie_info_list = []

    movies = soup.select(".wikitable.sortable i a")
    for index, movie in enumerate(movies):
        if index == 41:
            break
        if index % 10 == 0:
            print(index)
        try:
            full_path = base_path + movie['href']
            movie_name = movie.get_text()
            movie_info_list.append(get_movie_details(full_path))
        except Exception as e:
            continue

    with open('movie_data.json', 'w', encoding='utf-8') as f:
        json.dump(movie_info_list, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    # main()
    clean_data()
