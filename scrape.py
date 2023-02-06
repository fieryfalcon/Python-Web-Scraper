from urllib import response
import requests
from bs4 import BeautifulSoup as bs
import pymysql.cursors
stcode = ""


def scrape(id):
    r = requests.get("https://cameochemicals.noaa.gov/chemical/" + str(id))
    stcode = r.status_code
    if stcode == 404:

        return False

    else:

        soup = bs(r.content, 'html.parser')

        chem_name = soup.find(class_="datasheet")
        chemical_name = chem_name.string

        cas_number_ul = soup.find(class_="no-bullet3")
        cas_num = cas_number_ul.findChildren("li", recursive=False)
        cas_number = cas_num[0].get_text()

        chemdict = {
            "name": chemical_name,
            "cas_number": cas_number,
        }

        return chemdict, True


def search(str):
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='QWDrt@12345',
                                 database='web_scrapping',
                                 cursorclass=pymysql.cursors.DictCursor)

    with connection.cursor() as cursor:
        # Read a single record

        cursor.execute(
            "SELECT * FROM `chemical` WHERE `cas_number`=%s ;", (str,))
        result = cursor.fetchone()

        print(result)
