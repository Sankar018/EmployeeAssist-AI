import streamlit as st
from rag import create_rag_chain
import time

# Page configuration
st.set_page_config(
    page_title="TCS Employee Support Chatbot",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for unique & attractive UI
st.markdown("""
<style>
    /* Main background gradient */
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #0f172a 100%);
        color: #e2e8f0;
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1e293b 0%, #0f172a 100%);
        border-right: 1px solid #334155;
    }
    
    /* Title styling */
    .main-title {
        font-size: 2.8rem;
        font-weight: 800;
        background: linear-gradient(90deg, #38bdf8, #818cf8, #c084fc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0.2rem;
        letter-spacing: -0.5px;
    }
    
    .sub-title {
        text-align: center;
        color: #94a3b8;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }
    
    /* Chat message styling */
    .stChatMessage {
        background-color: rgba(30, 41, 59, 0.7) !important;
        border: 1px solid #334155 !important;
        border-radius: 16px !important;
        padding: 1rem !important;
        margin-bottom: 1rem !important;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.3);
    }
    
    /* User message accent */
    [data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) {
        border-left: 4px solid #38bdf8 !important;
    }
    
    /* Assistant message accent */
    [data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-assistant"]) {
        border-left: 4px solid #818cf8 !important;
    }
    
    /* Input box */
    .stChatInput {
        border-radius: 16px !important;
    }
    
    /* Buttons */
    .stButton > button {
        background: linear-gradient(90deg, #3b82f6, #8b5cf6);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.6rem 1.2rem;
        font-weight: 600;
        transition: all 0.3s ease;
        width: 100%;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 15px rgba(59, 130, 246, 0.3);
    }
    
    /* Metric cards in sidebar */
    .metric-card {
        background: rgba(30, 41, 59, 0.8);
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 1rem;
        margin-bottom: 1rem;
        text-align: center;
    }
    
    .metric-value {
        font-size: 1.8rem;
        font-weight: 700;
        color: #38bdf8;
    }
    
    .metric-label {
        font-size: 0.85rem;
        color: #94a3b8;
    }
    
    /* Example question chips */
    .example-chip {
        background: rgba(59, 130, 246, 0.15);
        border: 1px solid #3b82f6;
        border-radius: 20px;
        padding: 0.5rem 1rem;
        margin: 0.3rem;
        display: inline-block;
        font-size: 0.9rem;
        color: #93c5fd;
        cursor: pointer;
        transition: all 0.2s;
    }
    
    .example-chip:hover {
        background: rgba(59, 130, 246, 0.3);
        transform: scale(1.02);
    }
    
    /* Header badge */
    .badge {
        display: inline-block;
        background: linear-gradient(90deg, #22c55e, #16a34a);
        color: white;
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 600;
        margin-left: 0.5rem;
        vertical-align: middle;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        color: #64748b;
        font-size: 0.85rem;
        margin-top: 2rem;
        padding-top: 1rem;
        border-top: 1px solid #334155;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

</style>
""", unsafe_allow_html=True)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "rag_chain" not in st.session_state:
    with st.spinner("🔄 Ruko Zaaraa Saabar Karooo..."):
        st.session_state.rag_chain = create_rag_chain()
if "query_count" not in st.session_state:
    st.session_state.query_count = 0

# Sidebar
with st.sidebar:
    st.markdown("### 🏢 Total Corporate Support (TCS)")
    st.markdown("---")
    
    st.markdown("""
    <div class="metric-card">
        <div class="metric-value">{}</div>
        <div class="metric-label">Questions Answered</div>
    </div>
    """.format(st.session_state.query_count), unsafe_allow_html=True)
    
    st.markdown("### 📌 Quick Topics")
    st.markdown("""
    - 🏠 Work From Home Policy  
    - 🏖️ Leave & Holidays  
    - 💰 Salary & Benefits  
    - 📋 HR Procedures  
    - 🛡️ Company Policies  
    - 🎯 Performance Reviews  
    """)
    
    st.markdown("---")
    st.markdown("### 💡 Try asking")
    
    example_questions = [
        "How many WFH days are allowed per month?",
        "How do I apply for casual leave?",
        "What is the notice period policy?",
        "What are the working hours?"
    ]
    
    for q in example_questions:
        if st.button(q, key=q):
            st.session_state.pending_question = q
            st.rerun()
    
    st.markdown("---")
    st.markdown("""
    <div style="text-align:center; color:#64748b; font-size:0.8rem;">
        Powered by RAG + Google Gemini<br>
        Official TCS Documents Only
    </div>
    """, unsafe_allow_html=True)

# Main content
st.markdown('<h1 class="main-title">TCS Employee Support</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Your intelligent HR assistant • Ask anything about company policies <span class="badge">AI Powered</span></p>', unsafe_allow_html=True)

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"], avatar="🧑‍💼" if message["role"] == "user" else "🤖"):
        st.markdown(message["content"])

# Handle example question click
if "pending_question" in st.session_state:
    prompt = st.session_state.pending_question
    del st.session_state.pending_question
else:
    prompt = st.chat_input("Ask about leave, WFH, policies, benefits...")

if prompt:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="🧑‍💼"):
        st.markdown(prompt)
    
    # Generate response
    with st.chat_message("assistant", avatar="🤖"):
        message_placeholder = st.empty()
        full_response = ""
        
        with st.spinner("🔍 Searching company documents..."):
            try:
                chat_history = ""

                for message in st.session_state.messages[:-1]:
                    role = "Employee" if message["role"] == "user" else "Assistant"
                    chat_history += f"{role}: {message['content']}\n"

                response = st.session_state.rag_chain.invoke({
                    "question": prompt,
                    "chat_history": chat_history
                })
                
                # Typing effect for better UX
                for chunk in response.split():
                    full_response += chunk + " "
                    time.sleep(0.03)
                    message_placeholder.markdown(full_response + "▌")
                
                message_placeholder.markdown(full_response)
                
            except Exception as e:
                full_response = f"⚠️ Sorry, I encountered an issue while processing your request.\n\n**Error:** {str(e)}\n\nPlease try again or rephrase your question."
                message_placeholder.markdown(full_response)
    
    # Save assistant response
    st.session_state.messages.append({"role": "assistant", "content": full_response})
    st.session_state.query_count += 1
    st.rerun()

# Footer
st.markdown("""
<div class="footer">
    © 2026 Total Corporate Support (TCS) • Employee Support Chatbot<br>
    Answers are generated from official company documents using Retrieval-Augmented Generation
</div>
""", unsafe_allow_html=True)