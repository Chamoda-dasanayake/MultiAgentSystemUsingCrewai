from crewai import Task
from agents.trader_agent import trader_agent

trade_decision = Task(
    description=(
        "use live market data and stock performance indicators for {stock} to make a strategic trading decision."
        "Asses key factors such as current price , daily change percentage, volume trends and recent momentrum."
        "based on your analysis, recommend whether to **Buy**, **sell**, or **hold** the stock."  
),
    expected_output=(
        "A clear ,confident trading recommendation (buy/sell/hold), supported by:\n."
        "-current stock price and daily change\n"
        "-daily price change and percentage\n"
        "-volume and market activity observations\n"
        "-justification for the trading action based on technical signals or risk-reward outlook"
    ),
    agent=trader_agent
)