from crewai import Task
from agents.analyst_agent import analyst_agent

get_stock_analysis = Task(
    description=(
    "Analyse the recent performance of the stock {stock}. "
    "Use the live_stock_data tool to retrieve the current price, "
    "percentage change, and market data. "
    "Provide a summary of how the stock is performing today."
),

    expected_output=(
        "A clear bullet-point summary including:\n"
        "- Current stock price\n"
        "- Daily price change and percentage\n"
        "- Volume and volatility insights\n"
        "- Immediate trends or observations"
    ),
    agent=analyst_agent
   
)
