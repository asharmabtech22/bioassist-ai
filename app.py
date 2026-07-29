import streamlit as st

st.set_page_config(page_title="BioAssist AI")

st.title("🧬 BioAssist AI")

st.write(
    "An open-source AI toolkit for biotechnology and bioinformatics students."
)

task = st.selectbox(
    "Choose a task",
    [
        "Literature Review",
        "Paper Summary",
        "FASTA Analysis",
        "Experiment Design",
    ],
)

if st.button("Start"):
    st.success(f"You selected: {task}")
