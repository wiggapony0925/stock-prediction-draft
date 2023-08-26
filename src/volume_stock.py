import requests
from bs4 import BeautifulSoup


def find_stocks():
    url = 'https://finance.yahoo.com/most-active/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    
    most_volume_stocks = []

    table = soup.find("table", {"class", "w(100%)"})
    if table:
        rows = table.find_all("tr")
        for row in rows[1:]:  # Skip the header row
            symbol_cell = row.find("td", {"aria-label": "Symbol"})
            if symbol_cell:
                symbol = symbol_cell.text
                most_volume_stocks.append(symbol)

    return most_volume_stocks

