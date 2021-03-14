from bs4 import BeautifulSoup as bs
import requests
import json
import re
from datetime import datetime
import urllib


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


'''def word_to_value(word):
    value_dict = {"thousand": 1000, "million": 1000000, "billion": 1000000000}
    return value_dict[word]


def parse_word_syntax(string, number, amounts):
    value_string = re.search(number, string).group()
    value = float(value_string.replace(",", ""))
    word = re.search(amounts, string, flags=re.I).group().lower()
    word_value = word_to_value(word)
    return value * word_value


def parse_value_syntax(string, number):
    value_string = re.search(number, string).group()
    value = float(value_string.replace(",", ""))
    return value


def money_conversion(money):
    if money == "NA":
        return None
    if type(money) is list:
        money = money[0]
    amounts = r"thousand|million|billion"
    number = r"\d+(,\d{3})*\.*\d*"

    word_re = rf"\${number}(-|\sto\s|-)?({number})?\s({amounts})"
    value_re = rf"\${number}"

    word_syntax = re.search(word_re, money, flags=re.I)
    value_syntax = re.search(value_re, money)

    if word_syntax:
        return parse_word_syntax(word_syntax.group(), number, amounts)
    elif value_syntax:
        return parse_value_syntax(value_syntax.group(), number)
    else:
        return None


def convert_budget_and_box_office_regex():
    with open('movie_data.json', 'r', encoding='utf-8') as f:
        movie_list = json.load(f)

    for movie in movie_list:
        movie['Box office'] = money_conversion(movie.get("Box office", "NA"))
        movie['Budget'] = money_conversion(movie.get('Budget', "NA"))

    with open('movie_data.json', 'w', encoding='utf-8') as f:
        json.dump(movie_list, f, ensure_ascii=False, indent=2)'''


def get_word_string_value(word):
    if word == "thousand":
        return 1000
    if word == "million":
        return 1000000
    if word == "billion":
        return 1000000000
    return None


def clean_amount_string(string):
    i = 0
    amount_string = ""
    while i < len(string):
        if string[i] == "–":
            break
        amount_string += string[i]
        i += 1
    return amount_string


def convert_to_money(string):
    if string == "NA":
        return None
    i = 0
    if type(string) is not str:
        return
    while i < len(string):
        if string[i] == "$":
            i += 1
            break
        i += 1
    amount_string = ""
    word_string = ""
    while i < len(string) and string[i] != ' ':
        amount_string += string[i]
        i += 1
    i += 1
    while i < len(string) and string[i] != ' ':
        word_string += string[i]
        i += 1
    amount_value = 0
    try:
        amount_value = float(clean_amount_string(amount_string).replace(",", ""))
    except Exception as e:
        pass
    word_value = get_word_string_value(word_string)
    if word_value is None:
        return amount_value
    else:
        return amount_value * word_value


def convert_budget_and_box_office():
    with open('movie_data.json', 'r', encoding='utf-8') as f:
        movie_list = json.load(f)

    for movie in movie_list:
        box_office_string = movie.get("Box office", "NA")
        budget_string = movie.get("Budget", "NA")
        try:
            del movie['Box office']
        except Exception as e:
            pass
        try:
            del movie['Budget']
        except Exception as e:
            pass
        movie.update({"Box office": convert_to_money(box_office_string)})
        movie.update({"Budget": convert_to_money(budget_string)})

    with open('movie_data.json', 'w', encoding='utf-8') as f:
        json.dump(movie_list, f, ensure_ascii=False, indent=2)


def get_date(date_string):
    if date_string == "NA":
        return None
    date_string = date_string.split('(')[0].strip()
    formats = ['%B %d, %Y', '%d %B %Y']
    for format in formats:
        try:
            return datetime.strptime(date_string, format)
        except Exception as e:
            return None


def convert_date():
    with open('movie_data.json', 'r', encoding='utf-8') as f:
        movie_list = json.load(f)

    for movie in movie_list:
        release_date_string = movie.get('Release date', 'NA')
        if type(release_date_string) is list:
            release_date_string = release_date_string[0]
        try:
            del movie['Release date']
        except Exception as e:
            pass
        release_date = str(get_date(release_date_string))
        movie.update({'Release date': release_date.split(' ')[0]})

    with open('movie_data.json', 'w', encoding='utf-8') as f:
        json.dump(movie_list, f, ensure_ascii=False, indent=2)


def clean_data():
    # Cleanup references => remove [1], [2]
    # Split up the long strings

    # Convert running time into integers
    minute_to_integer()

    # Convert budget and box office to numbers
        # convert_budget_and_box_office_regex()
    convert_budget_and_box_office()

    # Convert dates into datetime objects
    convert_date()


def get_ratings_from_api(title):
    url = "http://www.omdbapi.com/?"
    parameters = {'t': title, "apikey": 'a42a5b44'}
    params_encoded = urllib.parse.urlencode(parameters)
    full_url = url + params_encoded
    r = requests.get(full_url)
    if r.status_code != 200:
        return None
    return r.json()


def get_rotten_tomato_score(data):
    ratings = data.get("Ratings", None)
    if ratings is not None:
        for rating in ratings:
            if rating['Source'] == "Rotten Tomatoes":
                return rating['Value']
    return None


def get_omdb_info():
    with open('movie_data.json', 'r', encoding='utf-8') as f:
        movie_list = json.load(f)

    for movie in movie_list:
        title = movie['title']
        data = get_ratings_from_api(title)
        if data is not None:
            rating = get_rotten_tomato_score(data)
        movie.update({'imdb': data.get('imdbRating', None)})
        movie.update({'metascore': data.get('Metascore', None)})
        movie.update({'Rotten Tomatoes': rating})

    with open('movie_data.json', 'w', encoding='utf-8') as f:
        json.dump(movie_list, f, ensure_ascii=False, indent=2)


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


def main():
    r = requests.get("https://en.wikipedia.org/wiki/List_of_Walt_Disney_Pictures_films")
    soup = bs(r.content, features='lxml')

    base_path = "https://en.wikipedia.org/"
    movie_info_list = []

    movies = soup.select(".wikitable.sortable i a")
    for index, movie in enumerate(movies):
        print(index)
        try:
            full_path = base_path + movie['href']
            movie_info_list.append(get_movie_details(full_path))
        except Exception as e:
            continue

    with open('movie_data.json', 'w', encoding='utf-8') as f:
        json.dump(movie_info_list, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    # main()
    # clean_data()
    get_omdb_info()
