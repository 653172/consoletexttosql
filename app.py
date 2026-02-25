import streamlit as st
from llm import generate_sql

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI SQL Generator",
    page_icon="🧠",
    layout="centered"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

body {
    background-color: #0e1117;
}

.main-title {
    font-size: 42px;
    font-weight: 700;
    text-align: center;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    color: #9ca3af;
    margin-bottom: 30px;
}

.user-box {
    background-color: #1f2937;
    padding: 15px;
    border-radius: 10px;
    margin-bottom: 10px;
}

.sql-box {
    background-color: #111827;
    padding: 15px;
    border-radius: 10px;
    margin-bottom: 25px;
    border: 1px solid #374151;
}

.stButton > button {
    background-color: #2563eb;
    color: white;
    border-radius: 8px;
    padding: 8px 18px;
    border: none;
}

.stButton > button:hover {
    background-color: #1d4ed8;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown('<div class="main-title">🧠 AI SQL Code Generator</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Generate SQL from natural language instantly</div>', unsafe_allow_html=True)

# ---------------- SESSION STATE ----------------
if "history" not in st.session_state:
    st.session_state.history = []

# ---------------- INPUT AREA ----------------
st.divider()

question = st.text_input(
    "",
    placeholder="e.g. Create a table with 5 employees",
    label_visibility="collapsed"
)

col1, col2 = st.columns([1, 1])

with col1:
    generate = st.button("Generate SQL")

with col2:
    clear = st.button("Clear History")

# ---------------- GENERATE LOGIC ----------------
if generate and question.strip() != "":
    with st.spinner("Generating SQL..."):
        sql_query = generate_sql(question)

    st.session_state.history.append({
        "question": question,
        "sql": sql_query
    })

# ---------------- CLEAR LOGIC ----------------
if clear:
    st.session_state.history = []
    st.rerun()

# ---------------- DISPLAY HISTORY ----------------
for item in reversed(st.session_state.history):

    st.markdown(
        f'<div class="user-box"><b>🧑 You:</b><br>{item["question"]}</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="sql-box"><b>🤖 SQL:</b></div>',
        unsafe_allow_html=True
    )

    st.code(item["sql"], language="sql")
