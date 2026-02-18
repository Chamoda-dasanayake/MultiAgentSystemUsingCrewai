from crewai import Task
from agents.analyst_agent import analyst_agent

get_stock_analysis = Task(
    description=("analyse the recent performance of the stock:{stock}. use the live stock information tool to retrieve"
    "current price , percentage change, trading volume, and other market data. provide a summaryof how the stock"
    "is performing today and highlight any key observations from the data."
),
expected_output=(
"A clear , bullet-pointyed summary of:\n."
"-current stock price\n"
"-daily price change and percentage\n"
"-volume and volatility\n"
"-any immediate trends or observations"
),
agent=analyst_agent
)