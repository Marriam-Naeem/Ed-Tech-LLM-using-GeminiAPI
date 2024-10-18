import streamlit as st
from LLMhelper import (
    create_vector_db, generate_answer, get_relevant_docs, 
    generate_response, make_rag_prompt
)

# --- Page Configuration ---
st.set_page_config(
    page_title="AskIt: Ask Away Anything 🎓", 
    page_icon="🎓", 
    layout="centered", 
    initial_sidebar_state="expanded"
)

# --- Custom Styling ---
st.markdown("""
    <style>
        /* Background and General Styles */
        .main { background-color: #1e1e1e; }
        
        /* Title and Subtitle Styling */
        .title { 
            font-size: 48px; font-weight: 700; 
            color: #f0f0f0; text-align: center; 
            margin-top: 20px; 
        }
        .subtitle { 
            font-size: 22px; color: #d3d3d3; 
            margin-bottom: 40px; text-align: center; 
        }

        /* Button Styling */
        .stButton {
            display: flex;
            justify-content: center;
            margin-bottom: 20px 0; /* Add some margin above and below */
        }
        .stButton button { 
            background-color: #1ABC9C; 
            color: white; font-weight: bold; 
            border-radius: 8px; padding: 10px 20px; 
        }

        /* Question Header Styling */
        .question-header { 
            color: #f4f4f4; font-size: 28px;
            margin: 0;  /* Remove margin */
            padding: 0; /* Remove padding */
        }

        /* Text Input Styling */
        .stTextInput > div { 
            margin: 0;  /* Remove margin */
            padding: 0; /* Remove padding */
        }

        /* Answer Section Styling */
        .answer-container { 
            background-color: #2c2c2c; 
            padding: 20px; border-radius: 10px; 
        }
        .answer-header { 
            color: #f4f4f4; font-size: 28px; 
            margin-bottom: 10px; 
        }
        .answer-text { 
            color: #e0e0e0; font-size: 18px; 
        }
    </style>
""", unsafe_allow_html=True)

# --- Title and Subtitle ---
st.markdown("<h1 class='title'>AskIt: Ask Away Anything 🎓</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Explore knowledge effortlessly with smart Q&A at your fingertips</p>", unsafe_allow_html=True)

# --- Knowledgebase Button ---
st.markdown("<div class='stButton'>", unsafe_allow_html=True)
if st.button("Create Knowledgebase 🗂️"):
    with st.spinner("Setting up the knowledgebase..."):
        create_vector_db()
        st.success("Knowledgebase created successfully!")
st.markdown("</div>", unsafe_allow_html=True)

# --- User Input: Question ---
st.markdown("<h2 class='question-header'>Question:</h2>", unsafe_allow_html=True)
question = st.text_input("", placeholder="Type your question here...")

if question:
    with st.spinner("Generating answer..."):
        response = generate_answer(query=question)

        # Displaying the Answer
        st.markdown("<h2 class='answer-header'>Answer:</h2>", unsafe_allow_html=True)
        st.markdown(f"<p class='answer-text'>{response}</p>", unsafe_allow_html=True)
