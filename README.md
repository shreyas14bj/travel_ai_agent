# 🌍 Travel AI — Travel Intelligence Agent

> **An AI-powered Travel Planning & Tourism Intelligence Platform built with Machine Learning, Retrieval-Augmented Generation (RAG), and Generative AI.**

Travel AI brings destination discovery, travel recommendations, forecasting, personalized planning, and knowledge-grounded tourism assistance into a single intelligent application.

The platform combines traditional **Machine Learning** with modern **Generative AI + RAG** to help users explore tourism information, ask natural-language questions, and receive responses grounded in a structured tourism knowledge base.

---

## ✨ What is Travel AI?

Travel planning often requires users to search across multiple sources for:

- 🌍 Destination information
- 🏛️ Attractions
- 🎯 Activities
- 🏨 Hotel policies
- 🚗 Transportation
- 🍽️ Food and dining
- 🌦️ Weather and climate
- 💰 Budget information
- 🧳 Trip planning
- 🛡️ Travel safety

**Travel AI** brings these capabilities together through an AI-powered tourism assistant.

The application provides a modern Streamlit interface where users can ask questions in natural language and explore retrieved knowledge supporting the generated response.

---

# 🖥️ Application Experience

The application is designed as a production-style AI workspace rather than a simple chatbot.

### Main capabilities

| Capability | Description |
|---|---|
| 💬 **AI Assistant** | Ask natural-language tourism questions |
| 🧭 **Destination Discovery** | Explore tourism destinations and information |
| 🏨 **Hotel Intelligence** | Understand hotel policies and accommodation information |
| ✈️ **Travel Planning** | Get tourism-focused planning assistance |
| 🎒 **Activity Discovery** | Explore attractions and activities |
| 💰 **Budget Travel** | Ask about budget-friendly travel planning |
| 📚 **Knowledge Sources** | Inspect retrieved RAG documents |
| 🕘 **Conversation History** | Review questions and generated responses |
| ⚙️ **RAG System** | Monitor the underlying knowledge pipeline |
| 🔄 **Vector Database Rebuild** | Refresh the knowledge index when source data changes |

---

# 🎯 Project Objectives

The main objectives of the project are:

1. Analyze customer travel preferences and behavior.
2. Forecast future travel bookings and revenue.
3. Recommend suitable travel options based on customer preferences.
4. Build a tourism-focused RAG chatbot.
5. Provide reliable destination and travel information from a structured knowledge base.
6. Generate personalized travel planning assistance.
7. Provide a modern AI-agent-style user experience.
8. Extend the system toward a multi-agent travel architecture.

---

# 🏗️ Project Architecture

The project follows a sprint-based development approach and combines data science, machine learning, recommendation systems, RAG, and generative AI.

```text
                         ┌─────────────────────────┐
                         │       User Query        │
                         └────────────┬────────────┘
                                      │
                                      ▼
                         ┌─────────────────────────┐
                         │       Travel AI         │
                         │    Travel AI Agent      │
                         └────────────┬────────────┘
                                      │
                 ┌────────────────────┼────────────────────┐
                 │                    │                    │
                 ▼                    ▼                    ▼
        ┌────────────────┐   ┌────────────────┐   ┌────────────────┐
        │ Recommendation │   │  RAG Tourism   │   │ Travel Planning│
        │     Engine     │   │    Assistant   │   │    Assistance  │
        └───────┬────────┘   └───────┬────────┘   └───────┬────────┘
                │                    │                    │
                │                    ▼                    │
                │           ┌─────────────────┐           │
                │           │ Knowledge Base  │           │
                │           └────────┬────────┘           │
                │                    │                    │
                │                    ▼                    │
                │           ┌─────────────────┐           │
                │           │ Vector Database │           │
                │           └────────┬────────┘           │
                │                    │                    │
                └────────────────────┼────────────────────┘
                                     │
                                     ▼
                         ┌─────────────────────────┐
                         │ Personalized / Grounded│
                         │       AI Response       │
                         └─────────────────────────┘
```

---

# 🚀 Project Sprints

## Sprint 1 — Exploratory Data Analysis

Performed exploratory analysis on customer travel preference data.

### Activities

- Dataset understanding
- Data cleaning
- Missing-value analysis
- Statistical analysis
- Customer segmentation
- Travel preference analysis
- Data visualization
- Relationship analysis between travel attributes

### Dataset Features

The customer dataset contains attributes such as:

- Customer ID
- Age
- Country
- Travel Style
- Budget Level
- Family Size
- Preferred Climate
- Trip Duration
- Average Spend
- Favorite Activity
- Preferred Hotel Type
- Past Rating
- Preferred Destination

