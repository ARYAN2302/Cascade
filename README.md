# 🌊 Cascade: A 5-Layer Hierarchical Agent Orchestration Framework

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/release/python-3100/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=Streamlit&logoColor=white)](https://streamlit.io)
[![Groq Powered](https://img.shields.io/badge/Inference-Groq%20LPU-orange)](https://groq.com)

> **Research Artifact:** A dynamic routing architecture that achieves **93.38% reduction in inference costs** by offloading routine agentic subtasks to edge-optimized Small Language Models (SLMs).

![Architecture Diagram](architecture_diagram.png)

---

## 📄 Research Paper
For a detailed analysis of the architecture, mathematical formulation, and full benchmark results, please read the accompanying technical report:
<br>
👉 **[Read the Research Report (PDF)](Cascade_Report.pdf)**

---

## 💡 The Problem: The "Overshoot" Inefficiency
Current agentic systems suffer from a "Compute-per-Token" mismatch. Standard ReAct loops utilize a monolithic Large Language Model (e.g., GPT-4o) for every step of a workflow—whether that step is complex architectural reasoning or simple data formatting.

**Cascade** introduces a hierarchical architecture that treats Intelligence as a tiered resource:
1.  **Route Cheaply:** Handle routine tasks (extraction, formatting, basic code) with quantized SLMs (Llama-3-8B).
2.  **Escalate Rarely:** Only route to Cloud LLMs (Llama-3-70B/GPT-4) when cognitive load exceeds a dynamic threshold.

---

## 🏗 System Architecture

Cascade implements a 5-layer processing pipeline:

| Layer | Component | Function | Model Used |
| :--- | :--- | :--- | :--- |
| **I** | **Semantic Profiler** | Analyzing intent & complexity; filters unsafe inputs. | Llama-3-8B |
| **II** | **Hierarchical Planner** | Decomposes goals into a Directed Acyclic Graph (DAG). | Llama-3-70B |
| **III** | **Hybrid Executor** | Executes subtasks using a **Heterogeneous Model Pool** (Coder/Researcher). | Mixed |
| **IV** | **QA Refiner** | "Critic" loop that verifies outputs & fixes formatting. | Llama-3-70B |
| **V** | **Synthesizer** | Aggregates fragmented memory into a cohesive response. | Llama-3-70B |

---

## 📊 Evaluation & Results

We benchmarked Cascade against a monolithic GPT-4-class baseline across diverse enterprise workflows.

### 1. Cost Efficiency
Cascade achieves massive savings by successfully routing **80% of subtasks** to the SLM layer.

| Metric | Baseline (Monolithic) | Cascade (Hybrid) | Improvement |
| :--- | :--- | :--- | :--- |
| **Total Inference Cost** | $0.2400 | **$0.0158** | **93.38% Savings** |
| **Avg. Latency** | 1.44s | 15.00s | +940% (Tradeoff) |

![Cost Analysis](benchmarks/figure2_results.png)

### 2. Reasoning Boundaries (The "Verifier Paradox")
While efficient for tool-use and coding, the system exhibits performance degradation on symbolic logic tasks (GSM8K), revealing a trade-off between decomposition and reasoning fidelity.

* **Enterprise Automation:** 99% Routing Success (High Efficiency)
* **Symbolic Math:** 25% Accuracy vs 50% Baseline (Low Reasoning)

---

## 🚀 Getting Started

### Prerequisites
* Python 3.10+
* **Groq API Key** (For high-speed LPU inference)
* **Tavily API Key** (For real-time web search)

### Installation
```bash
git clone [https://github.com/ARYAN2302/Cascade.git](https://github.com/ARYAN2302/Cascade.git)
cd Cascade
pip install -r requirements.txt
Environment Setup
Create a .env file or export variables:

Bash

export GROQ_API_KEY="gsk_..."
export TAVILY_API_KEY="tvly-..."
Running the System
1. CLI Mode (The Kernel) Run a single multi-turn session in your terminal:

Bash

python src/main.py
2. Dashboard Mode (The Visualization) Launch the Streamlit interface to visualize the 5 layers in real-time:

Bash

streamlit run src/app.py
📂 Repository Structure
Plaintext

Cascade/
├── src/
│   ├── interpreter.py    # Layer 1: Complexity Profiling
│   ├── planner.py        # Layer 2: DAG Generation
│   ├── executor.py       # Layer 3: Heterogeneous Model Dispatch
│   ├── refiner.py        # Layer 4: Evaluator-Optimizer Loop
│   ├── synthesizer.py    # Layer 5: Final Context Aggregation
│   ├── memory.py         # CoALA-Inspired State Management
│   ├── tools.py          # Tavily Search & Python REPL
│   └── main.py           # Orchestration Logic
├── benchmarks/           # Evaluation datasets and plotting scripts
├── Cascade_Report.pdf    # Full Technical Paper
└── requirements.txt      # Dependencies
🔮 Future Work: ContextOS
Current limitations in long-horizon memory (context window saturation) will be addressed in the next phase of research: ContextOS, a graph-theoretic memory kernel that replaces linear history buffers with a dynamic knowledge graph.
