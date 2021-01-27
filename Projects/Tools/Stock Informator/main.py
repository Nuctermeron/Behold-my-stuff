import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = 'GEILXLI7FNTMYY14'  # alphavantage
NEWS_API_KEY = 'd181252ce6b642a39f43469e5b0b0f12'  # newsapi
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_PARAMETERS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,

}
NEWS_PARAMETERES = {
    "apiKey": NEWS_API_KEY,
    "qInTitle": COMPANY_NAME,

}

response = requests.get(STOCK_ENDPOINT, params=STOCK_PARAMETERS)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yday_data = data_list[0]
d_before_yday = data_list[1]

yday_dyday_dif = abs(float(yday_data["4. close"]) - float(d_before_yday["4. close"]))
yday_dyday_prcnt = round((yday_dyday_dif / float(yday_data["4. close"])) * 100)

if yday_dyday_prcnt > 0:
    inc_decr = "△"
else:
    inc_decr = "▽"

news_response = requests.get(NEWS_ENDPOINT, params=NEWS_PARAMETERES)
articles = news_response.json()["articles"]
articles_slice = articles[:5]
articles_list = [
    f"{STOCK} {inc_decr} {yday_dyday_prcnt}% Headline: {article['title']}. \n Content: {article['description']}\n" for
    article in
    articles_slice]

for n in articles_list:
    print(n)
