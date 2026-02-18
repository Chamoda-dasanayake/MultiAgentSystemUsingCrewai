from crewai import Agent, LLM
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get Groq API key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize Groq LLM
llm = LLM(
    provider="groq",
    model="groq/llama-3.1-8b-instant",
    api_key=GROQ_API_KEY,
    temperature=0.2
)

# Define trader agent
trader_agent = Agent(
    role="Strategic Stock Trader",
    goal=(
        "Decide whether to buy, sell, or hold a given stock based on analyst insights, "
        "market trends, and risk considerations."
    ),
    backstory=(
        "You are an experienced stock trader specializing in execution strategies and "
        "portfolio decisions. You interpret analyst reports and market signals to "
        "determine optimal trading actions that maximize returns while managing risk."
    ),
    llm=llm,
    tools=[],
    verbose=True
)
