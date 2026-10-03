# AI Data Analyst Portfolio Projects

This document contains four high-impact, industry-aligned portfolio projects designed to showcase end-to-end data analytics, machine learning, and business intelligence skills.

---

## Project 1: E-Commerce Customer Churn & Lifetime Value (LTV) Prediction

### Business Problem
A subscription-based e-commerce company is experiencing a 12% quarterly customer churn rate. Acquiring new customers costs 5x more than retaining existing ones. The leadership team needs a system to identify at-risk customers early and optimize retention marketing spend.

### Technical Stack
* **Languages & Libraries:** Python (`pandas`, `scikit-learn`, `xgboost`, `shap`)
* **Database & Querying:** PostgreSQL / Supabase
* **Interactive Dashboard:** Streamlit or Tableau
* **Deployment:** FastAPI + Render

### Project Architecture & Workflow
1. **Data Pipeline:** Ingest transactional history, user event logs, and support ticket data into PostgreSQL.
2. **Feature Engineering:** Calculate RFM (Recency, Frequency, Monetary) metrics, average order value trend, customer service interaction sentiment, and session activity frequency.
3. **Model Development:** Train an **XGBoost Classifier** to predict probability of churn within 30 days. Evaluate using ROC-AUC (target > 0.85) and Precision-Recall curves.
4. **Model Explainability:** Use **SHAP (SHapley Additive exPlanations)** values to generate individual risk factor reports for customer success teams.
5. **Business Value Output:** Calculate expected financial savings by segmenting users into churn risk bands and targeting high-value users with automated promotional incentives.

### Portfolio Deliverables to Include
* `notebooks/churn_modeling.ipynb`: Complete EDA, feature engineering, model tuning, and evaluation.
* `app/main.py`: A FastAPI endpoint serving real-time churn predictions for input customer IDs.
* `dashboard/`: Embeddable dashboard screenshot showing the churn risk segment distribution and high-risk customer lists.

---

## Project 2: Automated Financial News Sentiment & Stock Movement Analyzer

### Business Problem
Investment analysts waste hours reading financial reports and market news to gauge market sentiment. An automated pipeline that correlates real-time news sentiment with stock price movements allows analysts to detect trends faster.

### Technical Stack
* **LLM & NLP:** OpenAI API / Hugging Face (`FinBERT`)
* **Orchestration:** Python (`asyncio`, `apscheduler`)
* **Data Sources:** Financial news RSS feeds, Yahoo Finance API (`yfinance`)
* **Visualization:** Power BI or Plotly / Dash

### Project Architecture & Workflow
1. **Data Ingestion:** Fetch daily market news articles and ticker prices using background Python workers.
2. **Sentiment Analysis:** Process article headlines and summaries using `FinBERT` (or GPT-4 with structured outputs) to extract sentiment scores (Positive, Negative, Neutral) and key topics.
3. **Correlation Engine:** Align sentiment scores with 1-day, 3-day, and 7-day price returns using time-series alignment.
4. **Interactive Dashboard:** Build a dashboard featuring sentiment trends alongside moving average stock indicators.

### Portfolio Deliverables to Include
* `src/sentiment_pipeline.py`: Automated ingestion and LLM sentiment classification script.
* `reports/sentiment_vs_returns_analysis.md`: Detailed report on correlation strength between news sentiment and price movement across major market sectors.

---

## Project 3: Supply Chain Inventory Optimization & Demand Forecasting

### Business Problem
A regional retail distributor faces stockout costs on high-demand items while overstocking low-velocity inventory, leading to inflated warehousing costs and capital lockup.

### Technical Stack
* **Time-Series Forecasting:** Prophet, LightGBM, `statsmodels` (ARIMA/SARIMAX)
* **Data Handling:** Python (`pandas`, `numpy`)
* **BI & Reporting:** Power BI / Looker Studio

### Project Architecture & Workflow
1. **Exploratory Data Analysis:** Identify seasonality patterns, regional purchasing variances, and stockout historical events.
2. **Forecasting Model:** Build a multi-item forecasting model comparing **Prophet** against **LightGBM** with lag variables and holiday indicators.
3. **Inventory Logic Implementation:** Calculate Safety Stock, Reorder Points (ROP), and Economic Order Quantity (EOQ) based on predicted demand and lead time variability.
4. **Executive Dashboard:** Display 30-day forecast demand, recommended purchase orders, and cost optimization metrics.

### Portfolio Deliverables to Include
* `notebooks/inventory_forecasting.ipynb`: Time-series modeling and safety stock mathematical formulation.
* `dashboard_preview.png`: Executive dashboard demonstrating real-time inventory alerts and reorder recommendations.

---

## Project 4: Conversational AI Analytics Agent (Text-to-SQL for Business Metrics)

### Business Problem
Non-technical business stakeholders frequently request custom database queries, creating a backlog for the data team. An AI agent that allows executives to ask plain-English questions and receive accurate data visualization solves this bottleneck.

### Technical Stack
* **Framework:** LangChain / LlamaIndex, Python
* **LLM Provider:** OpenAI GPT-4o
* **SQL Engine:** SQLite / PostgreSQL
* **Frontend Interface:** Streamlit

### Project Architecture & Workflow
1. **Database Schema Setup:** Design a realistic relational database containing sales, marketing, and product tables.
2. **Text-to-SQL Agent:** Implement a LangChain agent with schema-aware prompting, query verification logic, and SQL execution safety bounds.
3. **Data Visualization Generation:** Automatically generate Plotly charts from returned SQL result sets.
4. **Evaluation Benchmark:** Test agent accuracy against a suite of 50 complex business queries (e.g., joins, aggregations, conditional filters).

### Portfolio Deliverables to Include
* `app/agent.py`: LangChain Text-to-SQL pipeline with error-correction and validation logic.
* `README.md`: System design diagram and benchmark results showing query execution accuracy.

---

## Portfolio Presentation Best Practices
1. **GitHub Repository Structure:** Ensure every project includes a clear `README.md` with an **Executive Summary**, **Architecture Diagram**, **Key Results/Business Impact**, and **Instructions to Run**.
2. **Live Demos:** Host interactive apps on free platforms like Streamlit Community Cloud or Render.
3. **Result Highlights:** State quantifiable impact directly in your resume points (e.g., *"Built XGBoost churn model achieving 0.88 ROC-AUC, identifying $120k potential revenue loss"*).