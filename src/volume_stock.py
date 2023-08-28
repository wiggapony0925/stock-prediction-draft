import requests
from bs4 import BeautifulSoup


def find_stocks():
    url = 'https://finance.yahoo.com/most-active/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    most_volume_stocks = []

    # Find all table rows with the specific class
    rows = soup.find_all("tr", class_="simpTblRow")

    for row in rows:
        symbol_cell = row.find("a", {"data-test": "quoteLink"})
        if symbol_cell:
            symbol = symbol_cell.text.strip()
            most_volume_stocks.append(symbol)

    return most_volume_stocks


# Test the function
print(find_stocks())
