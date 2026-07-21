# 🤖 Project-01: Local AI Chatbot

![Python](https://img.shields.io/badge/Python-3.12+-blue)
![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-green)
![Model](https://img.shields.io/badge/Model-Qwen3%208B-orange)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

## 📖 Project Overview

This project is a **Local AI Chatbot** built using **Python**, **Ollama**, and the **Qwen3:8B** Large Language Model.

The chatbot runs **100% locally** on your computer, allowing you to interact with an LLM without relying on cloud APIs.

This is **Project-01** in my AI Engineering learning journey.

---

# 🚀 Features

- ✅ Local Large Language Model (Qwen3:8B)
- ✅ Interactive terminal chatbot
- ✅ Conversation memory
- ✅ Offline after model download
- ✅ Python-based implementation
- ✅ Fast local inference using Ollama

---

# 🛠️ Tech Stack

- Python
- Ollama
- Qwen3:8B
- VS Code
- Git
- GitHub

---

# 📂 Project Structure

```
Project-01-Local-Chatbot
│
├── chatbot.py
├── requirements.txt
├── README.md
├── .gitignore
└── .venv/
```

---

# ⚙️ Prerequisites

Before running this project, install:

- Python 3.12+
- Ollama

Download Ollama:

https://ollama.com/download

---

# 📥 Install the Model

Download the Qwen3 8B model:

```bash
ollama pull qwen3:8b
```

Verify:

```bash
ollama list
```

Expected output:

```
qwen3:8b
```

---

# 📦 Install Python Packages

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it.

### Windows

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Project

```bash
python chatbot.py
```

---

# 💬 Example

```
==================================================
🤖 Local AI Chatbot (Qwen3)
Type 'exit' to quit
==================================================

You: Hello

AI:
Hello! How can I help you today?

You: My name is Mallikarjuna.

AI:
Nice to meet you!

You:
What is my name?

AI:
Your name is Mallikarjuna.
```

---

# 🧠 How It Works

```
User
   │
   ▼
Python Application
   │
   ▼
Conversation History
   │
   ▼
Ollama
   │
   ▼
Qwen3:8B
   │
   ▼
AI Response
```

---

# 📚 What I Learned

During this project I learned:

- Running LLMs locally
- Ollama installation
- Python Ollama SDK
- Chat completion API
- Maintaining conversation history
- Virtual environments
- Git & GitHub basics

---

# 🔮 Future Improvements

- Streaming responses
- Chat history in JSON
- Streamlit Web UI
- RAG (Retrieval-Augmented Generation)
- AI Agents
- Multi-Agent Systems
- Voice-enabled chatbot

---

# 📌 Repository

```text
Project-01: Local AI Chatbot
```

---

# 👨‍💻 Author

**V karthik**

GitHub:
https://github.com/karthikv22

LinkedIn:
(Add your LinkedIn profile here)

---

# ⭐ If you like this project

Please consider giving it a ⭐ on GitHub.

It motivates me to continue building more AI Engineering projects.
