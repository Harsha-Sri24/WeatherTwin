# WeatherTwin 🌤️ & AI Public Health Intelligence

**GenAI-Powered Climate Intelligence & Substance Abuse Risk Detection Command Center**

WeatherTwin goes beyond basic forecasts to provide personalized, context-aware weather insights and community health surveillance. It uses Large Language Models (LLMs) combined with Retrieval-Augmented Generation (RAG) to translate complex climate and clinical data into clear, actionable explanations.


> **Team:** CloudMind
> **Team Members:** Harsha Sri Neeriganti, Sayush Maharjan
> **Demo Video:** [https://youtu.be/IUzAAvJeHZE](https://youtu.be/IUzAAvJeHZE)  
> **Live App:** [https://weathertwin-fjyoanxtvya7tvmmdfppsy.streamlit.app/](https://weathertwin-fjyoanxtvya7tvmmdfppsy.streamlit.app/)

---

## 🚀 Key Features

### 🌡️ Climate Intelligence Module
| Feature | Description |
| :--- | :--- |
| **Current Conditions** | Real-time weather with contextual anomaly assessment |
| **Historical Context** | Compare today's weather to 5-year historical norms (Z-scores) |
| **Climate Trends** | Detect warming/cooling trends with automated statistical analysis |
| **AI Insights** | LLM-generated proactive climate intelligence (RAG-powered) |
| **AI Chat** | Conversational Q&A about weather, planning, and climate trends |
| **Interactive Map** | Dynamic location markers and geospatial visualization |

### 🏥 Public Health Module (NRT AI Challenge)
| Feature | Description |
| :--- | :--- |
| **Risk Signal Detection** | Statistical spike detection (1.3x rolling average) to identify surges. |
| **Seasonal Breakdown** | Substance distribution analysis (Pie Charts) by Winter/Spring/Summer/Fall. |
| **"Why and How" AI** | Narrative reasoning explaining climate-driven health triggers. |
| **Resource Locator** | Proximity-based search for 40,000+ SAMHSA treatment facilities. |

---

## 🎯 2. Problem Definition
1.  **The Climate Context Gap**: Traditional weather apps show raw numbers but lack "contextual reasoning" (Historical status and personal impact).
2.  **The Public Health "Silent Signal"**: Substance abuse surges are often buried in reports. CPHI addresses this by providing **automated risk detection** and **explainable AI** to mobilize local resources.

## 📊 3. Dataset & Preprocessing
- **Open-Meteo**: Real-time, forecast, and 5-year historical archived weather.
- **CDC Provisional Overdose Deaths**: Monthly state-level fatalities (Socrata API).
- **SAMHSA Facility Locator**: National database of accredited recovery centers.
- **Normalization**: Synchronizing heterogeneous data sources into a relational SQLite database (`public_health.db`).

## 🧠 4. Model & System Description
- **Statistical Engine**: 3-month rolling average surge detection for local spikes.
- **GenAI Reasoning**: Llama 3.3 70B via Groq with RAG-based context injection for empathetic, data-grounded summaries.
- **Seasonal Analysis**: Mapping death rates to climatic seasons to identify temporal risk factors.

## 🛠️ 5. Setup & Execution Instructions

### Prerequisites
- Python 3.9+
- [Groq API Key](https://console.groq.com)

### Installation
1.  **Clone the Repository**
2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Configure Environment**
    Create a `.env` file in the root directory:
    ```bash
    GROQ_API_KEY=your_key_here
    ```
4.  **Run Application**
    ```bash
    streamlit run streamlit_app.py
    ```

## 🏗️ 6. Tech Stack
- **Frontend/UI**: Streamlit (Modern dark-mode design), Plotly, Chart.js.
- **Backend API**: Python FastAPI (available for headless API access).
- **Intelligence**: Llama 3.3 70B via Groq API.
- **Storage**: Local SQLite for high-speed reproducibility.

## 🔄 7. Reproducibility
Our system ensures deterministic results for the NRT Challenge:
- **Local Persistence**: Calculation for "Spikes" and "YoY Change" will yield identical results across different systems due to local data caching.
- **Fixed Seeds**: LLM temperature is optimized for consistent narrative summaries.

---
**Team WeatherTwin** | *Final Submission for NRT AI Challenge (April 2026)*
