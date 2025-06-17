# MCP Demo

This repository demonstrates how to use [langchain-mcp-adapters](https://github.com/langchain-ai/langchain-mcp-adapters) to connect multiple MCP (Modular Command Protocol) servers and use them as tools in a LangChain agent. The demo includes a simple math server and an example of connecting to a weather server.

## Features

- **Math Server**: Provides simple math operations (add, multiply) via MCP.
- **Weather Server**: Example configuration for connecting to a weather MCP server (assumed to be running separately).
- **LangChain Agent**: Uses [LangGraph](https://github.com/langchain-ai/langgraph) and [langchain-groq](https://github.com/langchain-ai/langchain-groq) to create an agent that can use both math and weather tools.

## Requirements

- Python 3.12+
- [langchain-groq](https://pypi.org/project/langchain-groq/)
- [langchain-mcp-adapters](https://pypi.org/project/langchain-mcp-adapters/)
- [langgraph](https://pypi.org/project/langgraph/)
- [mcp](https://pypi.org/project/mcp/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

## Installation

1. Clone the repository: `git clone https://github.com/your-username/mcpdemo.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Create a `.env` file with your Groq API key: `GROQ_API_KEY=your-api-key`

## Running the Demo

1. Start the math server: `python mathserver.py`
2. Run the client: `python client.py`

## Example Use Cases

- Math operations: The math server provides simple math operations like addition and multiplication.
- Weather information: The weather server (example configuration) can be used to retrieve weather information.

## Contributing

Contributions are welcome! Please submit a pull request with your changes.
