import streamlit as st
from orquestador import get_agent
from langchain_core.messages import HumanMessage, AIMessage 


st.title("Asistente IA de Servicios")

if "agent_executor" not in st.session_state:
    st.session_state.agent_executor = get_agent()
    st.session_state.messages = [] # Aquí almacenamos el historial

# Muestra mensajes previos
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("¿En qué puedo ayudarte?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        

# ... dentro de tu bloque 'with st.chat_message("assistant"):' ...
        with st.spinner("Consultando..."):
            # 1. Convertir los mensajes de Streamlit al formato de LangChain
            langchain_messages = []
            for msg in st.session_state.messages:
                if msg["role"] == "user":
                    langchain_messages.append(HumanMessage(content=msg["content"]))
                else:
                    langchain_messages.append(AIMessage(content=msg["content"]))
            
            # 2. Invocar al agente con la lista convertida
            response = st.session_state.agent_executor.invoke(
                {"messages": langchain_messages}
            )
        
            final_message = response["messages"][-1].content
            st.markdown(final_message)
            
    st.session_state.messages.append({"role": "assistant", "content": final_message})