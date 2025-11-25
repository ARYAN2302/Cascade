"""Model configuration for Cascade Framework."""
from langchain_groq import ChatGroq

# SLM specialists (8B) - Cost-effective for focused tasks
slm_researcher = ChatGroq(model="llama-3.1-8b-instant", temperature=0.2)
slm_coder = ChatGroq(model="llama-3.1-8b-instant", temperature=0.1)

# LLM expert (70B) - High-capacity reasoning
llm_expert = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.7)

def get_model(role):
    """Route to appropriate model based on task role."""
    if role == "coder": return slm_coder
    if role == "researcher": return slm_researcher
    return llm_expert