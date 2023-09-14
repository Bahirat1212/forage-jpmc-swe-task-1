import json
import random
import urllib.request

# Server API URLs
QUERY = "http://localhost:8080/query?id={}"

# 500 server requests
N = 500


def getDataPoint(quote, prices):
    """Produce all the needed values to generate a data point."""
    stock = quote['stock']
    bid_price = float(quote['top_bid']['price'])
    ask_price = float(quote['top_ask']['price'])
    price = (bid_price + ask_price) / 2
    prices[stock] = price  # Add the price to the prices dictionary
    return stock, bid_price, ask_price, price


def getRatio(price_a, price_b):
    """Get the ratio of price_a and price_b, handling the case when price_b is zero."""
    if price_b == 0:
        return 0.0  # Return 0.0 when price_b is zero to avoid division by zero
    return price_a / price_b


# Main
if __name__ == "__main__":
    # Initialize prices dictionary
    prices = {"ABC": 0.0, "DEF": 0.0}

    # Query the price once every N seconds.
    for _ in range(N):
        quotes = json.loads(urllib.request.urlopen(QUERY.format(random.random())).read())

        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote, prices)
            print("Quoted %s at (bid:%s, ask:%s, price:%s)" % (stock, bid_price, ask_price, price))

        print("Ratio %s" % getRatio(prices["ABC"], prices["DEF"]))
