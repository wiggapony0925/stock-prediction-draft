import yfinance as yahooFinance
import config

def stock_information():
    selected_stock = config.selected_stock
    if selected_stock is None:
        return "No stock selected"

    get_information = yahooFinance.Ticker(selected_stock)

    company_name = get_information.info.get('longName', 'N/A')
    website = get_information.info.get('website', 'N/A')
    industry = get_information.info.get('industry', 'N/A')
    description = get_information.info.get('longBusinessSummary', 'N/A')

# i added this into a dictionary in order to retrive it into the  main file

    info_dict = {
        "Company Name": company_name,
        "Industry": industry,
        "Website": website,
        "Description": description
    }

    return info_dict


if __name__ == "__main__":
    print(stock_information())
else:
    print("No stock selected")

