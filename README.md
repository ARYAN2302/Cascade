# 🌊 Cascade: A 5-Layer Hierarchical Agent Orchestration Framework

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/release/python-3100/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=Streamlit&logoColor=white)](https://streamlit.io)
[![Groq Powered](https://img.shields.io/badge/Inference-Groq%20LPU-orange)](https://groq.com)

> **Research Artifact:** A dynamic routing architecture that achieves **93.38% reduction in inference costs** by offloading routine agentic subtasks to edge-optimized Small Language Models (SLMs).

![Architecture Diagram](architecture_diagram.png)

---

<<<<<<< HEAD
## 📄 Research Paper
For a detailed analysis of the architecture, mathematical formulation, and full benchmark results, please read the accompanying technical report:
<br>
👉 **[Read the Research Report (PDF)](https://github.com/ARYAN2302/Cascade/blob/main/paper/Cascade_Report.pdf)**

---

## �� The Problem: The "Overshoot" Inefficiency
Current agentic systems suffer from a "Compute-per-Token" mismatch. Standard ReAct loops utilize a monolithic Large Language Model (e.g., GPT-4o) for every step of a workflow—whether that step is complex architectural reasoning or simple data formatting.

**Cascade** introduces a hierarchical architecture that treats Intelligence as a tiered resource:
1.  **Route Cheaply:** Handle routine tasks (extraction, formatting, basic code) with quantized SLMs (Llama-3-8B).
2.  **Escalate Rarely:** Only route to Cloud LLMs (Llama-3-70B/GPT-4) when cognitive load exceeds a dynamic threshold.

---

## 🏗 System Architecture
=======
## 🎯 Quick Demo
>>>>>>> d2d317d (Fix app imports, session state, and update research paper link/location)

Launch the interactive dashboard and see Cascade in action:

```bash
# Clone and setup
git clone https://github.com/ARYAN2302/Cascade.git
cd Cascade

# Install dependencies
pip install -r requirements.txt

# Set your API key
export GROQ_API_KEY="gsk_..."

# Launch the demo dashboard
streamlit run src/app.py
```

Then open **http://localhost:8501** and try one of the demo buttons!

Cascade implements a 5-layer processing pipeline:

<<<<<<< HEAD
=======
## 💡 The Problem: The "Overshoot" Inefficiency

Current agentic systems suffer from a "Compute-per-Token" mismatch. Standard ReAct loops utilize a monolithic Large Language Model (e.g., GPT-4o) for every step of a workflow—whether that step is complex architectural reasoning or simple data formatting.

**Cascade** introduces a hierarchical architecture that treats Intelligence as a tiered resource:

1. **Route Cheaply:** Handle routine tasks (extraction, formatting, basic code) with quantized SLMs (Llama-3-8B).
2. **Escalate Rarely:** Only route to Cloud LLMs (Llama-3-70B/GPT-4) when cognitive load exceeds a dynamic threshold.

---

## 🏗 System Architecture

Cascade implements a 5-layer processing pipeline:

>>>>>>> d2d317d (Fix app imports, session state, and update research paper link/location)
| Layer | Component | Function | Model Used |
| :--- | :--- | :--- | :--- |
| **I** | **Semantic Profiler** | Analyzing intent & complexity; filters unsafe inputs. | Llama-3-8B |
| **II** | **Hierarchical Planner** | Decomposes goals into a Directed Acyclic Graph (DAG). | Llama-3-70B |
| **III** | **Hybrid Executor** | Executes subtasks using a **Heterogeneous Model Pool** (Coder/Researcher). | Mixed |
| **IV** | **QA Refiner** | "Critic" loop that verifies outputs & fixes formatting. | Llama-3-70B |
| **V** | **Synthesizer** | Aggregates fragmented memory into a cohesive response. | Llama-3-70B |
<<<<<<< HEAD

---

## 📊 Evaluation & Results

We benchmarked Cascade against a monolithic GPT-4-class baseline across diverse enterprise workflows.

### 1. Cost Efficiency
Cascade achieves massive savings by successfully routing **80% of subtasks** to the SLM layer.

| Metric | Baseline (Monolithic) | Cascade (Hybrid) | Improvement |
| :--- | :--- | :--- | :--- |
| **Total Inference Cost** | $0.2400 | **$0.0158** | **93.38% Savings** |
| **Avg. Latency** | 1.44s | 15.00s | +940% (Tradeoff) |

### 2. Benchmarks by Task Type

| Task Type       | Baseline (GPT-4) | Cascade  | Savings |
|-----------------|------------------|----------|---------|
| Factual Lookup  | $0.0012          | $0.0001  | 92%     |
| Code Generation | $0.0025          | $0.0004  | 84%     |
| Research + Math | $0.0035          | $0.0008  | 77%     |
| **Average**     | -                | -        | **~90%**|

### 3. Reasoning Boundaries (The "Verifier Paradox")
While efficient for tool-use and coding, the system exhibits performance degradation on symbolic logic tasks (GSM8K), revealing a trade-off between decomposition and reasoning fidelity.
But this can easily be solved by adding more slms to the model pool for specific tasks eg- a math model.
And the system is scalable to use more models as needed.

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
git clone https://github.com/ARYAN2302/Cascade.git
cd Cascade
pip install -r requirements.txt
```

### Environment Setup
Create a `.env` file or export variables:
```bash
export GROQ_API_KEY="gsk_..."
export TAVILY_API_KEY="tvly-..."
```

### Running the System
1. **CLI Mode (The Kernel)**: Run a single multi-turn session in your terminal:
```bash
python src/main.py
```
2. **Dashboard Mode (The Visualization)**: Launch the Streamlit interface to visualize the 5 layers in real-time:
```bash
streamlit run src/app.py
```

---

=======

---

## 📊 Evaluation & Results

We benchmarked Cascade against a monolithic GPT-4-class baseline across diverse enterprise workflows.

### 1. Cost Efficiency

Cascade achieves massive savings by successfully routing **80% of subtasks** to the SLM layer.

| Metric | Baseline (Monolithic) | Cascade (Hybrid) | Improvement |
| :--- | :--- | :--- | :--- |
| **Total Inference Cost** | $0.2400 | **$0.0158** | **93.38% Savings** |
| **Avg. Latency** | 1.44s | 15.00s | +940% (Tradeoff) |

![Cost Analysis](figure2_results.png)

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
# Clone the repository
git clone https://github.com/ARYAN2302/Cascade.git
cd Cascade

# Install dependencies
pip install -r requirements.txt
```

### Environment Setup

Create a `.env` file or export variables:

```bash
export GROQ_API_KEY="gsk_..."
export TAVILY_API_KEY="tvly-..."
```

### Running the Demo

#### Option 1: Dashboard Mode (Recommended)

Launch the interactive Streamlit dashboard with real-time metrics:

```bash
streamlit run src/app.py
```

**Features:**
- 📊 Real-time metrics dashboard (cost savings, query count, SLM route rate)
- 🎯 One-click demo examples
- 📈 Step-by-step visualization of the 5-layer pipeline
- 💬 Interactive chat interface
- 💰 Cost comparison with GPT-4 baseline

#### Option 2: CLI Mode

Run a single multi-turn session in your terminal:

```bash
python src/main.py
```

---

>>>>>>> d2d317d (Fix app imports, session state, and update research paper link/location)
## 📂 Repository Structure

```
Cascade/
├── src/
<<<<<<< HEAD
│   ├── interpreter.py   # Layer 1: Task profiling
│   ├── planner.py       # Layer 2: DAG planning + routing
│   ├── executor.py      # Layer 3: Model execution
│   ├── refiner.py       # Layer 4: QA refinement
│   ├── synthesizer.py   # Layer 5: Response synthesis
│   ├── tools.py         # Tavily + Python REPL
│   ├── memory.py        # Working + Episodic memory
│   ├── config.py        # Model configurations
│   ├── metrics.py       # Token tracking
│   ├── main.py          # CLI orchestrator
│   └── app.py           # Streamlit dashboard
├── benchmarks/
│   ├── run_evals.py     # Cost benchmark
│   └── gsm8k_eval.py    # Math accuracy benchmark
├── paper/
│   └── Cascade_Report.pdf # Full Technical Paper
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
=======
│   ├── interpreter.py    # Layer 1: Complexity Profiling
│   ├── planner.py        # Layer 2: DAG Generation
│   ├── executor.py       # Layer 3: Heterogeneous Model Dispatch
│   ├── refiner.py        # Layer 4: Evaluator-Optimizer Loop
│   ├── synthesizer.py    # Layer 5: Final Context Aggregation
│   ├── memory.py         # CoALA-Inspired State Management
│   ├── tools.py          # Tavily Search & Python REPL
│   ├── main.py           # Orchestration Logic (CLI)
│   └── app.py            # Dashboard (Streamlit)
├── benchmarks/           # Evaluation datasets and plotting scripts
├── paper/                # Technical reports
├── architecture_diagram.png
├── figure2_results.png
└── requirements.txt      # Dependencies
>>>>>>> d2d317d (Fix app imports, session state, and update research paper link/location)
```

---

<<<<<<< HEAD
## ⚠️ Known Limitations

### Math Reasoning
The current router assigns math tasks to SLMs, which struggle with multi-step arithmetic. This is a **design trade-off**, not a bug:
- **Root Cause**: The planner breaks math problems into subtasks, losing the chain-of-thought context that LLMs need for reasoning.
- **Impact**: GSM8K accuracy is ~25% vs 83% baseline.
- **Future Fix**: Add a dedicated math specialist SLM or force LLM routing for `intent_category: math`.

### Production Considerations
- Python REPL runs unsandboxed - use [E2B](https://e2b.dev/) or Docker isolation in production
- Rate limits on Groq free tier - add retry logic for high-volume use

---

## 🔮 Future Work: ContextOS
Current limitations in long-horizon memory (context window saturation) will be addressed in the next phase of research: **ContextOS**, a graph-theoretic memory kernel that replaces linear history buffers with a dynamic knowledge graph.

---

## 📄 Research Context
This project implements concepts from:
- **FrugalGPT** (Stanford, 2023) - LLM cascade for cost optimization
- **RouteLLM** (Berkeley, 2024) - Learned routing between models  
- **CoALA** (2023) - Cognitive architecture with memory systems
- **Mixture of Experts** - Specialized sub-networks for different tasks

---

## 📄 License
MIT License - See [LICENSE](LICENSE)

---

<<<<<<< HEAD
## 👤 Author
**Aryan** - [GitHub](https://github.com/ARYAN2302)

Built as a research internship portfolio project demonstrating:
- Multi-agent orchestration
- Cost-aware LLM routing
- Tool-augmented generation
- Production-ready Python architecture

---
**Star ⭐ the repo if you find it useful!**
=======
##  Author
wait
>>>>>>> cb638c9 (readme changes)
=======
## 🎮 Demo Features

The Streamlit dashboard includes:

### Real-time Metrics
- **Queries Processed** - Total queries handled
- **Cost Savings** - Cumulative savings vs GPT-4 baseline
- **SLM Route Rate** - Percentage of queries handled by cheap models
- **Avg Cost/Query** - Average inference cost

### Interactive Demo
- **Simple Task** - Basic retrieval queries
- **Coding Task** - Code generation and debugging
- **Research Task** - Complex analysis queries

### Visual Pipeline
- 5-layer architecture visualization
- Step-by-step processing trace
- Model routing decisions displayed
- Cost savings highlighted

---

## 📄 Research Paper

For a detailed analysis of the architecture, mathematical formulation, and full benchmark results, please read the accompanying technical report:

👉 **[Read the Research Report (PDF)](paper/Cascade_Report.pdf)**

---

## 🔮 Future Work: ContextOS

Current limitations in long-horizon memory (context window saturation) will be addressed in the next phase of research: **ContextOS**, a graph-theoretic memory kernel that replaces linear history buffers with a dynamic knowledge graph.

---

## 📄 License

MIT License - See LICENSE file for details.

---

## 👤 Author

**Aryan** - [GitHub](https://github.com/ARYAN2302)

---

**Star ⭐ the repo if you find it useful!**
>>>>>>> d2d317d (Fix app imports, session state, and update research paper link/location)
