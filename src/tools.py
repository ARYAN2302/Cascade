"""ToolKit - Real tools for web search (Tavily) and Python execution."""
import os
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_experimental.utilities import PythonREPL

class ToolKit:
    def __init__(self):
        print(">>> [System] Initializing ToolKit (Tavily + Python REPL)...")
        
        if not os.getenv("TAVILY_API_KEY"):
            print("⚠️ WARNING: TAVILY_API_KEY not found. Web search will fail.")
        
        self.search_tool = TavilySearchResults(max_results=3)
        self.python_repl = PythonREPL()  # Note: Use Docker/E2B in production

    def run(self, tool_name, query):
        """Execute tool and return results."""
        try:
            if tool_name == "web_search":
                print(f"    [Tool 🔍] Searching: '{query[:50]}...'")
                results = self.search_tool.invoke(query)
                
                summary = ""
                for res in results:
                    summary += f"- {res['content'][:300]}...\n  (Source: {res['url']})\n"
                return summary

            elif tool_name == "python_interpreter":
                print(f"    [Tool 🐍] Executing Python...")
                code = query.strip()
                if "```python" in code:
                    code = code.split("```python")[1].split("```")[0]
                elif "```" in code:
                    code = code.split("```")[1].split("```")[0]
                
                output = self.python_repl.run(code)
                return f"Execution Output:\n{output}"
                
            elif tool_name == "llm_generation":
                return None
                
            else:
                return f"Error: Tool '{tool_name}' not found."

        except Exception as e:
            return f"Tool Execution Error: {str(e)}"


if __name__ == "__main__":
    tk = ToolKit()
    print("Testing Web Search...")
    print(tk.run("web_search", "What is the current price of Bitcoin?"))
    print("\nTesting Python REPL...")
    print(tk.run("python_interpreter", "print(153 * 49)"))