# Layer 3: Router (The Cost Saver)
import json
from langchain_groq import ChatGroq

# --- CONFIGURATION ---
# WHY TWO MODELS?
# 1. The WORKER (8B) is the "Intern". It's cheap and fast.
WORKER_MODEL = "llama-3.1-8b-instant"
# 2. The EXPERT (70B) is the "Judge". It has higher reasoning capabilities.
EXPERT_MODEL = "llama-3.3-70b-versatile"

# WHY TEMPERATURE DIFFERENCE?
# Worker (0.3): Needs a little creativity to write answers.
# Judge (0.0): Needs to be cold, hard, and consistent. Math shouldn't be creative.
worker = ChatGroq(model=WORKER_MODEL, temperature=0.3)
expert = ChatGroq(model=EXPERT_MODEL, temperature=0)

# --- PROMPTS ---

# 1. Execution Prompt: Standard "Do the work" instruction.
EXECUTE_PROMPT = """
You are a specialized worker agent. 
Task: {step_description}
Context: {context}

Provide a concise, high-quality answer.
"""

# 2. Verifier Prompt: The "Metacognition" Layer.
# We force the model to output a NUMBER (score) so we can write an 'if' statement.
VERIFIER_PROMPT = """
You are a Quality Assurance Judge.
Review the following Answer for the given Task.

Task: {step_description}
Answer: {answer}

Rate the quality on a scale of 0.0 to 1.0.
- 1.0 = Perfect, fully addresses the task.
- 0.5 = Partial or vague.
- 0.0 = Wrong or hallucinated.

Output JSON ONLY: {{"score": float, "reason": "string"}}
"""

def execute_step_with_cascade(step_data, context=""):
    step_desc = step_data['step']
    print(f"\n>>> [Layer 3] Executing Step {step_data['id']}: '{step_desc}'")
    
    # --- PHASE 1: TRY CHEAP MODEL (The Intern) ---
    print(f"    --> Attempting with SLM ({WORKER_MODEL})...")
    
    try:
        # Run the cheap model
        response_slm = worker.invoke(
            EXECUTE_PROMPT.format(step_description=step_desc, context=context)
        )
        answer = response_slm.content
        
        # --- PHASE 2: SELF-REFLECTION (The Judge) ---
        # "Did the intern do a good job?"
        # Note: This is a 70B model call, BUT it's very short (cheap).
        verify_msg = VERIFIER_PROMPT.format(step_description=step_desc, answer=answer)
        grade_response = expert.invoke(verify_msg)
        
        # Robust Parsing logic (same as Layer 1/2)
        content = grade_response.content
        if "```json" in content:
            content = content.split("```json")[1].split("```")[0]
        elif "```" in content:
            content = content.split("```")[1].split("```")[0]
            
        grade_data = json.loads(content)
        score = grade_data.get("score", 0)
        
        print(f"    --> Verification Score: {score} | Reason: {grade_data.get('reason')}")
        
        # --- PHASE 3: THE DECISION (The Cascade) ---
        # WHY 0.8?
        # This is a hyperparameter. 
        # Too high (0.99) -> You reject everything (Cost goes up).
        # Too low (0.5) -> You accept bad answers (Quality goes down).
        # 0.8 is the "Goldilocks" zone for Research claims.
        if score >= 0.8:
            print("    --> Success! Keeping SLM result. (Cost Savings: HIGH)")
            return {
                "result": answer, 
                "model_used": "SLM (8B)", 
                "cost_saved": True
            }
        
        else:
            print("    --> Score too low. Escalating to Expert (70B)...")
            # --- PHASE 4: RETRY WITH EXPENSIVE MODEL ---
            # The intern failed. We pay the expert to do it from scratch.
            response_llm = expert.invoke(
                EXECUTE_PROMPT.format(step_description=step_desc, context=context)
            )
            return {
                "result": response_llm.content, 
                "model_used": "LLM (70B)", 
                "cost_saved": False
            }

    except Exception as e:
        print(f"Router Error: {e}")
        return {"result": "Error executing step", "model_used": "Error", "cost_saved": False}

# --- TEST HARNESS ---
if __name__ == "__main__":
    # Test 1: Easy Task (SLM should pass)
    step_easy = {"id": 1, "step": "Define what HTTP stands for."}
    res1 = execute_step_with_cascade(step_easy)
    
    # Test 2: Hard Task (SLM usually fails Logic Puzzles)
    step_hard = {"id": 2, "step": "Solve this: I have 3 apples. I eat 2. I buy 5 more. How many do I have? Explain step by step."}
    res2 = execute_step_with_cascade(step_hard)
