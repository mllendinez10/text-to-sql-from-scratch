"""
Streamlit app for the Text-to-SQL pipeline.
"""

import streamlit as st
import time

from main import run_pipeline


# --------------------------------------------------
# Page configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Text-to-SQL Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("Text-to-SQL Assistant")
st.caption("Ask questions about the product data")


# --------------------------------------------------
# Initialize chat history for the current session
# --------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []


# --------------------------------------------------
# Display previous messages
# --------------------------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])


# --------------------------------------------------
# User input
# --------------------------------------------------

question = st.chat_input(
    "Ask a question..."
)


# --------------------------------------------------
# Process question
# --------------------------------------------------

if question:

    # Show user message
    with st.chat_message("user"):
        st.write(question)

    # Save user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    # Run Text-to-SQL pipeline
    with st.spinner("Querying database..."):
    
        start_time = time.time()
        
        answer = run_pipeline(question)
        
        elapsed_time = time.time() - start_time
        

    # Show assistant answer and running time
    with st.chat_message("assistant"):
        st.write(answer)
        st.caption(f"Generated in {elapsed_time:.2f} seconds")

    # Save assistant answer
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )
