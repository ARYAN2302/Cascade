"""Layer 5: Final Synthesizer - Coherent response assembly."""
from langchain_groq import ChatGroq

SYNTHESIZER_MODEL = "llama-3.3-70b-versatile"
synthesizer = ChatGroq(model=SYNTHESIZER_MODEL, temperature=0.5)

SYNTHESIZER_PROMPT = """
You are the 'Final Synthesizer' (Layer 5) of the Cascade Framework.
Your job is to combine the results of multiple subtasks into a cohesive final response.

Original User Goal: {user_goal}

Subtask Outputs:
{memory_context}

Instructions:
1. Synthesize the information into a clean, professional response.
2. Do not mention "Step 1" or "Step 2". Make it flow naturally.
3. If code was generated, present it clearly.

Output ONLY the final response.
"""

def synthesize_final_response(user_goal, context_memory):
    """Combine step outputs into a cohesive final response."""
    print(f"\n>>> [Layer 5] Synthesizing Final Response...")
    
    formatted_context = ""
    for step_id, result in context_memory.items():
        formatted_context += f"\n--- [Result Part {step_id}] ---\n{result}\n"
    
    try:
        msg = SYNTHESIZER_PROMPT.format(
            user_goal=user_goal,
            memory_context=formatted_context
        )
        return synthesizer.invoke(msg).content

    except Exception as e:
        print(f"Synthesizer Error: {e}")
        return "Error generating final response."


if __name__ == "__main__":
    mock_goal = "Explain how Kafka works."
    mock_memory = {1: "Kafka is a distributed event store.", 2: "It uses Topics and Partitions for scalability."}
    print(synthesize_final_response(mock_goal, mock_memory))