from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools import Tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv

load_dotenv()
def main():
    model = ChatOpenAI(temperature=0.0,)
    tools = []
    agent_executor = create_react_agent(model,tools)

    print("Welcome!! I am Your AI Assistant. You can ask me anything. Type 'exit' to quit.")
    print("You can also use tools like 'calculator' or 'weather' if available.")
    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() == 'exit':
            print("Exiting the chat. Goodbye!")
            break

            
        try:
            response = agent_executor.invoke(HumanMessage(content=user_input))
            print(f"AI: {response.content}")
        except Exception as e:
            print(f"An error occurred: {e}")
