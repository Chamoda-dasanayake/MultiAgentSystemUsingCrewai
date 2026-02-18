from crewai import Agent, LLM
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Fetch the API key from environment
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize LLM with Groq-hosted Llama
llm = LLM(
    provider="groq",  # specify provider
    model="groq/llama-3.1-8b-instant",
    api_key=GROQ_API_KEY, 
    temperature=0.0
)

# Define the analyst agent
analyst_agent = Agent(
    role="Financial Market Analyst",
    goal=(
        "Perform in-depth evaluations of publicly traded stocks using real-time data, "
        "identifying trends, performance insights, and potential investment opportunities "
        "to provide actionable recommendations and key financial signals to support decision-making."
    ),
    backstory=(
        "You are a veteran financial analyst with deep expertise in interpreting stock market data, "
        "technical trends, and fundamentals. You specialize in producing well-structured reports that evaluate "
        "stock performance using market indicators."
    ),
    llm=llm,
    tools=[],
    verbose=True,
    allow_delegation=False
)

