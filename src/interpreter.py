"""Layer 1: Semantic Profiler - Task classification and complexity scoring."""
import json
import time
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage

SLM_MODEL_NAME = "llama-3.1-8b-instant"
slm = ChatGroq(model=SLM_MODEL_NAME, temperature=0)

INTERPRETER_PROMPT = """
You are the 'Semantic Profiler' (Layer 1) of the Cascade Framework.
Your goal is to minimize compute costs by filtering trivial tasks.

Analyze the User Input and output a JSON object with these keys:
1. "sanitized_goal": Clear technical description of the task (remove pleasantries).
2. "intent_category": ["retrieval", "coding", "math", "reasoning", "creative"].
3. "complexity_score": Integer 1-10.
    - 1-3: Simple formatting, factual lookup (Route to SLM).
    - 4-7: Single function coding, simple analysis (Route to SLM).
    - 8-10: Multi-file coding, complex reasoning, system design (Route to LLM).
4. "is_safe": Boolean. False if malicious/illegal.

Output ONLY valid JSON. No markdown formatting.
"""

def profile_task(user_input: str):
    """Analyze task intent and complexity for optimal routing."""
    print(f"\n>>> [Layer 1] Profiling via {SLM_MODEL_NAME}: '{user_input[:50]}...'")
    start_time = time.time()
    
    try:
        messages = [
            SystemMessage(content=INTERPRETER_PROMPT),
            HumanMessage(content=user_input)
        ]
        
        response = slm.invoke(messages)
        content = response.content.strip()
        
        # Parse JSON from model response
        if "```json" in content:
            content = content.split("```json")[1].split("```")[0]
        elif "```" in content:
            content = content.split("```")[1].split("```")[0]
            
        profile = json.loads(content)
        profile["profiling_latency"] = round(time.time() - start_time, 3)
        profile["model_provider"] = "Groq (LPU)"
        
        # Security guardrail
        if not profile.get("is_safe", True):
            print("!!! SECURITY BLOCK: Request rejected !!!")
            return {"error": "unsafe_content", "is_safe": False, "complexity_score": 0}
            
        return profile

    except Exception as e:
        print(f"Profiler Failed: {e}")
        return {
            "sanitized_goal": user_input,
            "complexity_score": 10,
            "intent_category": "unknown",
            "is_safe": True
        }


if __name__ == "__main__":
    print(json.dumps(profile_task("What is the speed of light?"), indent=2))
    print(json.dumps(profile_task("Design a microservices architecture for a banking app using Kafka."), indent=2))

