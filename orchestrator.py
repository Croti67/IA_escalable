import json
from langchain.agents import AgentExecutor, create_react_agent
from langchain_openai import ChatOpenAI
from langchain.tools import tool

from services import get_customer, get_tickets

# 🔹 convertir funciones en tools con decorator
@tool
def get_customer_tool(input: str):
    return get_customer(input)

@tool
def get_tickets_tool(input: str):
    return get_tickets(input)

# 🔹 lista de tools
tools = [get_customer_tool, get_tickets_tool]

# 🔹 modelo
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# 🔹 agente
agent = create_react_agent(llm, tools)

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True
)

# 🔹 ejecutar
if __name__ == "__main__":
    pregunta = input("Pregunta: ")
    respuesta = agent_executor.invoke({"input": pregunta})
    print("\nRespuesta:", respuesta["output"])