---

# 📈 Sprint 2 — Sales Forecasting

Developed a time-series forecasting component to analyze travel bookings and revenue.

### Dataset

The forecasting dataset contains:

- Date
- Destination
- Bookings
- Revenue (USD)

### Key Activities

- Time-series data preparation
- Trend analysis
- Booking analysis
- Revenue analysis
- Train/test splitting
- Baseline forecasting
- Naive forecasting
- Model evaluation

The forecasting component provides a baseline for understanding future booking and revenue trends.

---

# 🤖 Sprint 3 — Recommendation Engine

Developed a Machine Learning-based recommendation component using customer travel preferences.

The recommendation engine analyzes customer characteristics and preferences to predict suitable travel choices and generate recommendations.

### Input Features

Examples include:

- Age
- Country
- Travel Style
- Budget Level
- Family Size
- Preferred Climate
- Trip Duration
- Average Spend
- Favorite Activity
- Preferred Hotel Type
- Past Rating

### Machine Learning

The project evaluates classification-based approaches for predicting customer travel preferences and generating recommendations.

---

# 📚 Sprint 4 — RAG Tourism AI Assistant

The RAG assistant is the core knowledge-grounded AI component of the application.

Instead of relying only on a language model's internal knowledge, the system retrieves relevant information from the tourism knowledge base before generating an answer.

This approach allows the assistant to provide responses based on the project's available tourism documents.

## 🔎 RAG Pipeline

```text
User Question
      ↓
Query Processing
      ↓
Embedding Generation
      ↓
Vector Search
      ↓
Relevant Documents
      ↓
Context + User Question
      ↓
LLM
      ↓
Grounded Response
```

### Knowledge Base Categories

The tourism knowledge base is organized around:

- 🌍 Destination Information
- 🏛️ Attractions
- 🎯 Things to Do & Activities
- 🏨 Hotel Policies
- 🚗 Transportation
- 🍽️ Food & Dining
- 🌦️ Weather & Climate
- 🧳 Travel Planning
- 🧑‍🤝‍🧑 Family & Group Travel
- 👴 Elderly-Friendly Travel
- 💰 Budget Planning
- 🛡️ Travel Safety
- ❓ Frequently Asked Questions
- 🚨 Real-Life Travel Problem Solving

### RAG Principles

The assistant is designed to:

- Retrieve relevant information before answering.
- Ground responses in the available knowledge base.
- Reduce unnecessary hallucination.
- Clearly indicate when information is unavailable.
- Handle tourism-related questions using structured documents.

---

# 💬 AI Assistant Experience

Travel AI provides a conversational interface for interacting with the tourism knowledge base.

Users can ask questions such as:

```text
What are the top attractions in this destination?

What activities are suitable for families?

What is the best time to visit?

What transportation options are available?

What are the hotel check-in and cancellation policies?

Can you suggest a 3-day itinerary?

What activities are suitable for elderly travelers?

What can I do on a limited budget?

What should I know about local customs?

What should I do if my hotel check-in is delayed?
```

The assistant processes the question through the RAG pipeline and presents the resulting response through the Streamlit application.

---

# 📚 Retrieved Knowledge & Transparency

A key part of the new application experience is the **Knowledge Sources** section.

After an AI response is generated, users can inspect the retrieved knowledge chunks used by the RAG pipeline.

The source view can expose information such as:

- Source document
- Domain
- Destination / entity
- Retrieval score
- Retrieved document content

This provides greater transparency into the information retrieved by the tourism assistant.

---

# 🕘 Conversation History

The application maintains the current session's conversation history.

Users can review:

- Previous questions
- Generated answers
- Number of retrieved knowledge chunks

The conversation can also be cleared from the application interface.

---

# ⚙️ RAG System & Knowledge Base Management

The application includes a system section for inspecting the RAG infrastructure.

The system interface can display RAG status information and provides a **Vector Database Rebuild** operation.

The rebuild workflow is intended for situations where the underlying tourism source documents have changed.

The application can report:

- Current source chunks
- New vectors added
- Stale vectors removed
- Vector database count

---

# 🧠 Technology Stack

## Programming

- Python

## Data Science & Machine Learning

- Pandas
- NumPy
- Scikit-learn
- Time Series Forecasting
- Classification / Recommendation Models

## Generative AI

- Large Language Models (LLMs)
- Retrieval-Augmented Generation (RAG)
- LangChain

## Embeddings

