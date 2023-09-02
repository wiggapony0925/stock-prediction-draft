import yfinance as yahooFinance
import config


def stock_information():
    selected_stock = config.selected_stock
    if selected_stock is None:
        return "No stock selected"

    get_information = yahooFinance.Ticker(selected_stock)


    print(get_information.info)
    return get_information


if __name__ == "__main__":
    print(stock_information())
else:
    print("No stock selected")
