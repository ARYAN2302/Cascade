"""Streamlit Dashboard for Cascade Framework visualization."""
import streamlit as st
from main import CascadeSystem

st.set_page_config(page_title="Cascade Framework", layout="wide")
st.title("🌊 Cascade: Hierarchical Agent Orchestration")
st.markdown("**Layer 1-5 Visualization Dashboard**")

if "system" not in st.session_state:
    st.session_state.system = CascadeSystem()
if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:
    st.header("💬 Interaction Loop")
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
    user_input = st.chat_input("Enter a complex task...")

col1, col2 = st.columns([1, 1])

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.sidebar:
        with st.chat_message("user"):
            st.markdown(user_input)

    with col1:
        st.subheader("🧠 Cognitive Architecture")
        status = st.status("Processing...", expanded=True)
        
        status.write("🔍 **Layer 1: Profiling...**")
        from interpreter import profile_task
        profiler_data = profile_task(user_input)
        st.json(profiler_data)
        
        status.write("🗺️ **Layer 2: Planning...**")
        from planner import generate_plan
        plan = generate_plan(profiler_data)
        st.dataframe(plan)
        
        status.update(label="Planning Complete", state="running")

    with col2:
        st.subheader("⚙️ Execution Trace")
        from executor import execute_step
        from refiner import refine_output
        from memory import MemoryManager
        
        memory = MemoryManager()
        
        for step in plan:
            with st.expander(f"Step {step['id']}: {step['step']}", expanded=True):
                st.markdown(f"**Router Decision:** `{step.get('assigned_model')}`")
                exec_res = execute_step(step)
                st.info(f"**Raw Output:** {exec_res['result']}")
                
                final_out = refine_output(step, exec_res['result'])
                if final_out != exec_res['result']:
                    st.warning(f"**QA Correction:** {final_out}")
                else:
                    st.success("**QA Passed**")
                    
                memory.save_step_output(step['id'], final_out, {})

    from synthesizer import synthesize_final_response
    final_response = synthesize_final_response(user_input, memory.working_memory)
    
    status.update(label="Complete", state="complete")
    
    st.session_state.messages.append({"role": "assistant", "content": final_response})
    with st.sidebar:
        with st.chat_message("assistant"):
            st.markdown(final_response)