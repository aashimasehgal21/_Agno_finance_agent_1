from agno.agent import Agent 
from agno.models.openai import OpenAIChat
from agno.playground import Playground, serve_playground_app
from agno.storage.agent.sqlite import SqliteAgentStorage
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools
from agno.models.groq import Groq 

agent_storage: str = "tmp/agents.db"

web_agent = Agent(
    name="Web Agent",
    model=Groq(id="llama-3.2-90b-vision-preview"),
    tools=[DuckDuckGoTools()],
    instructions=["Always include source"],
    storage=SqliteAgentStorage(table_name="web_agent", db_file=agent_storage),
    add_datetime_to_instructions=True,
    add_history_to_messages=True,
    num_history_responses=5,
    markdown=True
)

finance_agent=Agent(
    name="Finance Agent",
    model=Groq(id="llama-3.2-90b-vision-preview"),
    tools=[YFinanceTools(stock_price=True,analyst_recommendations=True,stock_fundamentals=True)],
    instructions=["Always use tables to display data"],
    storage=SqliteAgentStorage(table_name="finance_agent", db_file=agent_storage),
    add_datetime_to_instructions=True,
    add_history_to_messages=True,
    num_history_responses=5,
    markdown=True
)

app = Playground(agents=[web_agent,finance_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True)