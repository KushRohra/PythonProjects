import requests
from bs4 import BeautifulSoup
import pandas


def main():
    properties = []

    # page_no = int(soup.find_all("a", {"class": "Page"})[-1].text) * 10
    # comes out to be 30

    max_value_to_count = 30
    skip_value = 10

    base_url = "http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s="
    for page in range(0, max_value_to_count, skip_value):
        url = base_url + str(page) + ".html"

        r = requests.get(url, headers={
            'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})

        if r.status_code != 200:
            continue

        c = r.content
        soup = BeautifulSoup(c, "html.parser")

        allEle = soup.findAll("div", {"class": "propertyRow"})
        for ele in allEle:
            try:
                price = ele.find("h4", {"class": "propPrice"}).text.replace("\n", "").replace(" ", "")
            except Exception as e:
                price = ""

            try:
                fullAddress = ele.find_all("span", {"class": "propAddressCollapse"})
                address = ""
                for item in fullAddress:
                    address += item.text
            except Exception as e:
                address = ""

            try:
                beds = ele.find("span", {"class": "infoBed"}).find("b").text
            except Exception as e:
                beds = ""

            try:
                fullBaths = ele.find("span", {"class": "infoValueFullBath"}).find("b").text
            except Exception as e:
                fullBaths = ""

            try:
                halfBaths = ele.find("span", {"class": "infoValueHalfBath"}).find("b").text
            except Exception as e:
                halfBaths = ""

            try:
                area = ele.find("span", {"class": "infoSqFt"}).find("b").text
            except Exception as e:
                area = ""

            lot_size = ""
            try:
                allColumnGroup = ele.find_all("div", {"class": "columnGroup"})
                for columnGroup in allColumnGroup:
                    allFeatureGroup = columnGroup.find_all("span", {"class": "featureGroup"})
                    allFeatureName = columnGroup.find_all("span", {"class": "featureName"})
                    for feature_group, feature_name in zip(allFeatureGroup, allFeatureName):
                        if "Lot Size" in feature_group.text:
                            lot_size = feature_name.text.replace(",", "")
                            break
            except Exception as e:
                lot_size = ""

            dict = {}

            dict["Address"] = address
            dict["Price"] = price
            dict["Beds"] = beds
            dict["fullBaths"] = fullBaths
            dict["halfBaths"] = halfBaths
            dict["Area"] = area
            dict["LotSize"] = lot_size

            properties.append(dict)

    df = pandas.DataFrame(properties)
    df.to_csv("Properties.csv")


if __name__ == "__main__":
    main()
