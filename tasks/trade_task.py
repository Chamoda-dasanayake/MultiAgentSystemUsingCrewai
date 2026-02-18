from crewai import Task
from agents.trader_agent import trader_agent

trade_decision = Task(
    description=(
        "Based on the analyst report for the stock: {stock}, make a strategic trading decision. "
        "Evaluate the provided price data, daily change, volume trends, and momentum indicators. "
        "Using this analysis, recommend whether to BUY, SELL, or HOLD the stock."
    ),
    expected_output=(
        "A clear trading recommendation (BUY / SELL / HOLD) including:\n"
        "- Key signals from the analyst report\n"
        "- Interpretation of price and momentum\n"
        "- Risk–reward reasoning\n"
        "- Final action with justification"
    ),
    agent=trader_agent
    
)
