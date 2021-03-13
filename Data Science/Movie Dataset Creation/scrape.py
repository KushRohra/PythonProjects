from bs4 import BeautifulSoup as bs
import requests

url = "https://en.wikipedia.org/wiki/Toy_Story_3"
r = requests.get(url)
soup = bs(r.content, features='lxml')


def get_content_value(row_data):
    if row_data.find("li"):
        return [str(li.get_text(" ", strip=True)).replace("\xa0", " ") for li in row_data.find_all("li")]
    else:
        return str(row.find("td").get_text(" ", strip=True)).replace("\xa0", " ")


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

print(movie_info)
