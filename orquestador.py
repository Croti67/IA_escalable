from langchain_ollama import ChatOllama
from langgraph.prebuilt import create_react_agent
from tool import tools as tool_list # Asegúrate de que este import sea correcto

def get_agent():
    # 1. Configura el modelo
    llm = ChatOllama(
        model="qwen2.5:7b ",
        temperature=0
    ) 

    # 2. Configura el agente
    agent_executor = create_react_agent(
        llm, 
        tool_list, 
     prompt = """Eres un asistente técnico. Reglas estrictas:
    - USA siempre las herramientas para obtener datos, NUNCA los inventes.
    - Cuando la herramienta devuelva un resultado, cópialo EXACTAMENTE, no lo interpretes.
    - Si la herramienta dice saldo=500, responde "500". NUNCA cambies el número.
    - Responde de forma amable y directa. NUNCA muestres JSON al usuario."""
    )

    # 3. Devuelve el agente
    return agent_executor