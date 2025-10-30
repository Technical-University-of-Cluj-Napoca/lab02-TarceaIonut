import sys

import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    len = len(sys.argv)
    if len != 2:
        print("Usage: define.py word")
        sys.exit(0)
    word = sys.argv[1]
    url = f"https://dexonline.ro/definitie/{word}"
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        print("could not connect to dexonline")
        print(e)
    soup = BeautifulSoup(response.text, 'html.parser')

    try:
        print(soup.find("body", class_="search").
              find("div", class_="container container-narrow").
              find("main",class_="row").
              find("div", class_="col-md-12").
              find("div", class_="tab-content").
              find("div", id="tab_2").
              find_all("div",class_="tree-body")[1].
              find("ul", class_="meaningTree").
              find("span", class_="tree-def html").get_text(strip=True))
    except AttributeError as e:
        print("could not find the word in dexonline")
        sys.exit(0)


    pass

