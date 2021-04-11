import requests
from bs4 import BeautifulSoup

base_url = "https://aviation-safety.net/database/dblist.php"


def get_info(year):
    url = base_url #+str(year)
    print(url)
    params = {"Year": str(year) }
    req = requests.post(url, params)
    print(req)
    soup = BeautifulSoup(req.content, "html.parser")
    print(soup)

def main():
    get_info(2021)


if __name__ == '__main__':
    main()
