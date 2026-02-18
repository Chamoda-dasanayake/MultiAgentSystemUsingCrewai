from crewai import Agent,LLM

from tools.stock_research_tool import get_stock_price 

llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    temperature=0.0
)

analyst_agent = Agent(
    role="Financial Market Analyst",
    goal=("perform in-depth evaluations of publicly traded stocks using real-time data,"
          "identifying trends, performance insights, and potential investment opportunities to provide actionable recommendations. and key financial signals to support decision-making"),
    backstory=("you are a veteran financial analyst with deep expertise in tntrpreting stock market data."
                   "technical trensd and fundamental;s. you soecialize in producing well-structured reports that evaluate "
                   "stock performance using market indicators")  ,
    llm=llm,
    tools=[get_stock_price],
    verbose=True
)