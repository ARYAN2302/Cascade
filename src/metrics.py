"""Token tracking and cost calculation for benchmarking."""
import tiktoken

class TokenTracker:
    def __init__(self):
        self.encoding = tiktoken.get_encoding("cl100k_base")
        
        # Pricing per 1M tokens (2025 rates)
        self.PRICING = {
            "gpt-4o": {"input": 5.00, "output": 15.00},
            "llama-3-8b": {"input": 0.20, "output": 0.20},
            "llama-3-70b": {"input": 0.90, "output": 0.90}
        }

    def count(self, text):
        if not text: return 0
        return len(self.encoding.encode(str(text)))

    def calculate_cost(self, model_name, input_text, output_text):
        """Calculate token counts and cost for a model call."""
        in_tok = self.count(input_text)
        out_tok = self.count(output_text)
        
        price_key = "gpt-4o"
        if "8b" in model_name: price_key = "llama-3-8b"
        if "70b" in model_name: price_key = "llama-3-70b"
        
        cost_input = (in_tok / 1_000_000) * self.PRICING[price_key]["input"]
        cost_output = (out_tok / 1_000_000) * self.PRICING[price_key]["output"]
        
        return cost_input + cost_output, in_tok, out_tok