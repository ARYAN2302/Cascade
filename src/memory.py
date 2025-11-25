"""Memory Manager - Working memory (short-term) and Episodic memory (long-term)."""
import json
import time
import os

class MemoryManager:
    def __init__(self, run_id=None):
        self.run_id = run_id or f"run_{int(time.time())}"
        self.working_memory = {}  # Short-term: current execution state
        self.episodic_log = []     # Long-term: action history for debugging
        
        if not os.path.exists("logs"):
            os.makedirs("logs")

    def save_step_output(self, step_id, result, metadata):
        """Store step result in both working and episodic memory."""
        self.working_memory[step_id] = result
        
        entry = {
            "step_id": step_id,
            "timestamp": time.time(),
            "action": "execution",
            "metadata": metadata,
            "result_snippet": result[:50] + "..."
        }
        self.episodic_log.append(entry)
        self._persist_logs()

    def get_working_context(self, dependency_ids):
        """Retrieve context from dependent steps."""
        if not dependency_ids:
            return ""
        
        context_str = "--- WORKING MEMORY (PREVIOUS STEPS) ---\n"
        for dep_id in dependency_ids:
            val = self.working_memory.get(dep_id, "Data missing")
            context_str += f"[Step {dep_id}]: {val}\n"
        return context_str

    def _persist_logs(self):
        """Write episodic memory to disk."""
        with open(f"logs/{self.run_id}.json", "w") as f:
            json.dump(self.episodic_log, f, indent=2)


if __name__ == "__main__":
    mem = MemoryManager()
    mem.save_step_output(1, "Kafka is a stream.", {"model": "SLM", "cost": 0})
    print(mem.get_working_context([1]))