"""Cascade Framework - Multi-turn hierarchical agent orchestration."""
from interpreter import profile_task
from planner import generate_plan
from executor import execute_step
from refiner import refine_output
from synthesizer import synthesize_final_response
from memory import MemoryManager

class CascadeSystem:
    def __init__(self):
        print("="*70)
        print(f"🚀 CASCADE SYSTEM INITIALIZED (Multi-Turn Mode)")
        print("="*70)
        self.memory = MemoryManager()
        self.turn_count = 0

    def run_turn(self, user_input):
        self.turn_count += 1
        print(f"\n\n🔴 --- TURN {self.turn_count} ---")
        print(f"📝 USER: '{user_input}'")

        # Context awareness for multi-turn
        full_context_input = user_input
        if self.turn_count > 1:
            last_output = self.memory.episodic_log[-1]['result_snippet']
            full_context_input = f"Context from previous turn: ...{last_output}\n\nCurrent Request: {user_input}"

        # Layer 1: Semantic Profiling
        profiler_data = profile_task(full_context_input)
        if not profiler_data: return "Security Blocked."
        
        print(f"📊 [Layer 1] Intent: {profiler_data.get('intent_category')} | Complexity: {profiler_data.get('complexity_score')}")

        # Layer 2: Hierarchical Planning
        plan = generate_plan(profiler_data)
        print(f"🗺️ [Layer 2] Plan: {len(plan)} steps generated.")

        # Layer 3 & 4: Execution + Refinement
        current_turn_memory = {} 
        completed_steps = set()
        
        while len(completed_steps) < len(plan):
            executable = [s for s in plan if s['id'] not in completed_steps and 
                          all(d in completed_steps for d in s['dependencies'])]
            
            if not executable:
                print("!!! DEADLOCK. Skipping remaining steps.")
                break

            for step in executable:
                step_id = step['id']
                print(f"\n⚙️ [Step {step_id}] {step['step']} ({step.get('assigned_model')})")

                step_context = ""
                for dep in step['dependencies']:
                    step_context += f"\n[Ref: Step {dep}]: {current_turn_memory[dep]}"

                exec_result = execute_step(step, context=step_context)
                final_output = refine_output(step, exec_result['result'])
                
                current_turn_memory[step_id] = final_output
                completed_steps.add(step_id)
                
                self.memory.save_step_output(
                    step_id=f"T{self.turn_count}-S{step_id}", 
                    result=final_output, 
                    metadata={"turn": self.turn_count, "model": exec_result['model_used']}
                )

        # Layer 5: Synthesis
        print("\n🏁 [Layer 5] Synthesizing Response...")
        final_response = synthesize_final_response(user_input, current_turn_memory)
        
        print(f"\n🤖 CASCADE: {final_response}")
        return final_response


if __name__ == "__main__":
    system = CascadeSystem()
    
    print("\nType 'exit' to quit.\n")
    while True:
        try:
            try:
                user_in = input("\nUser: ")
            except EOFError:
                print("\nExiting...")
                break
                
            if user_in.lower() in ['exit', 'quit']:
                break
            
            if not user_in.strip():
                continue
            
            system.run_turn(user_in)
            
        except KeyboardInterrupt:
            print("\nExiting...")
            break