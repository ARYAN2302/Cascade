"""Layer 4: Quality Assurance Refiner - Output validation and correction."""
from langchain_groq import ChatGroq

REFINER_MODEL = "llama-3.3-70b-versatile"
refiner = ChatGroq(model=REFINER_MODEL, temperature=0)

REFINER_PROMPT = """
You are the 'Quality Assurance Refiner' (Layer 4).
Your job is to ensure the output matches the requirements perfectly.

User Instruction: {step_instruction}
Current Output: {current_result}

Check for:
1. Completeness (Did it answer the whole prompt?)
2. Accuracy (Are there obvious errors?)
3. Formatting (Is it clean? No markdown artifacts if not requested).

If the output is excellent, return it EXACTLY as is.
If the output is flawed, REWRITE it to be perfect.

Output ONLY the final cleaned text. Do not add conversational filler like "Here is the fixed version".
"""

def refine_output(step_data, raw_result):
    """Validate and refine step output for quality."""
    print(f"\n>>> [Layer 4] QA Refinement for Step {step_data['id']}...")
    
    try:
        msg = REFINER_PROMPT.format(
            step_instruction=step_data['step'],
            current_result=raw_result
        )
        
        response = refiner.invoke(msg)
        refined_result = response.content.strip()
        
        if refined_result != raw_result:
            print("    --> QA Action: ⚠️ Output was refined/polished.")
        else:
            print("    --> QA Action: ✅ Output passed check.")
            
        return refined_result

    except Exception as e:
        print(f"Refiner Error: {e}")
        return raw_result


if __name__ == "__main__":
    step_good = {"id": 1, "step": "Define HTTP"}
    res_good = "HTTP stands for Hypertext Transfer Protocol. It is the foundation of data communication for the World Wide Web."
    print(f"Final 1: {refine_output(step_good, res_good)}\n")
    
    step_bad = {"id": 2, "step": "List the 3 primary colors in a bulleted list."}
    res_bad = "red blue yellow"
    print(f"Final 2: {refine_output(step_bad, res_bad)}")