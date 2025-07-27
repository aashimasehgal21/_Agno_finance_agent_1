What is AGNO?

**AGNO** (Agent-based Generalized Neural Orchestration) is a lightweight Python framework designed to build intelligent AI agents using Large Language Models (LLMs). It allows you to:

* Create agents with specific roles and instructions
* Integrate tools like web search, finance APIs, databases, and more
* Persist agent memory using SQLite
* Run agents via terminal or a visual playground
* Easily switch between OpenAI, Groq, and other LLM providers

AGNO simplifies the process of building **modular, interactive, and intelligent AI systems** for real-world applications.


 🚀 What is This Project?
This project uses **AGNO** to build a multi-agent AI system that performs:

🧠 1. Web Search Agent
* Uses Groq’s LLaMA 3 model and `DuckDuckGoTools`
* Searches the internet for real-time information and news
* Always includes the source for trust and verification

 💹 2. Finance Agent

* Uses the same Groq model with `YFinanceTools`
* Retrieves:

  * Current stock prices
  * Analyst recommendations
  * Stock fundamentals
* Displays data in clean, easy-to-read table format

 🤝 3. Multi-Agent Collaboration

* Combines both agents to perform tasks like:

  * “Summarize analyst recommendations and latest news for AAPL”
  * Providing both financial analysis and news from the web in a single response

 💡 Why Is This Useful?
This project is valuable because it:

* Automates research and financial analysis
* Reduces time spent on manual stock/news searching
* Combines real-time data from web + finance in one intelligent response
* Can be extended to other domains (e.g. health, education, tech analysis)
* Offers both **terminal-based streaming** and **GUI-based playground** for users to interact

 🧰 Tools & Technologies Used
* 🧠 **AGNO framework**
* ⚡ **Groq LLaMA 3 models**
* 🌐 **DuckDuckGoTools** (web search)
* 📊 **YFinanceTools** (finance data)
* 💾 **SQLite** (agent memory storage)
* 🧪 **Playground UI** (to interact visually)



Let me know if you want this in **pure Hindi** or **LinkedIn-style post format** too.
