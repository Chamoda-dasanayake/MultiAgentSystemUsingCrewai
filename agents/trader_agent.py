from crewai import Agent,LLM

llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    temperature=0.0
)

analyst_agent = Agent(
    role="Strategic Stock Trader",
    goal=("decide whether to buy , sell or hold a given stock based on live market data,"
          "price movement, and financial analysis with the available data."),
    backstory=("you are strategic stock trader with a strong background in financial analysis and market trends."
               "you rely on real time stock data, daily price movements, and financial indicators to make informed trading decisions."
                   "that optimize returns and reduce risk.")  ,
    llm=llm,
    tools=[],
    verbose=True
)