"""Layer 2: Hierarchical Planner - DAG decomposition with MoE routing."""
import json
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage

PLANNER_MODEL = "llama-3.3-70b-versatile" 
planner = ChatGroq(model=PLANNER_MODEL, temperature=0)

PLANNER_PROMPT = """
You are the 'Hierarchical Planner' (Layer 2) of the Cascade Framework.
Your goal is to decompose a complex task into a Directed Acyclic Graph (DAG) of subtasks.

Input: A 'Sanitized Goal' from Layer 1.
Output: A JSON List of steps.

For each step, you MUST select the correct tool based on these rules:
1. "web_search": REQUIRED for current events, stock prices, weather, or real-time data.
2. "python_interpreter": REQUIRED for math, logic, sorting, or data processing.
3. "llm_generation": ONLY for summarization, explanation, or formatting.

Schema per step:
{
  "id": int,
  "step": "Actionable description",
  "dependencies": [int list],
  "assigned_model": "SLM" or "LLM",
  "tool": "web_search" | "python_interpreter" | "llm_generation",
  "reasoning": "Why this tool/model?"
}

Output ONLY valid JSON.
"""

def generate_plan(layer1_output):
    """Generate execution plan with tool and model assignments."""
    goal = layer1_output.get("sanitized_goal")
    score = layer1_output.get("complexity_score", 10)
    
    print(f"\n>>> [Layer 2] Planning & Routing via {PLANNER_MODEL}...")
    
    # Fast-track trivial tasks
    if score < 3:
        print("    --> Task is trivial. Fast-tracking to SLM.")
        tool = "web_search" if "?" in goal else "llm_generation"
        return [{
            "id": 1, 
            "step": goal, 
            "dependencies": [], 
            "assigned_model": "SLM",
            "tool": tool,
            "reasoning": "Fast track"
        }]

    try:
        messages = [
            SystemMessage(content=PLANNER_PROMPT),
            HumanMessage(content=f"Goal: {goal}")
        ]
        
        response = planner.invoke(messages)
        content = response.content
        
        if "```json" in content:
            content = content.split("```json")[1].split("```")[0]
        elif "```" in content:
            content = content.split("```")[1].split("```")[0]
            
        return json.loads(content)

    except Exception as e:
        print(f"Planner Error: {e}")
        return []