
class Portfolio(object):
    def __init__(self):
        self.stocks = []

    def buy(self, name, shares, price):
        self.stocks.append([name, shares, price])

    def cost(self):
        amt = 0.0
        for name, shares, price in self.stocks:
            amt += shares / price + 8
        return amt