- Hugging Face Sentence Transformers
- `sentence-transformers/all-MiniLM-L6-v2`

## Vector Database

- ChromaDB

## Application

- Streamlit

## Development

- Jupyter Notebook
- Git
- GitHub

---

# 📁 Project Structure

```text
Travel_AI_Agent/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── documents/
│   ├── tourism_guides/
│   ├── hotel_policies/
│   └── travel_advisories/
│
├── notebooks/
│   ├── sprint_1_eda.ipynb
│   ├── sprint_2_forecasting.ipynb
│   ├── sprint_3_recommendation.ipynb
│   └── sprint_4_rag_chatbot.ipynb
│
├── src/
│   ├── data/
│   ├── forecasting/
│   ├── recommendation/
│   ├── rag/
│   └── utils/
│
├── vector_db/
│
├── app.py
├── requirements.txt
└── README.md
```

> The exact folder names may vary depending on the final project structure in the repository.

---

# 🔐 Data & API Security

Sensitive credentials and API keys are **not included in this repository**.

Environment variables or secure configuration should be used for confidential credentials.

Example:

```text
API_KEY=your_api_key
BASE_URL=your_model_endpoint
MODEL_NAME=your_model_name
```

> **Never commit real API keys, passwords, tokens, or confidential MaaS credentials to GitHub.**

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/Mohanreddy-8074/Travel_AI_Agent.git
cd Travel_AI_Agent
```

## 2. Create a Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Application

Launch the Streamlit application with:

```bash
streamlit run app.py
```

The application will open in your browser.

### Application Flow

```text
Launch Application
       ↓
Travel AI Dashboard
       ↓
Ask Tourism Question
       ↓
RAG Retrieval
       ↓
Knowledge-Grounded Answer
       ↓
Inspect Retrieved Sources
       ↓
Continue Conversation
```

---

# 🎨 Production-Style UI

The Streamlit application is designed around a modern AI-agent dashboard experience.

### Interface sections

```text
┌───────────────────────────────────────────────────────────────┐
│ 🌍 Travel AI                                                  │
│ Travel Intelligence Platform                                  │
├───────────────┬───────────────────────────────────────────────┤
│ Explore       │ Travel smarter. Explore deeper.               │
│               │                                               │
│ 🏝️ Destinations│  AI Assistant                                │
│ 🏨 Hotels      │  ┌───────────────────────────────────────┐   │
│ ✈️ Planning    │  │ Ask anything about tourism...         │   │
│ 🎒 Activities  │  └───────────────────────────────────────┘   │
│ 💰 Budget      │                                               │
│ ⚠️ Advisory    │  ✨ Ask Travel AI                            │
│               │                                               │
│ Session       │  ───────────────────────────────────────────  │
│ Questions     │  🤖 AI Response                               │
│               │                                               │
│ Clear Chat    │  📚 Retrieved Knowledge                       │
└───────────────┴───────────────────────────────────────────────┘
```

The UI separates the primary AI experience from supporting operational views such as retrieved knowledge, conversation history, and RAG system status.

---

# 🔮 Future Enhancements

The project can be extended with:

- 🤝 Multi-Agent Travel Architecture
- 🏨 Hotel Agent
- 🚗 Transport Agent
- 🎯 Attraction Agent
- 💰 Budget Planner Agent
- 🧳 Automated Itinerary Optimization
- 📊 Model Monitoring
- 📈 RAG Evaluation
- ⭐ User Feedback System
- 🔍 Improved Semantic Search
- 🌐 Multilingual Travel Assistance
- 📱 Improved Responsive UI

---

# 📊 Project Outcome

This project demonstrates an end-to-end approach to building an intelligent travel solution by combining:

```text
Data
  ↓
Machine Learning
  ↓
Forecasting
  ↓
Recommendation
  ↓
RAG
  ↓
LLM
  ↓
Travel Assistance
  ↓
AI-Agent Experience
```

The project provides practical experience in developing AI applications that combine traditional Machine Learning with modern Generative AI and Retrieval-Augmented Generation techniques.

---

# 👥 Team Project

**Project:** Travel AI / Travel AI Agent  
**Domain:** Travel & Tourism  
**Technologies:** Python, Machine Learning, RAG, LangChain, LLMs, ChromaDB, Streamlit

---

# 📜 License

This project is intended for educational and project demonstration purposes.

---

# ⭐ Acknowledgement

This project was developed as part of an AI/ML project focused on applying **Machine Learning, Generative AI, and RAG technologies to real-world travel and tourism use cases**.

If you find this project useful, consider giving the repository a ⭐.
