from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools import Tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv

load_dotenv()
def main():
    # Initialize the OpenAI chat model
    llm = ChatOpenAI(model="gpt-4o", temperature=0.0)

    # Define a tool that returns the current time
    def get_current_time():
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    time_tool = Tool(
        name="get_current_time",
        func=get_current_time,
        description="Returns the current date and time."
    )

    # Create a React agent with the LLM and the tool
    agent = create_react_agent(llm, tools=[time_tool])

    # Run the agent with a human message