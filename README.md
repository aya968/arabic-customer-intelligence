
---

```markdown
# 📊 Arabic Customer Intelligence Platform

An end-to-end Machine Learning and Natural Language Processing (NLP) system designed to analyze Arabic customer reviews, classify sentiments, handle emojis intelligently, and discover hidden business topics using **BERTopic** and **Streamlit**.

---

## 🚀 Key Features

* **Advanced Arabic Preprocessing Pipeline:**
  * Custom normalization for Arabic letters and removal of Tashkeel.
  * Intelligent emoji-to-Arabic mapping (`EMOJI_TO_ARABIC`) to preserve sentimental value instead of raw deletion.
  * Comprehensive Arabic Stop Words filtering to reduce noise and irrelevant prepositions.
  * Regex-based noise reduction (URLs, social media handles, elongated characters, and repetition).
* **Topic Modeling (BERTopic):**
  * Unsupervised clustering of customer feedback to automatically detect recurring pain points and complaints.
  * Pre-computed model serialization (`pickle`) for high-performance and zero-lag inference.
* **Sentiment Classification:**
  * Machine learning models (Logistic Regression & TF-IDF) to evaluate review polarity.
* **Interactive Dashboard (Streamlit):**
  * Clean, modular UI for real-time prediction, company topic exploration, and deep customer insights.

---

## 🛠️ Project Architecture

The project follows a clean, modular software engineering structure:

```text
arabic-customer-intelligence/
│
├── models/                  # Serialized ML models & BERTopic pickles
│   ├── logistic_model.pkl
│   ├── tfidf_vectorizer.pkl
│   └── companies_topics.pkl
│
├── src/                     # Core source code
│   ├── config.py            # Centralized paths, regex patterns, and dictionaries
│   ├── preprocessing.py     # Text cleaning & Arabic NLP pipeline
│   ├── inference.py         # Model prediction logic
│   └── routing.py           # Streamlit UI views & layout routing
│
├── app.py                   # Main Streamlit application entry point
├── requirements.txt         # Project dependencies
└── README.md                # Project documentation

```
---

## 📈 Model Evaluation & Performance

The Sentiment Classification model (Logistic Regression with TF-IDF) was evaluated on a test dataset of **7,251 customer reviews**, demonstrating strong generalization and balance across both negative and positive classes:

| Class | Precision | Recall | F1-Score | Support |
| :--- | :---: | :---: | :---: | :---: |
| **Negative (0)** | 0.84 | 0.86 | 0.85 | 2,743 |
| **Positive (1)** | 0.92 | 0.90 | 0.91 | 4,508 |
| **Overall Accuracy** | — | — | **0.89** | **7,251** |
| **Macro Average** | 0.88 | 0.88 | 0.88 | 7,251 |
| **Weighted Average** | 0.89 | 0.89 | 0.89 | 7,251 |

### 🔍 Key Evaluation Insights:
* **High Overall Accuracy (89%):** The model accurately classifies 9 out of 10 customer reviews correctly across unbalanced datasets.
* **Strong Positive Class Detection (91% F1-Score):** Excellent capability in capturing positive feedback (`Recall = 0.90`) with high precision (`Precision = 0.92`).
* **Robust Negative Class Detection (85% F1-Score):** Successfully flags negative feedback (`Recall = 0.86`), which is crucial for pain-point detection and risk mitigation in customer service.

---

## ⚙️ Installation & Setup

1. **Clone the repository:**
```bash
git clone [https://github.com/aya968/arabic-customer-intelligence.git](https://github.com/aya968/arabic-customer-intelligence.git)
cd arabic-customer-intelligence

```


2. **Create and activate a virtual environment:**
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

```


3. **Install dependencies:**
```bash
pip install -r requirements.txt

```


4. **Run the Streamlit application:**
```bash
streamlit run app.py

```



---

## 💡 Tech Stack

* **Programming Language:** Python
* **Machine Learning & NLP:** Scikit-Learn, BERTopic, Emoji, Regular Expressions (Re)
* **Data Visualization & Dashboard:** Streamlit, Pandas, NumPy
* **Architecture:** Modular Design, Pickle Caching

---

## 👩‍💻 Author

**Aya Ali Hassan**

*AI & Data Science Engineer*

[GitHub Profile](https://github.com/aya968)

```


```