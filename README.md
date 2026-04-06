# WeatherTwin 🌤️ & AI Public Health Intelligence

**GenAI-Powered Climate Intelligence & Substance Abuse Risk Detection Command Center**

WeatherTwin is a multi-dimensional analysis platform providing personalized climate insights and advanced community health surveillance. It uses Large Language Models (LLMs) combined with Retrieval-Augmented Generation (RAG) to translate complex climate, agricultural, and clinical data into actionable explanations.

> **NRT AI Challenge Submission**  
> **Challenge 1:** AI for Substance Abuse Risk Detection from Social Signals  
> **Team:** CloudMind  
> **Team Members:** Harsha Sri Neeriganti, Sayush Maharjan  
> **Demo Video:** [https://youtu.be/IUzAAvJeHZE](https://youtu.be/IUzAAvJeHZE)  
> **Live App:** [https://weathertwin-fjyoanxtvya7tvmmdfppsy.streamlit.app/](https://weathertwin-fjyoanxtvya7tvmmdfppsy.streamlit.app/)

---

## 🚀 The WeatherTwin Command Center (Features)

| Tab / Feature | Description |
| :--- | :--- |
| **🏥 Public Health** | **NRT Challenge Module**: Statistical spike detection, seasonal substance pie charts, and "Why and How" AI reasoning for overdose risks. |
| **🌤️ Dashboard** | Real-time weather, 5-year historical norms (Z-scores), and proactive RAG-powered AI insights on clothing and activity. |
| **🔄 Compare** | Side-by-side analysis of two cities with shared interactive maps and comparative weather metrics. |
| **🧳 Travel Planner** | AI-driven weather-aware itinerary generation for global travel planning. |
| **🌱 Agriculture** | Specialized irrigation advice, frost alerts, and soil moisture insights for farmers and gardeners. |
| **🏥 Health Weather** | Personalized health advice relating weather to asthma, allergies, and cardiovascular safety. |
| **🤖 Smart Rec** | AI-suggested activities based on current environmental conditions and user preferences. |
| **🌋 Simulator** | Climate simulation module visualizing future environmental scenarios based on current trends. |
| **📰 Climate News** | Real-time curated news feed on climate change and environmental policy. |
| **🖥️ Monitoring** | Live system health dashboard tracking LLM latency, API status, and database performance. |

---

## 🎯 Problem Definitions
1.  **The Information Gap**: Traditional weather apps show numbers; WeatherTwin provides **reasoning**.
2.  **The Public Health "Silent Signal"**: Substance abuse surges are often buried in dense datasets. CPHI provides **automated detection** and **explainable AI** for localized response.

## 📊 Dataset & Preprocessing
- **Open-Meteo & OpenWeatherMap**: Real-time and 5-year historical climate data.
- **CDC Provisional Overdose Deaths**: Monthly state-level fatalities (Socrata API).
- **SAMHSA Facility Locator**: A national database of recovery and treatment centers.
- **Processing**: Real-time mapping of diverse data streams into a persistent SQLite database.

## 🧠 Model & System Description
- **Intelligence**: Llama 3.3 70B via Groq API (High-speed inference).
- **Temporal Analysis**: 3-month rolling baseline for statistical surge detection.
- **RAG Architecture**: Dynamic context injection for evidence-based AI reasoning.

## 📂 Modular Code Structure
```
├── streamlit_app.py           # Unified Dashboard Interface
├── backend/                   # Core Services (LLM, DB, Weather)
├── features/                  # Specialized Analysis Modules
│   ├── public_health/         # NRT Challenge Module
│   ├── travel_planner/        # Travel Itinerary Intelligence
│   ├── agriculture/           # Agricultural Analytics
│   ├── health_weather/        # Personal Health Guidance
│   └── climate_simulator/     # Future Projections
└── data/                      # Persistent Knowledge Base
```

## 🛠️ Setup & Execution Instructions

1.  **Clone & Install**
    ```bash
    pip install -r requirements.txt
    ```
2.  **Configure Environment**
    Add your `GROQ_API_KEY` to the `.env` file.
3.  **Run Application**
    ```bash
    streamlit run streamlit_app.py
    ```

---
**Team CloudMind** | *Final Submission for NRT AI Challenge (April 2026)*
