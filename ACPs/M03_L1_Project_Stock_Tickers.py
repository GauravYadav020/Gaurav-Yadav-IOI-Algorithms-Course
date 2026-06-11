# Module 3 Lesson 1: After-Class Project
# Project Name: Stock Market Market-Ticker Aggregator Array Matrix

class MarketTickerMatrix:
    def __init__(self):
        self.ticker_history = [] # Stores tuples: (Symbol, Timestamp, TradingPrice)

    def append_ticker_tick(self, symbol, timestamp, execution_price):
        self.ticker_history.append((symbol, timestamp, execution_price))

    def filter_isolated_asset(self, target_symbol):
        return [tick for tick in self.ticker_history if tick[0] == target_symbol]

if __name__ == "__main__":
    exchange = MarketTickerMatrix()
    exchange.append_ticker_tick("AAPL", "10:00:00", 175.20)
    exchange.append_ticker_tick("NVDA", "10:00:01", 895.50)
    exchange.append_ticker_tick("AAPL", "10:00:02", 175.45)
    print(f"Filtered Target Assets Data Stream: {exchange.filter_isolated_asset('AAPL')}")