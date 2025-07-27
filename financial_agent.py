from agno.agent import Agent, RunResponse
from agno.models.groq import Groq
from agno.tools.yfinance import YFinanceTools
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.models.openai import OpenAIChat

import openai
import os
from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

web_search_agent = Agent(
    name="Web Search Agent",
    role="Search the web for the information",
    model=Groq(id="llama3-70b-8192"),  # ✅ updated
    tools=[DuckDuckGoTools()],
    instructions=["Always include source"],
    show_tool_calls=True,
    markdown=True
)

finance_agent = Agent(
    name="Finance Agent",
    role="Get financial data",
    model=Groq(id="llama3-70b-8192"),  # ✅ updated
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
    instructions=["Display data in table format"],
    show_tool_calls=True,
    markdown=True
)

multi_ai_agent = Agent(
    team=[web_search_agent, finance_agent],
    model=Groq(id="llama3-70b-8192"),  # ✅ updated
    instructions=["Always include source", "Display data in table format"],
    show_tool_calls=True,
    markdown=True
)

multi_ai_agent.print_response("Summarize analyst recommendation and share latest news for APPL", stream=True)
