# AI Career Trends Radar 📈🤖

An end-to-end data pipeline to monitor and analyze emerging career trends in Artificial Intelligence (AI) and technology fields — including Data Engineering, AI Engineering, and Cybersecurity.

## 🎯 Objective

To build a fully automated ETL pipeline that:

- Collects career trend data from sources like **Google Trends** and **OpenAI (ChatGPT)**
- Transforms raw data into clean, structured insights
- Generates weekly reports in **CSV/JSON**
- Prepares data for dashboards and long-term analysis
- Is extensible to include new sources like **Reddit**, **LinkedIn**, or **Kaggle**

## 🛠️ Technologies Used

- **Python** – scripting, automation
- **Pandas** – data manipulation
- **OpenAI API** – career insights generation
- **Google Trends (PyTrends)** – popularity over time
- **Apache Airflow** – pipeline automation (coming soon)
- **Git & GitHub** – version control
- **Docker** – environment reproducibility
- **SQLite** – optional local storage

## 📁 Project Structure

```
ai-career-trends-radar/
├── etl/             # extract.py, transform.py, load.py scripts
├── data/            # raw and processed data (CSV, JSON, Markdown)
├── reports/         # auto-generated weekly summaries
├── scripts/         # automation helpers (scheduling, email, etc.)
├── .env.example     # template for your OpenAI API key
├── main.py          # entry point for pipeline execution
└── README.md
```

## 🔄 Workflow

1. **Extract** data from:
   - Google Trends (job title search volume)
   - OpenAI (insights on emerging roles via GPT)
2. **Transform** raw data into structured DataFrames
3. **Load** into CSV and JSON formats for further analysis
4. (Soon) **Automate** the entire process using Apache Airflow

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/seu-usuario/ai-career-trends-radar.git
cd ai-career-trends-radar
```

### 2. Set up the virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configure API key
Create a `.env` file:
```env
OPENAI_API_KEY=sk-xxxxxxx...
```

### 4. Run the ETL pipeline manually
```bash
python main.py
```

---

## 📝 Status

🚧 **Project in active development**  
Upcoming features:
- Airflow DAG integration
- Streamlit dashboard
- Multi-language support (EN/PT)

---

## 🤝 Contributing

This is a personal learning project but open to improvements.  
Feel free to fork, suggest enhancements, or create pull requests.

---

## 📬 Contact

Created by [Alexandre Faria](https://www.linkedin.com/in/aleqfaria) – transitioning into Data Engineering.
