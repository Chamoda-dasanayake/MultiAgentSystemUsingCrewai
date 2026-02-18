import yfinance as yf
from crewai.tools import tool

@tool("Live stock information Tool")
def get_stock_price(stock_symbol: str) -> str:
    """
    Get the current stock price for a given ticker symbol.

    Args:
        ticker (str): The stock ticker symbol (e.g., "AAPL" for Apple Inc.).

    Returns:
        float: The current stock price.
    """
    try:
        stock = yf.Ticker(stock_symbol)
        # Get historical data (last 1 day) as a fallback method
        hist = stock.history(period="1d")
        
        if hist.empty:
            return f"Unable to fetch data for {stock_symbol}"
        
        current_price = hist['Close'].iloc[-1]
        currency = "USD"
        
        # Try to get additional info
        try:
            info = stock.info
            change = info.get("regularmarketchange")
            change_percent = info.get("regularmarketchangepct", 0)
        except:
            change = None
            change_percent = 0
        
        if current_price is not None:
            return (
                f"Stock:{stock_symbol.upper()}\n"
                f"Price:{round(current_price, 2)} {currency}\n"
                f"Change:{change} ({round(change_percent, 2) if change_percent else 0}%)"
            )
        
        return f"Unable to fetch price for {stock_symbol}"
    except Exception as e:
        return f"Error fetching data for {stock_symbol}: {str(e)}"

# print(get_stock_price("AAPL"))  