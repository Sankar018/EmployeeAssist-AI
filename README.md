# 🏢 TCS EmployeeAssist AI

**TCS EmployeeAssist AI** is an AI-powered employee support chatbot designed to answer company policy and workplace-related questions using **Retrieval-Augmented Generation (RAG)**.

The system retrieves relevant information from company policy documents and uses **Google Gemini** to generate contextual, conversational, and employee-friendly responses.

> **TCS = Total Corporate Support**

---

## ✨ Features

* 🤖 **AI-Powered Employee Assistant**
  Ask questions about company policies using natural language.

* 📚 **Retrieval-Augmented Generation (RAG)**
  Retrieves relevant information from company documents before generating a response.

* 💬 **Conversational Follow-ups**
  Uses previous conversation context to understand follow-up questions.

* 📄 **PDF-Based Knowledge Base**
  Uses company policy documents as the chatbot's primary knowledge source.

* 🔍 **Semantic Document Search**
  Uses ChromaDB for vector-based retrieval of relevant information.

* 🧠 **Google Gemini Integration**
  Generates natural and context-aware responses.

* 👋 **General Conversation Support**
  Handles greetings and basic conversational interactions in addition to policy questions.

* 🖥️ **Interactive Streamlit UI**
  Provides a simple and user-friendly chat interface.

---

## 🏗️ Architecture

```text
                    Employee
                       │
                       ▼
              ┌─────────────────┐
              │  Streamlit UI   │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │  User Question  │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │   RAG Pipeline  │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │    ChromaDB     │
              │ Vector Retrieval│
              └────────┬────────┘
                       │
                 Relevant Context
                       │
                       ▼
              ┌─────────────────┐
              │  Google Gemini  │
              │      LLM        │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │   AI Response   │
              └─────────────────┘
```

---

## 📚 Knowledge Base

The chatbot works with company policy documents covering areas such as:

* Attendance & Working Hours
* Leave Policy
* Work From Home
* Employee Benefits
* Travel Policy
* Expense Reimbursement
* Code of Conduct
* Cyber Security Policy
* Employee Handbook
* Onboarding Policy
* Training & Learning Policy
* VPN & Remote Access
* Password & Access Control
* Laptop & IT Equipment
* Employee Grievance & Complaint
* Company FAQ

---

## 🛠️ Tech Stack

| Technology        | Purpose                                |
| ----------------- | -------------------------------------- |
| **Python**        | Application development                |
| **Google Gemini** | Large Language Model                   |
| **LangChain**     | LLM and RAG integration                |
| **ChromaDB**      | Vector database and semantic retrieval |
| **Streamlit**     | Interactive web interface              |
| **PyPDF**         | PDF document processing                |
| **Embeddings**    | Document vectorization                 |
| **python-dotenv** | Environment variable management        |

---

## 📂 Project Structure

```text
TCS EmployeeAssist AI/
│
├── app.py                 # Streamlit application
├── config.py              # Configuration and environment settings
├── embedding.py           # Embedding generation
├── model.py               # Gemini model configuration
├── pdf_loader.py          # PDF document loading
├── prompt.py              # System and response prompts
├── rag.py                 # RAG pipeline and conversation handling
├── search.py              # Document retrieval and search
├── text_splitter.py       # Document chunking
├── vector_store.py        # ChromaDB vector store
│
├── documents/             # Company policy documents
│
├── requirements.txt       # Python dependencies
├── .env                   # API configuration (not committed)
└── .gitignore
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Sankar018/EmployeeAssist-AI.git
cd EmployeeAssist-AI
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the Gemini API

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_gemini_api_key
```

> ⚠️ **Never commit your `.env` file or expose your API key publicly.**

### 5. Build the vector store

Process the policy documents and create the local ChromaDB vector store using the project's vector-store setup.

### 6. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 💡 Example Questions

Try asking:

```text
How many days of leave can I take?

Can I work from home?

What is the work-from-home policy?

How can I claim travel expenses?

What should I do if I lose my company laptop?

How do I report a workplace grievance?

What are the password requirements?

Can I take one week of leave?
```

### 🔄 Follow-up Questions

The chatbot can also use previous conversation context:

```text
Employee: How many days of leave can I take?

Assistant: [Leave policy response]

Employee: What about during my probation period?

Assistant: [Context-aware follow-up response]
```

---

## 🔐 Security

Sensitive configuration and generated files are excluded from Git using `.gitignore`.

The following should not be committed:

```text
.env
venv/
chroma_db/
```

API credentials should always be stored as environment variables.

---

## 🚀 Future Improvements

* 👤 Employee authentication
* 🗃️ Employee database integration
* 📝 Leave and request submission
* 🔐 Role-based access control
* 📊 Employee interaction analytics
* 📧 Automated notifications
* 🌐 Production deployment
* 🤝 Integration with internal employee services

---

## 👨‍💻 Author

### Sankar Bhunia

**B.Tech — Computer Science & Engineering (AI/ML)**

GitHub: [@Sankar018](https://github.com/Sankar018)

---

## ⭐ Project

**TCS EmployeeAssist AI**
*AI-powered RAG-based Employee Support Assistant*

**TCS — Total Corporate Support**
