"""Layer 3: Specialized Executor - Tool invocation with model routing."""
from config import slm_researcher, slm_coder, llm_expert
from tools import ToolKit

tools = ToolKit()

EXECUTE_PROMPT = """
You are a {role}.
Task: {step_desc}
Context: {context}
Tool Output: {tool_output}

Perform the task concisely.
"""

def execute_step(step_data, context=""):
    """Execute a single step with appropriate model and tools."""
    step_desc = step_data['step']
    assigned_model = step_data.get('assigned_model', 'LLM')
    tool_name = step_data.get('tool', 'llm_generation')
    
    print(f"\n>>> [Layer 3] Executing Step {step_data['id']} ({assigned_model} + {tool_name})...")
    
    # Run tool first if needed
    tool_result = tools.run(tool_name, step_desc)
    
    # Route to specialized model based on assignment and tool
    if assigned_model == "SLM":
        if tool_name == "python_interpreter":
            active_model, role = slm_coder, "Python Expert"
        else:
            active_model, role = slm_researcher, "Research Assistant"
    else:
        active_model, role = llm_expert, "Senior Architect"

    try:
        prompt = EXECUTE_PROMPT.format(
            role=role,
            step_desc=step_desc,
            context=context,
            tool_output=tool_result or "None"
        )
        
        response = active_model.invoke(prompt)
        cost = 0.0 if assigned_model == "SLM" else 0.03
        print(f"    --> Finished via {role}. Cost: ${cost}")
        
        return {"result": response.content, "model_used": role, "cost": cost}

    except Exception as e:
        print(f"Executor Error: {e}")
        return {"result": "Error", "model_used": "Error", "cost": 0}


if __name__ == "__main__":
    step1 = {"id": 1, "step": "Define a Python function to sort a list.", "assigned_model": "SLM", "tool": "python_interpreter"}
    execute_step(step1)
    
    step2 = {"id": 2, "step": "Explain the strategic impact of AI on banking.", "assigned_model": "LLM", "tool": "llm_generation"}
    execute_step(step2)