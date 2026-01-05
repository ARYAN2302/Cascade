"""
Cascade Framework - Professional Streamlit Dashboard
Visual upgrade with real-time metrics and demo mode.
"""
import streamlit as st
import time
import json
from datetime import datetime

# Import existing Cascade modules
from interpreter import profile_task
from planner import generate_plan
from router import execute_step_with_cascade
from refiner import refine_output
from synthesizer import synthesize_final_response
from memory import MemoryManager

# Page configuration
st.set_page_config(
    page_title="Cascade - Hierarchical Agent Orchestration",
    page_icon="🌊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for professional styling
st.markdown("""
<style>
    /* Main header styling */
    .main-header {
        background: linear-gradient(135deg, #1e3a5f 0%, #2d5a87 100%);
        padding: 25px;
        border-radius: 15px;
        margin-bottom: 25px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    
    .main-header h1 {
        color: white !important;
        margin: 0;
        font-size: 2.2em;
    }
    
    .main-header p {
        color: #a8d4f0 !important;
        margin: 8px 0 0 0;
        font-size: 1.1em;
    }
    
    /* Metric cards */
    .metric-card {
        background: white;
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        border-left: 4px solid #2d5a87;
    }
    
    .metric-value {
        font-size: 2em;
        font-weight: bold;
        color: #1e3a5f;
        margin: 0;
    }
    
    .metric-label {
        color: #666;
        font-size: 0.9em;
        margin: 5px 0 0 0;
    }
    
    /* Layer indicator */
    .layer-badge {
        display: inline-block;
        padding: 8px 16px;
        border-radius: 20px;
        font-weight: bold;
        margin: 3px;
        font-size: 0.85em;
    }
    
    .layer-1 { background: #e3f2fd; color: #1565c0; }
    .layer-2 { background: #e8f5e9; color: #2e7d32; }
    .layer-3 { background: #fff3e0; color: #ef6c00; }
    .layer-4 { background: #fce4ec; color: #c2185b; }
    .layer-5 { background: #f3e5f5; color: #7b1fa2; }
    
    /* Chat messages */
    .user-msg {
        background: #2d5a87;
        color: white;
        padding: 12px 18px;
        border-radius: 18px 18px 4px 18px;
        margin: 8px 0;
    }
    
    .bot-msg {
        background: #f0f4f8;
        color: #1e3a5f;
        padding: 12px 18px;
        border-radius: 18px 18px 18px 4px;
        margin: 8px 0;
        border-left: 3px solid #2d5a87;
    }
    
    /* Demo button */
    .demo-btn {
        background: linear-gradient(135deg, #2d5a87 0%, #1e3a5f 100%);
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 8px;
        cursor: pointer;
        font-weight: bold;
        margin: 5px;
    }
    
    .demo-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
    }
    
    /* Status indicator */
    .status-running {
        color: #ff9800;
        animation: pulse 1.5s infinite;
    }
    
    @keyframes pulse {
        0% { opacity: 1; }
        50% { opacity: 0.5; }
        100% { opacity: 1; }
    }
    
    /* Architecture diagram container */
    .arch-container {
        background: linear-gradient(180deg, #f8fafc 0%, #e2e8f0 100%);
        border-radius: 15px;
        padding: 20px;
        margin: 15px 0;
    }
    
    /* Cost savings highlight */
    .savings-highlight {
        background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%);
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        border: 2px solid #4caf50;
    }
    
    .savings-value {
        font-size: 2.5em;
        font-weight: bold;
        color: #2e7d32;
    }
    
    .savings-label {
        color: #4caf50;
        font-size: 0.95em;
    }
</style>
""", unsafe_allow_html=True)


class CascadeDashboard:
    """Professional dashboard for Cascade Framework."""
    
    def __init__(self):
        self.session_state_init()
        self.metrics_init()
    
    def session_state_init(self):
        """Initialize Streamlit session state."""
        if "messages" not in st.session_state:
            st.session_state.messages = []
        if "total_cost" not in st.session_state:
            st.session_state.total_cost = 0.0
        if "queries_processed" not in st.session_state:
            st.session_state.queries_processed = 0
        if "slm_usage" not in st.session_state:
            st.session_state.slm_usage = 0
        if "llm_usage" not in st.session_state:
            st.session_state.llm_usage = 0
        if "show_cost_comparison" not in st.session_state:
            st.session_state.show_cost_comparison = False
        if "baseline_cost" not in st.session_state:
            st.session_state.baseline_cost = 0.24  # GPT-4 baseline per query
    
    def metrics_init(self):
        """Initialize metrics tracking."""
        pass
    
    def display_header(self):
        """Display professional header."""
        st.markdown("""
        <div class="main-header">
            <h1>🌊 Cascade</h1>
            <p>Hierarchical Agent Orchestration Framework • 5-Layer Processing Pipeline</p>
        </div>
        """, unsafe_allow_html=True)
    
    def display_metrics_panel(self):
        """Display real-time metrics dashboard."""
        st.markdown("### 📊 Real-time Metrics")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown(f"""
            <div class="metric-card">
                <p class="metric-value">{st.session_state.queries_processed}</p>
                <p class="metric-label">Queries Processed</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            savings = st.session_state.baseline_cost * st.session_state.queries_processed - st.session_state.total_cost
            st.markdown(f"""
            <div class="metric-card">
                <p class="metric-value">${savings:.4f}</p>
                <p class="metric-label">Cost Savings</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            total_models = st.session_state.slm_usage + st.session_state.llm_usage
            slm_pct = (st.session_state.slm_usage / total_models * 100) if total_models > 0 else 0
            st.markdown(f"""
            <div class="metric-card">
                <p class="metric-value">{slm_pct:.0f}%</p>
                <p class="metric-label">SLM Route Rate</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col4:
            avg_cost = st.session_state.total_cost / st.session_state.queries_processed if st.session_state.queries_processed > 0 else 0
            st.markdown(f"""
            <div class="metric-card">
                <p class="metric-value">${avg_cost:.4f}</p>
                <p class="metric-label">Avg Cost/Query</p>
            </div>
            """, unsafe_allow_html=True)
    
    def display_architecture(self):
        """Display 5-layer architecture visualization."""
        st.markdown("### 🏗️ 5-Layer Processing Pipeline")
        
        st.markdown("""
        <div class="arch-container">
            <div style="display: flex; justify-content: space-around; align-items: center; flex-wrap: wrap; gap: 10px;">
                <div style="text-align: center;">
                    <span class="layer-badge layer-1">🔍 Layer 1<br><small>Semantic Profiler</small></span>
                    <div style="color: #666;">▼</div>
                </div>
                <div style="text-align: center;">
                    <span class="layer-badge layer-2">🗺️ Layer 2<br><small>Hierarchical Planner</small></span>
                    <div style="color: #666;">▼</div>
                </div>
                <div style="text-align: center;">
                    <span class="layer-badge layer-3">⚙️ Layer 3<br><small>Hybrid Executor</small></span>
                    <div style="color: #666;">▼</div>
                </div>
                <div style="text-align: center;">
                    <span class="layer-badge layer-4">✅ Layer 4<br><small>QA Refiner</small></span>
                    <div style="color: #666;">▼</div>
                </div>
                <div style="text-align: center;">
                    <span class="layer-badge layer-5">🎯 Layer 5<br><small>Synthesizer</small></span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Quick explanation
        with st.expander("ℹ️ How Cascade Works"):
            st.markdown("""
            **Cascade** intelligently routes queries through a 5-layer pipeline:
            
            1. **🔍 Semantic Profiler** - Analyzes intent and complexity (Llama-3-8B)
            2. **🗺️ Hierarchical Planner** - Breaks complex tasks into subtasks (Llama-3-70B)
            3. **⚙️ Hybrid Executor** - Routes to optimal model (SLM first, escalate if needed)
            4. **✅ QA Refiner** - Quality check and corrections
            5. **🎯 Synthesizer** - Aggregates results into final response
            
            **Result:** 93% cost savings vs monolithic GPT-4 baseline
            """)
    
    def display_demo_section(self):
        """Display demo examples section."""
        st.markdown("### 🚀 Try It Now")
        
        col1, col2, col3 = st.columns(3)
        
        demo_queries = [
            ("📝 Simple Task", "What is the capital of France?", "Simple retrieval"),
            ("💻 Coding Task", "Write a Python function to calculate factorial", "Code generation"),
            ("🔬 Research Task", "Explain the benefits of hierarchical agent systems", "Analysis"),
        ]
        
        with col1:
            if st.button("📝 Simple Task", use_container_width=True):
                self.process_query("What is the capital of France?")
        
        with col2:
            if st.button("💻 Coding Task", use_container_width=True):
                self.process_query("Write a Python function to calculate factorial")
        
        with col3:
            if st.button("🔬 Research Task", use_container_width=True):
                self.process_query("Explain the benefits of hierarchical agent systems")
    
    def display_chat_interface(self):
        """Display chat interface."""
        st.markdown("### 💬 Interactive Demo")
        
        # Chat history
        chat_container = st.container()
        
        with chat_container:
            for msg in st.session_state.messages:
                role = msg["role"]
                content = msg["content"]
                
                if role == "user":
                    st.markdown(f'<div class="user-msg"><strong>You:</strong> {content}</div>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<div class="bot-msg"><strong>Cascade:</strong><br>{content}</div>', unsafe_allow_html=True)
        
        # Input area
        user_input = st.text_area("Enter your query:", placeholder="Type anything here...", height=80)
        
        col1, col2 = st.columns([1, 4])
        
        with col1:
            process_btn = st.button("🚀 Process", type="primary", use_container_width=True)
        
        with col2:
            st.info("💡 Tip: Try complex multi-step tasks to see Cascade's planning in action")
        
        if process_btn and user_input:
            self.process_query(user_input)
    
    def process_query(self, user_input: str):
        """Process a query through the Cascade pipeline."""
        # Add user message
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        # Create containers for real-time updates
        status_container = st.container()
        result_container = st.container()
        
        with status_container:
            st.markdown("### ⚡ Processing...")
            
            # Progress indicator
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            # Layer 1: Profiling
            status_text.markdown("🔍 **Layer 1:** Analyzing task complexity...")
            progress_bar.progress(20)
            time.sleep(0.3)  # Simulated delay for visual effect
            
            profiler_data = profile_task(user_input)
            
            with st.expander("📊 Layer 1 Results", expanded=True):
                st.json({
                    "Intent Category": profiler_data.get("intent_category", "unknown"),
                    "Complexity Score": f"{profiler_data.get('complexity_score', 0)}/10",
                    "Sanitized Goal": profiler_data.get("sanitized_goal", user_input),
                    "Profiling Time": f"{profiler_data.get('profiling_latency', 0)}s"
                })
            
            # Layer 2: Planning
            status_text.markdown("🗺️ **Layer 2:** Generating task plan...")
            progress_bar.progress(40)
            time.sleep(0.3)
            
            plan = generate_plan(profiler_data)
            
            with st.expander("📋 Layer 2 Results", expanded=True):
                st.markdown(f"**Plan with {len(plan)} steps:**")
                for step in plan:
                    st.markdown(f"- Step {step['id']}: {step['step']} → `{step.get('assigned_model', 'TBD')}`")
            
            # Layer 3-4: Execution
            status_text.markdown("⚙️ **Layer 3-4:** Executing and refining...")
            progress_bar.progress(60)
            time.sleep(0.3)
            
            memory = MemoryManager()
            step_results = {}
            
            for step in plan:
                with st.expander(f"⚙️ Step {step['id']}: {step['step']}", expanded=False):
                    st.markdown(f"**Assigned Model:** `{step.get('assigned_model')}`")
                    
                    exec_result = execute_step_with_cascade(step)
                    
                    if exec_result.get("cost_saved"):
                        st.success(f"✅ SLM Success! (Cost saved)")
                        st.session_state.slm_usage += 1
                    else:
                        st.warning(f"⚠️ Escalated to LLM (higher cost)")
                        st.session_state.llm_usage += 1
                    
                    final_out = refine_output(step, exec_result['result'])
                    step_results[step['id']] = final_out
                    
                    st.markdown(f"**Result:** {final_out[:200]}...")
                    
                    # Track cost
                    cost = 0.0158 if exec_result.get("cost_saved") else 0.24
                    st.session_state.total_cost += cost
            
            progress_bar.progress(80)
            
            # Layer 5: Synthesis
            status_text.markdown("🎯 **Layer 5:** Synthesizing final response...")
            progress_bar.progress(90)
            time.sleep(0.3)
            
            final_response = synthesize_final_response(user_input, step_results)
            
            status_text.markdown("✅ **Complete!**")
            progress_bar.progress(100)
            
            # Display final response
            with result_container:
                st.markdown("### 🎉 Final Response")
                st.markdown(f">{final_response}")
                
                # Cost comparison
                baseline = 0.24
                cascade_cost = st.session_state.total_cost / (st.session_state.queries_processed + 1)
                savings_pct = ((baseline - cascade_cost) / baseline) * 100
                
                st.markdown(f"""
                <div class="savings-highlight">
                    <p class="savings-value">{savings_pct:.1f}%</p>
                    <p class="savings-label">Cost Savings vs GPT-4 Baseline</p>
                </div>
                """, unsafe_allow_html=True)
            
            # Update metrics
            st.session_state.queries_processed += 1
        
        # Add assistant message
        st.session_state.messages.append({"role": "assistant", "content": final_response})
        
        # Rerun to update display
        st.rerun()
    
    def display_cost_comparison(self):
        """Display cost comparison chart."""
        with st.expander("💰 Cost Analysis"):
            st.markdown("""
            ### Cascade vs Baseline Comparison
            
            | Metric | Baseline (GPT-4) | Cascade (Hybrid) | Improvement |
            |--------|------------------|------------------|-------------|
            | Total Cost | $0.24/query | $0.0158/query | **93.38% Savings** |
            | Avg Latency | 1.44s | 15.00s | +940% (tradeoff) |
            | SLM Route Rate | 0% | 80% | **80% cheap calls** |
            
            **Key Insight:** By routing 80% of subtasks to cheaper SLMs (Llama-3-8B) 
            and only escalating complex tasks to LLMs (Llama-3-70B), Cascade achieves 
            massive cost savings with minimal quality impact.
            """)
    
    def display_sidebar(self):
        """Display sidebar with additional info."""
        with st.sidebar:
            st.markdown("### ℹ️ About")
            st.markdown("""
            **Cascade** is a research artifact demonstrating cost-efficient LLM orchestration.
            
            **Key Features:**
            - 5-layer hierarchical processing
            - Dynamic model routing
            - 93% cost savings vs baseline
            - Real-time metrics dashboard
            
            **Technologies:**
            - Llama-3 (8B/70B) via Groq
            - Streamlit dashboard
            - LangChain integration
            """)
            
            st.markdown("---")
            st.markdown("### 📚 Resources")
            st.markdown("- [GitHub Repo](https://github.com/ARYAN2302/Cascade)")
            st.markdown("- [Research Paper](https://github.com/ARYAN2302/Cascade/blob/main/paper/Cascade_Report.pdf)")
            
            st.markdown("---")
            st.markdown("### ⚙️ Settings")
            
            if st.button("🗑️ Clear Chat"):
                st.session_state.messages = []
                st.rerun()
            
            if st.button("🔄 Reset Metrics"):
                st.session_state.total_cost = 0.0
                st.session_state.queries_processed = 0
                st.session_state.slm_usage = 0
                st.session_state.llm_usage = 0
                st.rerun()
    
    def run(self):
        """Run the dashboard."""
        # Display sidebar
        self.display_sidebar()
        
        # Display header
        self.display_header()
        
        # Display metrics
        self.display_metrics_panel()
        
        # Display architecture
        self.display_architecture()
        
        # Display demo section
        self.display_demo_section()
        
        # Display chat interface
        self.display_chat_interface()
        
        # Display cost comparison
        self.display_cost_comparison()


def main():
    """Main entry point."""
    dashboard = CascadeDashboard()
    dashboard.run()


if __name__ == "__main__":
    main()
